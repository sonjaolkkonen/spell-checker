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
        incorrect_word = request.form["word"]
        suggestions = spell_checker.suggest(incorrect_word)
    return render_template("index.html", suggestions=suggestions)
