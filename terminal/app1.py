import json
from difflib import get_close_matches

print("===============================")
print("==== DICTIONARY Version 1.2 ===")

data = json.load(open("../data.json"))

def translate(word):
    word = word.lower()
    wordCap = word.title()
    wordUpper = word.upper()
    if word in data:
        print(wordCap)
        return data[word]
    elif wordCap in data:
        print(wordCap)
        return data[wordCap]
    elif wordUpper in data:
        print(wordUpper)
        return data[wordUpper]
    elif len(get_close_matches(word, data.keys())) > 0:
        closest_word = get_close_matches(word, data.keys())[0]
        asking = input(f"Did you mean { closest_word.title() } instead ? (y/n) ")
        if asking.lower() == "y":
            print(closest_word.title())
            return data[closest_word]
        elif asking.lower() == "n":
            return f"Opps, {word} is not EXISTS. Please Double Check it"
        else:
            return f"Opps, Sorry we didn't understand your entry"
    else:
        return f"Opps, {word} is not EXISTS. Please Double Check it"

while True:
    print("=============================== \n")
    word = input("Enter Word : ")
    if word != "\e":
        findword = translate(word)
        if type(findword) == list:
            for item in findword:
                print(f" - {item}")
        else: 
            print(findword)
    else:
        exit()

