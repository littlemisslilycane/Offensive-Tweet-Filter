#app.py
from flask import Flask, request, render_template  # import main Flask class and request object
from Tweets import get_text_features

app = Flask(__name__, template_folder='./templates') #create the Flask app

@app.route('/')
def my_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    if request.form['submit'] == 'Funny':
        return get_text_features(text)
    elif request.form['submit'] == 'Opposite':
        return ''
    else:
        return 'Invalid Request'

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()