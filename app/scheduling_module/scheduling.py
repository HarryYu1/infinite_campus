from datetime import datetime
from . import find_lowest

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

schedulingbp = Blueprint('scheduling', __name__)

@schedulingbp.route('/initiateSOAR', methods = ["POST"])
def initiateSOAR():
  if request.method == 'POST':
    try:
      currentDate = request.form.get('currentdatepost') # Date for Current Date
      soarDate = request.form.get('soardatepost') # Date for SOAR Date 
    except:
      return redirect(url_for('auth.login'))

    #print("\n\n\n\n\nCurrent Date:", currentDate, "\t\t\tSOAR Date:", soarDate, "\n\n\n\n")

    #convert to datetime objects
    currentDate = datetime.strptime(currentDate,'%Y-%m-%d')
    soarDate = datetime.strptime(soarDate, '%Y-%m-%d')

    #Imports and runs find_lowest 

    find_lowest.write_to_database(currdate=currentDate, soardate=soarDate)

    return render_template('scheduling/finished.html')
    
  else:
    return redirect(url_for('auth.login'))

#error handler
@schedulingbp.errorhandler(500)
def function_name(error):
    return render_template('scheduling/error.html')
