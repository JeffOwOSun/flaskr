# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

#create our little application OwO
app = Flask(__name__)
app.config.from_object(__name__)

#Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS',silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory=sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request. This is the reaction function of the event teardown appcontext. error here is the error code passed in when the teardown function is called"""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__=='__main__':
    app.run()

