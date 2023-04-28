import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

schedulingbp = Blueprint('scheduling', __name__)

@schedulingbp.route('/initiateSOAR', methods = ["POST"])
def initiateSOAR():
  if request.method == 'POST':
    from . import find_lowest # Imports find_lowest
    return render_template('scheduling/index.html')
  else:
    return redirect(url_for('auth.login'))
