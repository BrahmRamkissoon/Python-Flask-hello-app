import os

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # user has pressed submit button
    if request.method == 'POST': 
        if valid_login(request.form['username'], request.form['password']):
            return "Welcome back, %s" % request.form['username']
        else:
            error = 'Incorrect username and password'
    return render_template('login.html', error=error)
    
# check valid login    
def valid_login(username, password):
    if username == password:
        return True
    else:
        return False
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)