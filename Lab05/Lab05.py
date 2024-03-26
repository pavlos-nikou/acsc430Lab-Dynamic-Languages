from string import punctuation as punc
from htmlFunctions import *

# lab5
# prepared by:
    # pavlos nikou
    # 26276
    # 23/3/2024

def top_words(countWords,topWordCount):
    sortedCountWordsList = sorted(countWords.items(), key=lambda x:x[1])# Sort the word counts
    return dict(sortedCountWordsList[-(topWordCount+1):]) # return top 40 words

def count_words(splitText):
    wordCounter = {}# Initialize an empty dictionary to store word counts
    for word in splitText:
        if word in wordCounter:
            wordCounter[word] = wordCounter[word]+1# Increment word count if word is already in dictionary
        else:
            wordCounter[word] = 1 # Add new word to dictionary with count 1 if its not in the dictionary already
    return wordCounter

def remove_punctuation(word):
    for ch in word:
        if ch in punc:
            word = word.replace(ch, "") # Replace punctuation characters with an empty string
    return word

def get_speakers_words(text, ignoreWords):
    text = text.split()# Split text into words
    speakerListIndex = {"OBAMA:":"obama","ROMNEY:":"romney","LEHRER:":"junk", "CROWLEY:": "junk", "QUESTION:":"junk"}
    speakerWords = {"obama":[], "romney":[], "junk":[]}# Initialize dictionary to store words spoken by each speaker
    listIndex = None
    for word in text:
        if word in speakerListIndex:# Set the current speaker based on the word encountered
            listIndex = speakerListIndex[word]
        else :
            word = remove_punctuation(word).lower()# Remove punctuation and convert word to lowercase
            if word not in ignoreWords:
                speakerWords[listIndex].append(word)# Add word to speaker's word list if not in ignoreWords
    return speakerWords

# Main Code
print("Enter the name of the filename to be processed:")
doc = input()

f = open(doc+".txt", "r")
text = f.read() # Read text from file
f.close()
f = open("stopwords.txt", "r")
stopWords = f.read().split("\n")# Read stopwords from file and split by newline
f.close()

speakerWords = get_speakers_words(text, stopWords)# Get words spoken by each speaker
top40wordCount = {"obama":top_words(count_words(speakerWords["obama"]),40), "romney":top_words(count_words(speakerWords["romney"]),40)}

# Calculate max and min word counts for each speaker
obamaMax = max(top40wordCount["obama"].values())
obamaMin = min(top40wordCount["obama"].values())
romneyMax = max(top40wordCount["romney"].values())
romneyMin = min(top40wordCount["romney"].values())

# Generate HTML for Obama's top words
body = ""
obamaWords = dict(sorted(top40wordCount["obama"].items()))#order obamas words alphabetically
for word in obamaWords:
    body = body + makeHTMLword(word, obamaWords[word], obamaMax, obamaMin)
box = makeHTMLbox(body)
printHTMLfile(box, "obama")

# Generate HTML for Romney's top words
body = ""
romneyWords = dict(sorted(top40wordCount["romney"].items())) #order romneys words alphabetically

for word in romneyWords:
    body = body + makeHTMLword(word, romneyWords[word], romneyMax, romneyMin)
box = makeHTMLbox(body)
printHTMLfile(box, "romney")

