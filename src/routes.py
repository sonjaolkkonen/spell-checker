from flask import Flask, render_template, request
from services.spell_checker import SpellChecker

app = Flask(__name__)
spell_checker = SpellChecker()

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles the index page and processes the form submission.

    Returns:
        index.html page
    """
    suggestions = None
    if request.method == "POST":
        text = request.form["text"]
        suggestions = spell_checker.suggest_text(text)
    return render_template("index.html", suggestions=suggestions)
