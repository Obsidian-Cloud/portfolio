# routes.py
from flask import Blueprint
from flask import request
from flask import redirect, render_template

from zope.component import getUtility

from components.Interfaces.interfaces import IComposer
from components.Interactor import request as _req

std_routes_bp = Blueprint('std_routes', __name__)

# Routes for portfolio selection on index ('/')
portfolio = ["movie-search", "ormlabs", "github"]


@std_routes_bp.route("/")
def index():
    return render_template("index.html", portfolio=portfolio)


@std_routes_bp.route("/movie-search/")
def moviesearch():

    return render_template("movie_search.html")


@std_routes_bp.route("/ormlabs/")
def ormlabs():
    #implementation = getUtility(IComposer)
    #implementation.execute_composer(category)
    return render_template("ormlabs.html")


@std_routes_bp.route("/github")
def githubviewer():

    return render_template("github.html")


@std_routes_bp.route("/contact-me")
def contactme():

    return render_template("contact_me.html")


@std_routes_bp.route("/review-console")
def reviewboard():
    
    return render_template("review_board.html")


# API Calls

#@app.route("/")

