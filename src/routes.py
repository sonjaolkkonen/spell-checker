from flask import Flask, render_template, request
from services.spell_checker import SpellChecker

app = Flask(__name__)
spell_checker = SpellChecker("src/data/words.txt")

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
        suggest.html page which shows suggestions for the given word
    """
    word = request.form.get("input_word")
    if spell_checker.find_word(word):
        suggestions = "Ei kirjoitusvirheitä"
        return render_template("index.html", suggestions=suggestions)
    suggestions = spell_checker.suggest(word)
    if len(suggestions) == 0:
        suggestions = "Sanaa ei löytynyt sanastosta"
        return render_template("suggest.html", word=word, suggestions=suggestions)
    return render_template("suggest.html", word=word, suggestions=suggestions)

@app.route("/fix_spelling", methods=["POST"])
def fix_spelling():
    """Fixes typos of the given text

    Returns:
        result.html page which includes the fixed text
    """
    text = spell_checker.parse_text(request.form.get("input_text"))
    fixed_words = spell_checker.fix_typos(text)
    fixed_text = spell_checker.return_into_text(fixed_words[0])
    able_to_correct = fixed_words[1]
    if not able_to_correct:
        return render_template("result.html", fixed_text=fixed_text, message="Huom! Kaikkia sanoja ei voitu korjata.")
    return render_template("result.html", fixed_text=fixed_text)

@app.route("/<word>/add", methods=["POST"])
def add(word):
    """Adds words given by the user to the vocabulary

    Args:
        word (str): word given by the user

    Returns:
        message.html page which includes info whether the adding was successful or not
    """
    input = word
    if input and spell_checker.add_word(input):
        return render_template("message.html", message="Sanan lisääminen onnistui")
    return render_template("message.html", message="Sanan lisääminen ei onnistunut")
