from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/s')
def search():
    from spider import info
    word = request.args.get('wd')
    if word is not None:
        return info(word)
    else:
        return " "
