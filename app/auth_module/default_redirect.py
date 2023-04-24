import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

#set up a route for default redirect
default_redirect_bp = Blueprint('default_redirect', __name__)

@default_redirect_bp.route('/')
def redirect_login():
    return redirect(url_for('auth.login'))