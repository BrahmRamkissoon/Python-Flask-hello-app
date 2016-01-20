import os


from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return url_for('show_user_profile', username='david')
    
@app.route('/username/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return "User %s" % username
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the ide must be an integer
    return "Post %d" % post_id

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)