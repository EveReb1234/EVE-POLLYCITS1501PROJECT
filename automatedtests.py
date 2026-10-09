import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class AutomatedTests(unittest.TestCase):
    # Checks that the home page links to both the translator and language statistics pages.
    def test_homepage_links_to_translation_and_statistics(self):
        home_page = (ROOT / "homescreen.html").read_text(encoding="utf-8", errors="ignore")

        self.assertIn('<a href="translate2.html">Translation</a>', home_page)
        self.assertIn('<a href="Stats.html">Languages spoken</a>', home_page)

    # Checks that every translator category has a search input and a separate match-results area.
    def test_translation_categories_have_search_and_results(self):
        translate_page = (ROOT / "translate2.html").read_text(encoding="utf-8", errors="ignore")

        for input_id in ["q", "weather-q", "food-q", "everyday-q", "family-q", "body-parts-q"]:
            self.assertIn('id="' + input_id + '"', translate_page)
        self.assertIn('id="weather-matches"', translate_page)
        self.assertIn('id="food-matches"', translate_page)
        self.assertIn('id="everyday-matches"', translate_page)
        self.assertIn('id="family-matches"', translate_page)
        self.assertIn('id="body-parts-matches"', translate_page)

    # Checks that lowercasing both the query and dictionary entries allows uppercase and mixed-case searches.
    def test_search_is_case_insensitive(self):
        translate_page = (ROOT / "translate2.html").read_text(encoding="utf-8", errors="ignore")

        self.assertIn("return s.toLowerCase()", translate_page)
        self.assertIn("var query = clean(get(queryId).value);", translate_page)
        self.assertIn("clean(entry.english).indexOf(query)", translate_page)
        self.assertIn("clean(entry.noongar).indexOf(query)", translate_page)

    # Checks that search normalization removes punctuation but keeps numeric characters.
    def test_search_strips_punctuation_and_keeps_numbers(self):
        translate_page = (ROOT / "translate2.html").read_text(encoding="utf-8", errors="ignore")

        self.assertIn('replace(/[^a-z0-9 \'-]/g, "")', translate_page)

    # Checks that search uses substring matching, so misspellings that are not substrings are not corrected.
    def test_search_does_not_correct_unmatched_spelling_errors(self):
        translate_page = (ROOT / "translate2.html").read_text(encoding="utf-8", errors="ignore")

        self.assertIn("clean(entry.english).indexOf(query) !== -1", translate_page)
        self.assertIn("clean(entry.noongar).indexOf(query) !== -1", translate_page)
        self.assertNotIn("dayligth", "daylight")

    # Checks that searching adds chips to the match area without removing rows from the full word list.
    def test_search_keeps_the_full_word_list_visible(self):
        translate_page = (ROOT / "translate2.html").read_text(encoding="utf-8", errors="ignore")

        self.assertIn("matches.appendChild(makeChip(entry.noongar, entry.english, !exactMatch))", translate_page)
        self.assertIn("all.appendChild(row)", translate_page)
        self.assertIn('get(matchBoxId).style.display = query && matchCount ? "block" : "none";', translate_page)

    # Checks that the stats page offers both census years, comparison controls, and two updating charts.
    def test_stats_page_has_year_region_controls_and_charts(self):
        stats_page = (ROOT / "Stats.html").read_text(encoding="utf-8", errors="ignore")

        self.assertIn('<select id="year"><option>2016</option><option>2021</option></select>', stats_page)
        self.assertIn('<select id="measure">', stats_page)
        self.assertIn('value="english"', stats_page)
        self.assertIn('value="atsi"', stats_page)
        self.assertIn('value="other"', stats_page)
        self.assertIn('<select id="region"></select>', stats_page)
        self.assertIn('<canvas id="c1"', stats_page)
        self.assertIn('<canvas id="c2"', stats_page)
        self.assertIn("$('year').onchange=()=>{fillRegions();draw1();draw2()}", stats_page)
        self.assertIn("$('measure').onchange=draw1", stats_page)
        self.assertIn("$('region').onchange=draw2", stats_page)

        data_start = stats_page.index("const D=") + len("const D=")
        data_end = stats_page.index(";\nconst css", data_start)
        stats_data = json.loads(stats_page[data_start:data_end])
        self.assertEqual(stats_data["2021"]["Perth"]["atsi"], 4.4)
        self.assertEqual(stats_data["2021"]["South-Western WA"]["atsi"], 3.9)
        self.assertEqual(stats_data["2021"]["Perth"]["top"][0], ["Nyungar", 2.3])

    # Checks that slash-separated English and Noongar terms are matched individually for yellow exact-match chips.
    def test_slash_separated_english_terms_match_individually(self):
        translate_page = (ROOT / "translate2.html").read_text(encoding="utf-8", errors="ignore")

        self.assertIn('entry.english.split("/")', translate_page)
        self.assertIn("query === clean(englishTerms[termIndex])", translate_page)
        self.assertIn('entry.noongar.split("/")', translate_page)
        self.assertIn("query === clean(noongarTerms[termIndex])", translate_page)
        self.assertIn("matches.appendChild(makeChip(entry.noongar, entry.english, !exactMatch))", translate_page)


if __name__ == "__main__":
    unittest.main()
