import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/queue')
def queue():
    return render_template('queue.html')


@app.route('/odd_even/<input_number>')
def odd_even(input_number):
    return render_template('odd_even.html', number=int(input_number))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')