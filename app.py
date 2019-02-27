from flask import Flask
import numpy as np
from models.activities import Stream
from models.ads import AdType


app = Flask(__name__)

@app.route('/')
def startpage():
    return stream()

@app.route('/stream')
def stream(n=100):
    states = ["search", "site visit", "conversion"]
    init = [.6,.3,.1]
    transitions = [[.3,.7,0.],[.2,.6,.2],[0.,0.,1.]]
    return Stream(states, init,transitions).simulate(n).__str__()

@app.route('/ads')
def ads():
    states = ['GDN', 'PLA']
    ad = AdType('display',states, .2, .1, 5)
    return ad.__str__()


if __name__ == '__main__':
    app.run()