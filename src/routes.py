from flask import Flask, render_template, request
from services.spell_checker import SpellChecker

app = Flask(__name__)
spell_checker = SpellChecker()

@app.route("/")
def index():
    """Handles the index page and processes the form submission.

    Returns:
        index.html page
    """
    return render_template("index.html")

@app.route("/check_spelling", methods=["POST"])
def check_spelling():
    word = request.form.get("input_word")
    if spell_checker.find_word(word):
        suggestions = "Ei kirjoitusvirheitä"
        return render_template("index.html", suggestions=suggestions)
    suggestions = spell_checker.suggest(word)
    return render_template("index.html", suggestions=suggestions)
    

