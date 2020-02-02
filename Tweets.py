from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import cross_validate, LeaveOneOut, KFold
from sklearn.linear_model import LogisticRegression
from clean_text import get_tweet_tuples
import numpy as np
import sys


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
    vectorizer = TfidfVectorizer(token_pattern=r'\b\w\w+\b|(?<!\w)@\w+|(?<!\w)#\w+',
                                 stop_words='english')
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
    vectorizer = TfidfVectorizer(stop_words='english', vocabulary=vocabulary)
    features = vectorizer.fit_transform(test_tweets)

    final_results = predict(features, model, test_data, vocabulary)
    return final_results


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
    test_data = get_tweet_tuples('test-tweets.csv')
    return run(train_data, test_data)


if __name__ == "__main__":
    print(main())
