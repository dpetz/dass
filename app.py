from flask import Flask
# import numpy as np
from models import simulate
from models.states import States
from models.ads import Ad


app = Flask(__name__)


@app.route('/')
def startpage():
    return stream()


@app.route('/stream')
def stream(n=100):
    states = ["search", "site visit", "conversion",'churn']
    init = [.6,.3,.1,0.]
    transitions = [[.3,.5,0.,.2],[.2,.6,.1,.1],[0.,0.,1.,0.],[0.,0.,0.,1.]]
    states = States(states,init,transitions)
    return simulate.streams(states).__str__()


@app.route('/ads')
def ads():
    states = ['GDN', 'PLA']
    ad = Ad('display',states, .2, .1, 5)
    return ad.__str__()


if __name__ == '__main__':
    app.run()