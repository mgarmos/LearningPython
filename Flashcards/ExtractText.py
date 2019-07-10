import re
import json
from difflib import get_close_matches
import numbers


def getListWords(filename):
    myList = []
    
    #Extract all the words in a file
    with open(filename, 'r', encoding="utf8") as file:  # Use file to refer to the file object
        lineList = [line.rstrip('\n') for line in file]
        for line in lineList:
            #words = re.findall(r'\w+', line)
            words = re.findall(r'\w+', line)
            #re.split("\s", str)
            for word in words:
                myList.append(word)

    #Remove duplicates           
    myList = list(dict.fromkeys(myList))            

    #Order the list
    myList.sort()
    
    return myList

def getMeaning(word, data):
    word=word.lower()

    
    if word in data:
        return word, data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        return get_close_matches(word,data.keys())[0], data[get_close_matches(word,data.keys())[0]]


        
#Load dictionary
data= json.load(open("data.json"))

for word in getListWords( 'text1.txt'):
    if not re.search('\d+', word):
        # no numbers
        print("%s: %s"% (getMeaning(word, data)))

        


