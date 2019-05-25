"""..."""

from flask import Flask

from logic import paper
from logic.states import verify_states
from logic.ads import verify_ads
from logic.simulate import streams
from logic import db
from tinydb import Query
import time

from util.seqs import seq_not_str


def pretty(d, indent=0):
    """..."""
    if seq_not_str(d):
        return str(list(map(pretty, d)))
    elif isinstance(d, dict):
        s = ''
        for key, value in d.items():
            s += '\t' * indent + str(key)
            if isinstance(value, dict):
                s += pretty(value, indent+1)
            else:
                s += '\t' * (indent+1) + str(value)
        return s + '\n'
    else:
        return str(d)


app = Flask(__name__)


@app.route('/')
def startpage():
    """..."""
    return data()


@app.route('/data')
def data():
    """..."""
    return pretty(db.search(Query().timestamp == 1558383417.0162141))


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

    sim = {'states': states, 'ads': ads, 'impress': impressibilities, 'n': 1000}

    sim['streams'] = streams(**sim)
    sim['timestamp'] = time.time()
    db.insert(sim)
    return sim.__str__()


if __name__ == '__main__':
    app.run()
