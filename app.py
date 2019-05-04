from flask import Flask

app = Flask(__name__)


@app.route('/')
def startpage():
    return stream()


@app.route('/stream')
def stream():
    from logic.activities import validate, paper
    return validate(paper).__str__()


@app.route('/ads')
def ads():
    from logic.ads import paper, validate
    return validate(paper).__str__()


if __name__ == '__main__':
    app.run()