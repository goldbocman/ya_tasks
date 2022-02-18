import json

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    styles = url_for('static', filename='css/style.css')
    return render_template('index.html', title=title, styles=styles)


@app.route('/training/<prof>')
def training(prof):
    ing = url_for('static', filename='img/ing.png')
    sci = url_for('static', filename='img/sci.png')
    styles = url_for('static', filename='css/style.css')
    return render_template('profs.html', prof=prof, ing=ing, sci=sci, styles=styles)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')