from flask import render_template
from app import app

@app.route("/")
def index():
    """Method which returns index.html page

    Returns:
        index.html page
    """
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    """Method which returns result.html page
    
    Returns:
        result.html page
    """
    return render_template("result.html")