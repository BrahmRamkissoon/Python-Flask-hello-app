import os


from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"
    
@app.route('/user/<username>')
def show_user_profile(username):
    visits = 3
    # show the user profile for that user
    return "User %s visited %d times ( 3 just a sample here)" % (username, visits)
    
@app.route('/hello')
def hello_world():
    return "Hello World"
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show th epost with the given id, the ide must be an integer
    return "Post %d" % post_id

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)