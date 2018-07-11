import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input('Did you mean " %s " instead? Enter "Y" if Yes, or "N" if No: ' % (get_close_matches(w, data.keys(), n=4, cutoff=0.8))[0])
        if yn == 'Y':
            return data[(get_close_matches(w, data.keys(), n=4, cutoff=0.8))[0]]
        elif yn == 'N':
            return "This word doesn't exit. Please check..."
        else:
            return "We didn't understand your input!!!"
    else:
        return "This word doesn't exit. Please check..."

word = input('Enter word ')

ShowDefination = (translate(word))
if type(ShowDefination) == list:
    for item in ShowDefination:
        print(item)
else:
    print(ShowDefination)