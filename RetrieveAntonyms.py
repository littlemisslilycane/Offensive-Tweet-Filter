import nltk
from nltk.corpus import wordnet

def retrieve_antonym(word):
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():
                return l.antonyms()[0].name()
    return ""

# import json
# import requests
#
#
# def get_antonym(word):
#     # headers = {
#     #     'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
#     #     'x-rapidapi-key': "e29d201fc4msh561c08a33b21199p180f2ejsnd87867afb9df"
#     # }
#     url = "https://wordsapiv1.p.mashape.com/words/" + word + "/antonyms"
#     response = requests.get(url=url, params=None, headers = {
#         'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
#         'x-rapidapi-key': "e29d201fc4msh561c08a33b21199p180f2ejsnd87867afb9df"
#     })
#     json_data = json.loads(response.text)
#     antonym = []
#     antonym = json_data["antonyms"]
#     return antonym[0]
#
# print(get_antonym("regretful"))