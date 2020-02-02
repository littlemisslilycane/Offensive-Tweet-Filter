# tuple1 = (
#     'these dumb comments from the failed republican candidate for governor of new york in 2010, #carlpaladino #dumb.', 'dumb','failed')

import random
import re

funny = ['aardvark', 'abacus', 'abundance', 'ache', 'acupuncture',
         'airbrush', 'alien', 'anagram', 'angle', 'amazing', 'ankle',
         'alphabet', 'antenna', 'aqua', 'asphalt', 'bacon', 'banana',
         'bangles', 'banjo', 'bankrupt', 'bar', 'barracuda', 'basket',
         'beluga', 'binder', 'birthday', 'bisect', 'blizzard', 'googly', 'happy',
         'boa', 'bog', 'bounce', 'broomstick', 'brought', 'bubble', 'dance',
         'blast', 'bug', 'bug-a-boo', 'bugger', 'buff', 'burst', 'butter',
         'buzz', 'cabana', 'cake', 'cackle', 'calculator', 'camera', 'candle',
         'carnival', 'carpet', 'casino', 'cashew', 'caterpillar', 'catfish', 'ceiling',
         'celery', 'chalet', 'chalk', 'chart', 'cheddar', 'chesterfield',
         'chicken', 'chinchilla', 'chit-chat', 'chocolate', 'chowder', 'coal',
         'compass', 'compress', 'computer', 'conduct', 'contents', 'cookie',
         'copper', 'corduroy', 'cow', 'cracker', 'crackle', 'croissant',
         'cube', 'cupcake', 'curly', 'curtain', 'cushion', 'cuticle',
         'daffodil', 'delicious', 'dictionary', 'dimple',
         'disk', 'disco duck', 'dodo', 'dolphin', 'donuts',
         'dracula', 'duct tape', 'effigy', 'egad', 'elastic', 'elephant',
         'encasement', 'erosion', 'eyelash', 'fabulous', 'fantastic',
         'feather', 'falafel', 'flick', 'frazzle', 'finger', 'finite',
         'fish', 'fizzle', 'fizzy', 'flame', 'flash', 'flavor', 'flick',
         'flock', 'flour', 'flower', 'foamy', 'foot', 'fork', 'fritter',
         'fudge', 'fungus', 'funny', 'fuse', 'fusion', 'fuzzy', 'garlic',
         'gelato', 'globe', 'glitter', 'glossy', 'giggle', 'fluffy'
         'groceries', 'goulashes', 'guacamole', 'gumdrop', 'haberdashery',
         'hamster', 'happy', 'highlight', 'hippopotamus', 'hobbit', 'hold',
         'hoop', 'hooplah', 'hydrant', 'icicles', 'implode', 'implosion',
         'indeed', 'issue', 'itchy', 'jazzy', 'jello', 'jewel', 'jump', 'kabob',
         'kasai', 'kite', 'kiwi', 'ketchup', 'knob', 'laces', 'lacy',
         'laughter', 'laundry', 'leaflet', 'legacy', 'leprechaun', 'lollipop',
         'lumberjack', 'macadamia', 'magenta', 'magic', 'magnanimous',
         'mango', 'margarine', 'massimo', 'mechanical', 'medicine', 'meh',
         'melon', 'meow', 'mesh', 'mogul', 'microphone', 'minnow', 'mitten',
         'mozzarella', 'moo', 'malarkey', 'mumble', 'mustache',
         'noodle', 'nostril', 'nuggets', 'oatmeal', 'oboe', 'o\'clock',
         'octopus', 'ointment', 'olive', 'optic', 'overhead', 'ox',
         'oxen', 'pajamas', 'pancake', 'paper', 'paprika',
         'parmesan', 'pasta', 'pattern', 'pecan', 'peek-a-boo', 'pen',
         'pepper', 'pepperoni', 'peppermint', 'perfume', 'periwinkle',
         'photograph', 'pie', 'pierce', 'pillow', 'pineapple',
         'pistachio', 'plush', 'polish', 'pompom', 'poodle', 'pop',
         'popsicle', 'prism', 'prospector', 'prosper', 'pudding', 'puppet',
         'puzzle', 'query', 'radish', 'rainbow', 'ribbon', 'rotate',
         'salami', 'sandwich', 'saturday', 'saturn', 'saxophone', 'scissors',
         'scooter', 'scrabbleship', 'scrunchy', 'scuffle', 'shadow',
         'sickish', 'silicone', 'slippery', 'smash', 'smooch', 'snap',
         'snooker', 'socks', 'soy', 'spaghett', 'spaghetti', 'sparkle', 'spatula',
         'spiral', 'splurge', 'spoon', 'sprinkle', 'square', 'squiggle',
         'squirrel', 'statistics', 'stuffing', 'sticky', 'sparkly', 'sparkle', 'sugar',
         'sunshine', 'super', 'swirl', 'taffy', 'tangy', 'tape', 'tat',
         'telephone', 'television', 'thinkable', 'tip', 'tuft', 'fractal',
         'gopher', 'glob', 'garble', 'jingle', 'blarg', 'bubbly',
         'toga', 'trestle', 'tulip', 'turnip', 'turtle', 'tusks',
         'ultimate', 'unicycle', 'unique', 'uranus', 'vegetable', 'waddle',
         'waffle', 'wallet', 'walnut', 'wagon', 'window', 'whatever',
         'whimsical', 'winky', 'wobbly', 'yellow', 'zap', 'zebra', 'zigzag', 'zip',
         ]
def more_funny(tuple1: tuple) -> str:
    data = tuple1[0]
    for i in range(len(tuple1) - 1):
        foul = tuple1[i+1]
        foul_replace = (' '.join(random.sample(funny, random.randint(2, 2))))
    if foul in data:
        foul_replace_hashtag = '#' + foul_replace.replace(" ", '_')
        data = re.sub('#{0}'.format(foul), foul_replace_hashtag, data)
        data = data.replace(foul, foul_replace)
    return data
