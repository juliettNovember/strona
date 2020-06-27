from flask import Flask
from flask import render_template

app = Flask (__name__)

@app.route('/omnie')
def home():
    return render_template("omnie.html")

# @app.route('/kontakt.html')
# def contact():
#     inscriptions = "Kontakt"
#     inscription = ["email: nowakowska.just@gmail.com ", "telefon: 505-350-391"]
#     return render_template("kontakt.html", inscriptions=inscriptions)

@app.route('/kontakt.html')
def contact():
    inscription = ["imię"]
    return render_template("omnie.html", inscription=inscription)