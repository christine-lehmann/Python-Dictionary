import json
from difflib import get_close_matches

data = json.load(open("data.json"))

print("\t==========================================")
print("\t=                                        =")
print("\t=   WELCOME TO ENGLISH WORD DICTIONARY   =")
print("\t=                                        =")
print("\t==========================================")
print("\n")


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0]+ "?")
        decide = input("Press Y for Yes or N for No: ").upper()
        if decide == "Y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "N":
            return("Oh no! Pugger your paw steps on wrong keys. ")
        else:
            return("Rubbish input mate! Please enter just Y or N: ")
    else:
        print("Oh no! Pugger your paw steps on wrong keys. ")



word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
