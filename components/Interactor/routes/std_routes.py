# routes.py
import uuid

from zope.component import getUtility

from flask import Blueprint
from flask import session
from flask import render_template

from components.Interfaces.interfaces import IComposer


std_routes_bp = Blueprint('std_routes', __name__)

@std_routes_bp.route("/")
def index():

    return render_template("index.html")


@std_routes_bp.route("/movie-search/")
def moviesearch():

    return render_template("movie_search.html")

# When a user directs to '/ormlabs/', they are given a 'uuid4' and their
# session is set to permanent so the `app.config[]` can set the actual timeout.
# Otherwise, if 'False', the session(cookies) would clear on browser closing.
# 'UUID4' is used to determine who owns what data in the multi-tenancy 
# database schema.
@std_routes_bp.route("/ormlabs/")
def ormlabs():
    if 'user_cookie' not in session:
        session['user_cookie'] = str(uuid.uuid4())
        session.permanent = True
    
    implementation = getUtility(IComposer)
    rows = implementation.execute_composer(query=True, cookie_val=session['user_cookie'])
    return render_template("ormlabs.html", rows=rows)

@std_routes_bp.route("/github/")
def githubviewer():

    return render_template("github.html")

@std_routes_bp.route("/contact-me/")
def contactme():

    return render_template("contact_me.html")

@std_routes_bp.route("/portfolio-diagram/")
def portfolio_diagram():
    
    return render_template("portfolio_diagram.html")
