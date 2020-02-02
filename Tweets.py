from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import cross_validate, LeaveOneOut, KFold
from sklearn.linear_model import LogisticRegression
from clean_text import get_tweet_tuples
import numpy as np

def get_basic_features(corpus):
    labels = []
    tweets = []
    for tweet in corpus:
        tweets.append(tweet[1])
        labels.append(tweet[0])
    return tweets, labels


def run(train_data, test_data):
    model = LogisticRegression(penalty="l2", solver="liblinear")
    train_tweets, labels = get_basic_features(train_data)
    vectorizer = TfidfVectorizer( token_pattern=r'\b\w\w+\b|(?<!\w)@\w+|(?<!\w)#\w+')
    features = vectorizer.fit_transform(train_tweets)
    vocabulary = vectorizer.get_feature_names()

    train_results = cross_validate(model, features, labels, cv=KFold(n_splits=10, shuffle=True, random_state=1))
    scores = train_results["test_score"]
    avg_score = sum(scores) / len(scores)
    model.fit(features, labels)
    print("The model's average accuracy is %f" % avg_score)

    neg_class_prob_sorted = model.coef_[0, :].argsort()
    pos_class_prob_sorted = (-model.coef_[0, :]).argsort()
    termsToTake = 10
    pos_indicators = [vocabulary[i] for i in neg_class_prob_sorted[:termsToTake]]
    neg_indicators = [vocabulary[i] for i in pos_class_prob_sorted[:termsToTake]]
    print("The most informative terms for pos are: %s" % pos_indicators)
    print("The most informative terms for neg are: %s" % neg_indicators)

    # predictions

    test_tweets, vocab = get_basic_features(test_data)
    vectorizer = TfidfVectorizer(stop_words='english', vocabulary = vocabulary)
    features = vectorizer.fit_transform(test_tweets)

    print(predict(features, model, test_data))


def predict(features, model, tweets):
    prediction = model.predict_proba(features)
    prediction_int = prediction[:, 1] >= 0.3  # if prediction is greater than or equal to 0.3 than 1 else 0
    prediction_int = prediction_int.astype(np.int)
    result = []
    i = 0
    for p in prediction_int:
        if p == 1:
            result.append(tweets[i][2])
        i = i + 1

    return result


train_data = get_tweet_tuples('train-tweets.csv')
test_data = get_tweet_tuples('test-tweets.csv')
run(train_data, test_data)
