import json
import random
from difflib import get_close_matches
data= json.load(open("data.json"))
def dictionary(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        response=input("Did you mean %s instead? If yes enter Y else N for no: "% get_close_matches(word,data.keys())[0])
        if response =='Y' or response =='y':
            return data[get_close_matches(word,data.keys())[0]]
        elif response == 'N'or response == 'n':
            return "Word does not exist, plz double check it"
        else:
            return "We did not get you"
    else:
        return ("Word does not exist. Please double check it! ")

def randomWord():
    word = random.choice(list(data.keys()))
    print(word)
    return word


def main():
    while True:
        #word=input("Search your word: ")
        #result=dictionary(word)
        result=dictionary(randomWord())
        
        if type(result) == list:
            for item in result:
                print(item)
        else:
            print(result)
        demand=input("To close type 'Y' else 'N': ")
        if demand == 'Y' or demand =='y':
            print("Hope you visit again")
            break
    
if __name__== "__main__":
    main()