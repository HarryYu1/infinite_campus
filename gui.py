from flask import Flask, render_template, Response, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def view_form():
  return render_template('form.html')
  
@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username == "123" and password == "123": # HARDCODED PASSWORD! WARNING!!!!!!!!! >:(
            return render_template('index.html')
          
        else:
            return render_template('incorrect.html')
    else:
        return render_template('login.html')

@app.route('/initiateSOAR', methods=['POST'])
def initiateSOAR():
  import main # Imports the main.py file. 
  return render_template('index.html')

app.run(host='0.0.0.0', port=81)

