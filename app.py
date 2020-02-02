# app.py
from flask import Flask, request, render_template, jsonify  # import main Flask class and request object
from Tweets import get_text_features
from RetrieveAntonyms import retrieve_antonym
from MoreFunny import more_funny

app = Flask(__name__, template_folder='./templates')  # create the Flask app


@app.route('/')
def my_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    # text = request.form['text']
    text = request.args.get("tweet")
    if "yhgsd568isugfus76sdfgjs767utyyjfv" in text:
        text = text.replace("yhgsd568isugfus76sdfgjs767utyyjfv","#")
    action = request.args.get("action")
    # action = "Funny"
    # text = "these  comments from the failed republican candidate for governor of new york in 2010, #carlpaladino. "

    offensive_words = get_text_features(text)
    if offensive_words:
        if action == 'Funny':
            text = more_funny((text, offensive_words))
        elif action == 'Opposite':
            text = retrieve_antonym(text, offensive_words)
        else:
            return jsonify({'error': "Invalid request"})
    if "#" in text:
        text = text.replace("#","yhgsd568isugfus76sdfgjs767utyyjfv")
    json_resp = {'tweet': text}
    return jsonify(json_resp)


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
# my_form_post()
