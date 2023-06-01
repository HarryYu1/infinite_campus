import functools
from datetime import datetime

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

schedulingbp = Blueprint('scheduling', __name__)

@schedulingbp.route('/initiateSOAR', methods = ["POST"])
def initiateSOAR():
  if request.method == 'POST':
    currentDate = request.form.get('currentdatepost')
    soarDate = request.form.get('soardatepost')

    print("\n\n\n\n\nCurrent Date:", currentDate, "\t\t\tSOAR Date:", soarDate, "\n\n\n\n")

    from . import find_lowest # Imports and runs find_lowest 

    return render_template('scheduling/finished.html')
    
  else:
    return redirect(url_for('auth.login'))

