import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

authbp = Blueprint('auth', __name__, url_prefix='/auth')

@authbp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = 1

@authbp.route('/login', methods = ["POST", "GET"])
def login():
  return render_template('auth/form.html')
  
@authbp.route('/handle_post', methods = ["POST"])
def handle_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("Returned Username: " + username, "\t\t\tReturned Password: " + password)
        if username == "administrator" and password == "N@perv1ll3Centr4l": # HARDCODED PASSWORD! WARNING!!!!!!!!! >:(
            return render_template('scheduling/index.html')
          
        else:
            return render_template('auth/incorrect.html')
    else:
        return render_template('auth/form.html')
    
@authbp.route('/logout')
def logout():
    session.clear()
    g.users = None
    print('redirected from logout')
    return redirect(url_for('auth.login'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            print('redirected from login_required')
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
