import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

schedulingbp = Blueprint('scheduling', __name__)

@schedulingbp.route('/initiateSOAR', methods = ["POST"])
def initiateSOAR():
  if request.method == 'POST':
<<<<<<< Updated upstream
    import main # Imports the main.py file. 
    return render_template('scheduling/loading.html')
=======
    from . import find_lowest # Imports find_lowest
    return render_template('scheduling/index.html')
>>>>>>> Stashed changes
  else:
    return redirect(url_for('auth.login'))
