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
    """Checks the spelling of the given word

    Returns:
        index.html page which shows suggestions for the given word
    """
    word = request.form.get("input_word")
    if spell_checker.find_word(word):
        suggestions = "Ei kirjoitusvirheitä"
        return render_template("index.html", suggestions=suggestions)
    suggestions = spell_checker.suggest(word)
    if len(suggestions) == 0:
        suggestions = "Sanaa ei löytynyt sanastosta"
        return render_template("index.html", suggestions=suggestions)
    return render_template("index.html", suggestions=suggestions)

@app.route("/fix_spelling", methods=["POST"])
def fix_spelling():
    """Fixes typos of the given text

    Returns:
        result.html page which includes the fixed text
    """
    text = spell_checker.parse_text(request.form.get("input_text"))
    fixed_words = spell_checker.fix_typos(text)
    fixed_text = spell_checker.return_into_text(fixed_words)
    return render_template("result.html", fixed_text=fixed_text)
