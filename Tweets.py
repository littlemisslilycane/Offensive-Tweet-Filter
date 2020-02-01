from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import requests
import json
from sklearn.model_selection import cross_validate, LeaveOneOut

from sklearn.linear_model import LogisticRegression

# Create a feature representation

# Create the model and add the feature

TWEETS = ['You are ugly', 'Hey beautiful']


def get_corpus():
    raw = requests.get(
        "").text.strip()
    corpus = [json.loads(line) for line in raw.split("\n")]


    corpus = [entry for entry in corpus if entry["genre"] != "history"]
    return corpus


def get_features(corpus):
    labels = []
    tweets = []
    for tweet in corpus:
        tweets.append(tweet['text'])
        labels.append(tweet['genre'])
    vectorizer = CountVectorizer(stop_words='english')
    features = vectorizer.fit_transform(tweets)
    vocab = vectorizer.get_feature_names()
    return features, labels, vocab


def build_model(features, labels, vocabulary):
    print('Building the model')
    # Penalty can be L1 or L2; L1 makes the less important features shrink to zero.
    model = LogisticRegression(penalty="l2")
    results = cross_validate(model, features, labels, cv=LeaveOneOut())
    scores = results["test_score"]
    avg_score = sum(scores) / len(scores)
    model.fit(features, labels)
    print("The model's average accuracy is %f" % avg_score)


corpus = get_corpus()
features, labels, vocab = get_features(corpus)
build_model(features, labels, vocab)
