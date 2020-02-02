from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import cross_validate, LeaveOneOut, KFold
from sklearn.linear_model import LogisticRegression
from clean_text import get_tweet_tuples
import numpy as np
import sys


# Create a feature representation
def get_features(corpus, type, vocab):
    labels = []
    tweets = []
    for tweet in corpus:
        tweets.append(tweet[1])
        if type == 'train':
            labels.append(tweet[0])

    if type == 'train':
        vectorizer = TfidfVectorizer(token_pattern=r'\b\w\w+\b|(?<!\w)@\w+|(?<!\w)#\w+', stop_words='english')
        # vocab = list(filter(lambda word: re.match(".*[a-zA-Z].*", word) is not None, vectorizer.get_feature_names()))
        features = vectorizer.fit_transform(tweets)
        vocabulary = vectorizer.get_feature_names()
        features = vectorizer.fit_transform(tweets)
    if type == 'test':
        vectorizer = TfidfVectorizer(vocabulary=vocab)
        features = vectorizer.fit_transform(tweets)
    if type == 'train':
        return features, labels, vocabulary
    else:
        return features, vocab


# Construct the model and add the feature
def build_model(features, labels, vocabulary):
    print('Building the model')
    model = LogisticRegression(penalty="l2", solver="liblinear")

    results = cross_validate(model, features, labels, cv=KFold(n_splits=10, shuffle=True, random_state=1))
    scores = results["test_score"]
    avg_score = sum(scores) / len(scores)
    model.fit(features, labels)
    print("The model's average accuracy is %f" % avg_score)

    neg_class_prob_sorted = model.coef_[0, :].argsort()
    pos_class_prob_sorted = (-model.coef_[0, :]).argsort()

    termsToTake = 3
    pos_indicators = [vocabulary[i] for i in neg_class_prob_sorted[:termsToTake]]
    neg_indicators = [vocabulary[i] for i in pos_class_prob_sorted[:termsToTake]]

    print("The most informative terms for pos are: %s" % pos_indicators)
    print("The most informative terms for neg are: %s" % neg_indicators)

    return model

    print('tested')


def removeSpecialCharacters(word):
    return word


def predict(features, model, tweets, vocab):
    prediction = model.predict_proba(features)
    prediction_int = prediction[:, 1] >= 0.3  # if prediction is greater than or equal to 0.3 then 1(offensive) else 0
    prediction_int = prediction_int.astype(np.int)
    result = []
    finalTweets = []
    i = 0
    for p in prediction_int:
        if p == 1:
            result.append(tweets[i][2])
            smax = -sys.maxsize - 1
            index = 0
            j = 0
            for word in tweets[i][1].split():
                if word in vocab:
                    wordIndex = vocab.index(word)
                    si = model.coef_[0][wordIndex]
                    if si > smax:
                        smax = si
                        index = j
                j = j + 1
            finalTweets.append((tweets[i][2], tweets[i][1].split()[index]))
        i = i + 1

    return finalTweets


def main():
    train_data = get_tweet_tuples('train-tweets.csv')
    features, labels, vocab = get_features(train_data, 'train', '')
    model = build_model(features, labels, vocab)
    test_data = get_tweet_tuples('test-tweets.csv')
    features_test, vocab = get_features(test_data, 'test', vocab)
    results = predict(features_test, model, test_data, vocab)
    print(results)

if __name__== "__main__":
  main()
