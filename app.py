from flask import Flask
import numpy as np
from models.activities import Stream

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/stream')
def stream():
    states = ["search", "site visit", "conversion"]
    init_probs = [0.6,0.3,0.1]
    transitions = np.matrix('0.3 0.7 0; 0.2 0.6 0.2; 0 0 1.0')
    return Stream(states, init_probs,transitions).__str__()

if __name__ == '__main__':
    app.run()
