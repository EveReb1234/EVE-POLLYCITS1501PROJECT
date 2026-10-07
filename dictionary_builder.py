import json
import re
from pathlib import Path

import pymupdf
from rapidocr_onnxruntime import RapidOCR

PDF_PATH = Path(__file__).with_name("Noongar-Dictionary-Second-Edition.pdf")
OUTPUT_PATH = Path(__file__).with_name("dictionary_data.json")


def clean_text(value: str) -> str:
    text = value.replace("’", "'").replace("—", "-")
    text = re.sub(r"[^A-Za-z0-9\s'-]", "", text)
    text = " ".join(text.split())
    return text


def build_dictionary(pdf_path: Path = PDF_PATH, output_path: Path = OUTPUT_PATH):
    if not pdf_path.exists():
        raise FileNotFoundError(f"Dictionary PDF not found: {pdf_path}")

    ocr = RapidOCR()
    doc = pymupdf.open(str(pdf_path))
    seen = set()
    entries = []

    for page_num in range(1, doc.page_count + 1):
        page = doc[page_num - 1]
        pix = page.get_pixmap(dpi=180)
        temp_path = Path(f"__ocr_page_{page_num}.png")
        pix.save(str(temp_path))
        try:
            result, _ = ocr(str(temp_path))
        finally:
            if temp_path.exists():
                temp_path.unlink()

        if not result:
            continue

        rows = {}
        for box, text, _ in result:
            cleaned = clean_text(text)
            if not cleaned or len(cleaned) < 2:
                continue
            xs = [point[0] for point in box]
            ys = [point[1] for point in box]
            x_center = sum(xs) / len(xs)
            y_center = sum(ys) / len(ys)
            row_key = round(y_center / 12) * 12
            rows.setdefault(row_key, []).append((x_center, cleaned))

        for items in rows.values():
            items.sort(key=lambda pair: pair[0])
            left_candidates = [value for x, value in items if x < 1900]
            right_candidates = [value for x, value in items if x > 2100]

            if len(left_candidates) != 1 or not right_candidates:
                continue

            left = clean_text(left_candidates[0])
            right = clean_text(right_candidates[0])

            if not left or not right:
                continue

            lower_left = left.lower()
            lower_right = right.lower()
            if lower_left in {"noongar", "english", "the", "page", "diagram", "letters", "used", "speech", "sounds"}:
                continue
            if lower_right in {"noongar", "english", "page", "diagram", "letters", "used"}:
                continue
            if len(left.split()) > 4 or len(right.split()) > 8:
                continue

            entry = {"english": right, "noongar": left}
            key = (entry["english"].lower(), entry["noongar"].lower())
            if key in seen:
                continue
            seen.add(key)
            entries.append(entry)

    entries.sort(key=lambda item: item["english"].lower())
    output_path.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    return entries


if __name__ == "__main__":
    entries = build_dictionary()
    print(f"Built dictionary with {len(entries)} entries.")
