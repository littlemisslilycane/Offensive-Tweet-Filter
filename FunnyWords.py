import random
import csv

funny = [    'aardvark', 'abacus', 'abundance', 'ache', 'acupuncture',
    'airbrush', 'alien', 'anagram', 'angle', 'amazing', 'ankle',
    'alphabet', 'antenna', 'aqua', 'asphalt', 'bacon', 'banana',
    'bangles', 'banjo', 'bankrupt', 'bar', 'barracuda', 'basket',
    'beluga', 'binder', 'birthday', 'bisect', 'blizzard', 'blunderbuss',
    'boa', 'bog', 'bounce', 'broomstick', 'brought', 'bubble',
    'budgie', 'bug', 'bug-a-boo', 'bugger', 'buff', 'burst', 'butter',
    'buzz', 'cabana', 'cake', 'calculator', 'camera', 'candle',
    'carnival', 'carpet', 'casino', 'cashew', 'catfish', 'ceiling',
    'celery', 'chalet', 'chalk', 'chart', 'cheddar', 'chesterfield',
    'chicken', 'chinchill', 'chit-chat', 'chocolate', 'chowder', 'coal',
    'compass', 'compress', 'computer', 'conduct', 'contents', 'cookie',
    'copper', 'corduroy', 'cow', 'cracker', 'crackle', 'croissant',
    'cube', 'cupcake', 'curly', 'curtain', 'cushion', 'cuticle',
    'daffodil', 'delicious', 'dictionary', 'dimple', 'ding-a-ling',
    'disk', 'disco duck', 'dodo', 'dolphin', 'donuts', 'dork',
    'dracula', 'duct tape', 'effigy', 'egad', 'elastic', 'elephant',
    'encasement', 'erosion', 'eyelash', 'fabulous', 'fantastic',
    'feather', 'felafel', 'fetish', 'financial', 'finger', 'finite',
    'fish', 'fizzle', 'fizzy', 'flame', 'flash', 'flavour', 'flick',
    'flock', 'flour', 'flower', 'foamy', 'foot', 'fork', 'fritter',
    'fudge', 'fungus', 'funny', 'fuse', 'fusion', 'fuzzy', 'garlic',
    'gelatin', 'gelato', 'glebe', 'glitter', 'glossy',
    'groceries', 'goulashes', 'guacamole', 'gumdrop', 'haberdashery',
    'hamster', 'happy', 'highlight', 'hippopotamus', 'hobbit', 'hold',
    'hooligan', 'hydrant', 'icicles', 'implode', 'implosion',
    'indeed', 'issue', 'itchy', 'jell-o', 'jewel', 'jump', 'kabob',
    'kasai', 'kite', 'kiwi', 'ketchup', 'knob', 'laces', 'lacy',
    'laughter', 'laundry', 'leaflet', 'legacy', 'leprechaun', 'lollypop',
    'lumberjack', 'macadamia', 'magenta', 'magic', 'magnanimous',
    'mango', 'margarine', 'massimo', 'mechanical', 'medicine', 'meh',
    'melon', 'meow', 'mesh', 'metric', 'microphone', 'minnow', 'mitten',
    'mozzarella', 'muck', 'mumble', 'mushy', 'mustache', 'nanimo',
    'noodle', 'nostril', 'nuggets', 'oatmeal', 'oboe', 'o\'clock',
    'octopus', 'odour', 'ointment', 'olive', 'optic', 'overhead', 'ox',
    'oxen', 'pajamas', 'pancake', 'pansy', 'paper', 'paprika',
    'parmesan', 'pasta', 'pattern', 'pecan', 'peek-a-boo', 'pen',
    'pepper', 'pepperoni', 'peppermint', 'perfume', 'periwinkle',
    'photograph', 'pie', 'pierce', 'pillow', 'pimple', 'pineapple',
    'pistachio', 'plush', 'polish', 'pompom', 'poodle', 'pop',
    'popsicle', 'prism', 'prospector', 'prosper', 'pudding', 'puppet',
    'puzzle', 'query', 'radish', 'rainbow', 'ribbon', 'rotate',
    'salami', 'sandwich', 'saturday', 'saturn', 'saxophone', 'scissors',
    'scooter', 'scrabbleship', 'scrunchie', 'scuffle', 'shadow',
    'sickish', 'silicone', 'slippery', 'smash', 'smooch', 'snap',
    'snooker', 'socks', 'soya', 'spaghett', 'sparkle', 'spatula',
    'spiral', 'splurge', 'spoon', 'sprinkle', 'square', 'squiggle',
    'squirrel', 'statistics', 'stuffing', 'sticky', 'sugar',
    'sunshine', 'super', 'swirl', 'taffy', 'tangy', 'tape', 'tat',
    'teepee', 'telephone', 'television', 'thinkable', 'tip', 'tof',
    'toga', 'trestle', 'tulip', 'turnip', 'turtle', 'tusks',
    'ultimate', 'unicycle', 'unique', 'uranus', 'vegetable', 'waddle',
    'waffle', 'wallet', 'walnut', 'wagon', 'window', 'whatever',
    'whimsical', 'wobbly', 'yellow', 'zap', 'zebra', 'zigzag', 'zip',
    ]

# for i in range(100):
#     print(' '.join(random.sample(funny, random.randint(2, 2))))

# String that you want to search
foul = 'cheap'
foul_replace = (' '.join(random.sample(funny, random.randint(2, 2))))
print(foul_replace)
with open("dummy-foul.csv") as f_obj:
    data = f_obj.read()
    print(data)
    # reader = csv.reader(f_obj, delimiter=',')
    # Iterates through the rows of your csv
    for row in data:
        # print(row)
        # If the string you want to search is in the row
        # for word in row:
        if foul in data:
            # print(row)
            # data = f_obj.read()
            data = data.replace(foul, foul_replace)
            print("String found!")
            # print(row)
            print(data)



