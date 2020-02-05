import nltk
from nltk.corpus import wordnet

def retrieve_antonym(tweet, words):
    for word in words:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.antonyms():
                    tweet = tweet.replace(word, l.antonyms()[0].name())
                else:
                    tweet = tweet.replace(word, "")
    return tweet