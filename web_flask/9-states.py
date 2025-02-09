#!/usr/bin/python3
""" Starts a Flask web application for listing states and cities """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Display states and their cities if an ID is provided."""
    states = storage.all(State)
    if id:
        state = states.get(f"State.{id}")
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', states=states.values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
