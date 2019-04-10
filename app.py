from flask import Flask

app = Flask(__name__)


@app.route('/')
def startpage():
    return ads()


@app.route('/stream')
def stream():
    from logic.activities import validate, example
    return validate(example).__str__()


@app.route('/ads')
def ads():
    from logic.ads import paper, validate
    return validate(paper).__str__()


if __name__ == '__main__':
    app.run()