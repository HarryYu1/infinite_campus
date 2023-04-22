import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

schedulingbp = Blueprint('scheduling', __name__)

@schedulingbp.route('/initiateSOAR')
def initiateSOAR():
  if request.method == 'POST':
    import main # Imports the main.py file. 
    return render_template('scheduling/index.html')
  else:
    return redirect(url_for('auth.login'))