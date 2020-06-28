from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask (__name__)

@app.route('/', methods=['GET'])
def home():
    return redirect ("/me")

@app.route('/me', methods=['GET'])
def me():
    return render_template("me.html")

@app.route('/contact', methods=['GET'])
def cont():
    return redirect("contact.html")

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect ("/contact.html")
