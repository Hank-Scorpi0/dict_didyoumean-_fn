import json
from difflib import get_close_matches as gcm

word = input("Search a word: ")

data = json.load(open(r".\Dictionary\data.json"))

def dict_search(x):
    x = x.lower()
    if x in data:
        defin = data[x]
        t = 0
        
        for i in defin:
            t = t + 1
            print(str(t) + ". " + i)
        print("\n")

    elif len(gcm(x, data.keys())) > 0:
        
        cls_match = gcm(x, data.keys())
        first_term = cls_match[0]
        rec_srch = input("Did you mean {} instead? (Y/N) ".format(first_term))

        if rec_srch == "Y" or rec_srch == "y":
            print("\n" + first_term.title() + ":")
            correct_search(first_term)
        elif:
            print("The word you searched does not exist")
        else:
            print("Entry not recognized")
    else:
        print("WORD NOT FOUND")

def correct_search(y):
    dict_search(y)

dict_search(word)
