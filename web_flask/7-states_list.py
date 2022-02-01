#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from models import storage, State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    Function that returns a list of states
    """
    a_dict = storage.all('State').values()
    return render_template('7-states_list.html', my_dict=a_dict)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
