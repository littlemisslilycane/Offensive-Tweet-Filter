#app.py
from clean_text import get_tweet_tuple
from flask import Flask, request, render_template  # import main Flask class and request object

app = Flask(__name__, template_folder='./templates') #create the Flask app

@app.route('/')
def my_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return text
    #return get_tweet_tuple(text)

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()