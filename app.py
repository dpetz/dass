"""..."""

from flask import Flask

from logic import paper
from logic.states import verify_states
from logic.ads import verify_ads
from logic.simulate import streams


app = Flask(__name__)


@app.route('/')
def startpage():
    """..."""
    return simulate()


@app.route('/states')
def states():
    """..."""
    paper_states = verify_states(paper.states)
    return paper_states.__str__()


@app.route('/ads')
def ads():
    """..."""
    paper_ads = verify_ads(paper.ads)
    return paper_ads.__str__()


@app.route('/simulate')
def simulate():
    """..."""
    from logic.paper import states, ads, impressibilities
    sim = streams(states, ads, impressibilities,1000)
    return sim.__str__()


if __name__ == '__main__':
    app.run()
