# Zaisa Makeover — Website (Python / Flask)

This is the Zaisa Makeover website, served with a small Python (Flask) web app,
using your real brand logo.

## Project structure

```
zaisa_flask/
├── app.py                 # Flask server
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # the website page
└── static/
    ├── logo.png            # full logo (nav + hero)
    └── logo-icon.png       # cropped icon-only logo (footer)
```

## Run it locally

1. (Recommended) create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate      # on Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Start the server:
   ```
   python app.py
   ```

4. Open your browser to:
   ```
   http://127.0.0.1:5000
   ```

## Notes

- `debug=True` in `app.py` auto-reloads the page whenever you edit `templates/index.html` — turn this off before deploying live.
- To deploy for real visitors, host this with a production server (e.g. Gunicorn) behind a platform like Render, Railway, PythonAnywhere, or a VPS.
