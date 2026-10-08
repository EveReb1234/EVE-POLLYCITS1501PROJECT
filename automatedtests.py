import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class AutomatedTests(unittest.TestCase):
    def test_homescreen_file_exists(self):
        self.assertTrue((ROOT / "homescreen.html").exists())

    def test_translate_page_exists(self):
        self.assertTrue((ROOT / "translate2.html").exists())

    def test_stats_page_exists(self):
        self.assertTrue((ROOT / "Stats.html").exists())

    def test_dictionary_json_exists(self):
        self.assertTrue((ROOT / "dictionary_data.json").exists())

    def test_dictionary_json_is_valid_and_not_empty(self):
        with open(ROOT / "dictionary_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 100)

    def test_dictionary_entries_have_required_fields(self):
        with open(ROOT / "dictionary_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        for entry in data:
            self.assertIn("english", entry)
            self.assertIn("noongar", entry)
            self.assertIsInstance(entry["english"], str)
            self.assertIsInstance(entry["noongar"], str)

    def test_banksia_is_not_in_dictionary_entries(self):
        with open(ROOT / "dictionary_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        text = json.dumps(data).lower()
        self.assertNotIn("banksia", text)

    def test_html_pages_contain_expected_content(self):
        home_page = (ROOT / "homescreen.html").read_text(encoding="utf-8", errors="ignore")
        translate_page = (ROOT / "translate2.html").read_text(encoding="utf-8", errors="ignore")

        self.assertIn("Noongar", home_page)
        self.assertIn("Translator", translate_page)
        self.assertIn("FOOD_DATA", translate_page)


if __name__ == "__main__":
    unittest.main()
