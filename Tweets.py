from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import cross_validate, LeaveOneOut, KFold
from sklearn.linear_model import LogisticRegression
from clean_text import get_tweet_tuples


# Create a feature representation
def get_features(corpus, type):
    labels = []
    tweets = []
    for tweet in corpus:
        tweets.append(tweet[1])
        if type == 'train':
            labels.append(tweet[0])

    vectorizer = TfidfVectorizer(stop_words='english')
    features = vectorizer.fit_transform(tweets)
    vocab = vectorizer.get_feature_names()
    if type == 'train':
        return features, labels, vocab
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


train_data = get_tweet_tuples('train-tweets.csv')
features, labels, vocab = get_features(train_data, 'train')
model = build_model(features, labels, vocab)
test_data = get_tweet_tuples('test-tweets.csv')
features, vocab = get_features(test_data, 'test')

print('Done')
