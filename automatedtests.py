import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class AutomatedTests(unittest.TestCase):
    # Checks that the project's home screen HTML file is present.
    def test_homescreen_file_exists(self):
        self.assertTrue((ROOT / "homescreen.html").exists())

    # Checks that the translator page HTML file is present.
    def test_translate_page_exists(self):
        self.assertTrue((ROOT / "translate2.html").exists())

    # Checks that the statistics page HTML file is present.
    def test_stats_page_exists(self):
        self.assertTrue((ROOT / "Stats.html").exists())

    # Checks that the JSON file containing dictionary data is present.
    def test_dictionary_json_exists(self):
        self.assertTrue((ROOT / "dictionary_data.json").exists())

    # Checks that the dictionary JSON parses into a list with more than 100 entries.
    def test_dictionary_json_is_valid_and_not_empty(self):
        with open(ROOT / "dictionary_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 100)

    # Checks that every dictionary entry has English and Noongar string values.
    def test_dictionary_entries_have_required_fields(self):
        with open(ROOT / "dictionary_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        for entry in data:
            self.assertIn("english", entry)
            self.assertIn("noongar", entry)
            self.assertIsInstance(entry["english"], str)
            self.assertIsInstance(entry["noongar"], str)

    # Checks that the word "banksia" does not appear anywhere in the dictionary data.
    def test_banksia_is_not_in_dictionary_entries(self):
        with open(ROOT / "dictionary_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        text = json.dumps(data).lower()
        self.assertNotIn("banksia", text)

    # Checks that the home and translator pages contain their expected text and data marker.
    def test_html_pages_contain_expected_content(self):
        home_page = (ROOT / "homescreen.html").read_text(encoding="utf-8", errors="ignore")
        translate_page = (ROOT / "translate2.html").read_text(encoding="utf-8", errors="ignore")

        self.assertIn("Noongar", home_page)
        self.assertIn("Translator", translate_page)
        self.assertIn("FOOD_DATA", translate_page)

    # Checks that slash-separated English terms are matched individually for yellow exact-match chips.
    def test_slash_separated_english_terms_match_individually(self):
        translate_page = (ROOT / "translate2.html").read_text(encoding="utf-8", errors="ignore")

        self.assertIn('entry.english.split("/")', translate_page)
        self.assertIn("query === clean(englishTerms[termIndex])", translate_page)
        self.assertIn("matches.appendChild(makeChip(entry.noongar, entry.english, !exactMatch))", translate_page)


if __name__ == "__main__":
    unittest.main()
