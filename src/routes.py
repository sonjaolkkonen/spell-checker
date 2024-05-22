from flask import render_template, request
from app import app
from services.spell_checker import SpellChecker

spell_checker = SpellChecker()

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles the index page and processes the form submission.

    Returns:
        index.html page
    """
    suggestion = None
    if request.method == "POST":
        incorrect_word = request.form["word"]
        suggestion = spell_checker.suggest(incorrect_word)
    return render_template("index.html", suggestion=suggestion)