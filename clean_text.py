#reference for pruning steps: https://www.analyticsvidhya.com/blog/2018/07/hands-on-sentiment-analysis-dataset-python/
import pandas as pd
import numpy as np
import warnings
from nltk.stem.porter import *

warnings.filterwarnings("ignore", category=DeprecationWarning)


def get_tweet_tuples(csv_path: str) -> tuple:

    # combine train and test sets to clean
    combi = pd.read_csv(csv_path)

    # remove unwanted text pattern from tweet
    def remove_pattern(input_txt, pattern):
        r = re.findall(pattern, input_txt)
        for i in r:
            input_txt = re.sub(i, '', input_txt)

        return input_txt

    # remove twitter handles (@user)
    combi['tidy_tweet'] = np.vectorize(remove_pattern)(combi['tweet'], "@[\w]*")

    # remove special characters, numbers, punctuations
    combi['tidy_tweet'] = combi['tidy_tweet'].str.replace("[^a-zA-Z#]", " ")

    # remove words < 3 letters long
    combi['tidy_tweet'] = combi['tidy_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))

    # tokenize remaining text in each tweets
    tokenized_tweet = combi['tidy_tweet'].apply(lambda x: x.split())
    tokenized_tweet.head()

    # stemming (strip suffixes)
    # stemmer = PorterStemmer()

    # tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x])
    # tokenized_tweet.head()

    # combine back together
    for i in range(len(tokenized_tweet)):
        tokenized_tweet[i] = ' '.join(tokenized_tweet[i])

    combi['tidy_tweet'] = tokenized_tweet

    tweet_tuples = []
    if 'label' in combi:
        for i in range(len(combi)):
            tweet_tuples.append((int(combi.loc[i, "label"]), combi.loc[i, "tidy_tweet"], combi.loc[i, 'tweet']))
    else:
        for i in range(len(combi)):
            tweet_tuples.append(('dummy', combi.loc[i, "tidy_tweet"], combi.loc[i,'tweet']))

    return tweet_tuples