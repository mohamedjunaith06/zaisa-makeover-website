"""
Zaisa Makeover — Website Server
--------------------------------
A small Flask app that serves the Zaisa Makeover website.

How to run:
    1. Install Flask:      pip install flask
    2. Start the server:   python app.py
    3. Open in a browser:  http://127.0.0.1:5000

Project structure:
    app.py                  <- this file
    templates/index.html    <- the website page
    static/zaisa-logo.png   <- logo (PNG)
    static/zaisa-logo.svg   <- logo (SVG)
"""

# pyrefly: ignore [missing-import]
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Serve the Zaisa Makeover homepage."""
    return render_template("index.html")


if __name__ == "__main__":
    # debug=True auto-reloads the page whenever you edit index.html
    app.run(debug=True, host="127.0.0.1", port=5000)
