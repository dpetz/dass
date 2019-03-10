from flask import Flask
from logic.simulate import Simulation
from logic.models import Activities, Ad

app = Flask(__name__)


@app.route('/')
def startpage():
    return stream()


@app.route('/stream')
def stream(n=100):
    return Activities.example().__str__()


@app.route('/ads')
def ads():
    states = ['GDN', 'PLA']
    # ad = Ad('display',states, .2, .1, 5)
    return 'test'


if __name__ == '__main__':
    app.run()