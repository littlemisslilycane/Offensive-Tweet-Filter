from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import cross_validate, LeaveOneOut, KFold
from sklearn.linear_model import LogisticRegression
from clean_text import get_tweet_tuples
import  numpy as np

# Create a feature representation
def get_features(corpus, type, vocab):
    labels = []
    tweets = []
    for tweet in corpus:
        tweets.append(tweet[1])
        if type == 'train':
            labels.append(tweet[0])

    if type == 'train':
        vectorizer = TfidfVectorizer(stop_words='english')
        features = vectorizer.fit_transform(tweets)
        vocabulary = vectorizer.get_feature_names()
        features = vectorizer.fit_transform(tweets)
    if type == 'test':
        vectorizer = TfidfVectorizer(stop_words='english', vocabulary=vocab)
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


def predict(features, model):

    prediction = model.predict_proba(features)
    prediction_int = prediction[:, 1] >= 0.3  # if prediction is greater than or equal to 0.3 than 1 else 0
    prediction_int = prediction_int.astype(np.int)

    print('prediction done')



vocab = []
train_data = get_tweet_tuples('train-tweets.csv')
features, labels, vocab = get_features(train_data, 'train','')
model = build_model(features, labels, vocab)
test_data = get_tweet_tuples('test-tweets.csv')
features_test, vocab = get_features(test_data, 'test', vocab)
predict(features_test, model)
print('Done')
