# Noongar Language Explorer

This project is a small web-based language learning and dictionary application focused on Noongar words, meanings, and cultural context. It includes a landing page, a translator/search interface, and supporting data used to display word entries.

## Project overview

The project contains:

- `homescreen.html` – home page / landing screen
- `translate2.html` – translator and dictionary lookup interface
- `Stats.html` – statistics or language information page
- `dictionary_builder.py` – Python script for building word data from the source PDF
- `dictionary_data.json` – generated dictionary dataset used by the app
- `Noongar-Dictionary-Second-Edition.pdf` – source reference dictionary

## Purpose

The application helps users explore Noongar vocabulary and meanings in a browser-based format, making it easier to search words, review language data, and learn common terms.

## Install and run

1. Open the project folder in VS Code or your preferred editor.
2. Activate the Python virtual environment:

   ```bash
   source .venv/bin/activate
   ```

3. Open the HTML page in a browser:

   - `homescreen.html` for the main landing page
   - `translate2.html` for the translator/dictionary page

You can also run a simple local web server if preferred, for example:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/homescreen.html
```

## Data / dictionary generation

The script `dictionary_builder.py` reads the PDF dictionary and uses OCR to extract entries into `dictionary_data.json`.

To regenerate the dictionary data:

```bash
source .venv/bin/activate
python dictionary_builder.py
```

## Testing

Run the automated project checks with:

```bash
source .venv/bin/activate
python -m unittest automatedtests.py
```

## Notes

- This project is designed as a lightweight front-end app using static HTML and JavaScript.
- Data is stored in JSON format and rendered in the browser.
- The app is intended for educational and cultural language exploration purposes.

## Project status

The project is currently a working prototype / student project focused on Noongar language exploration and translation support.

