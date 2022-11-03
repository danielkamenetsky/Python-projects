"""
Student name: Daniel Kamenetsky
Student #: 20248702
Date: July 10, 2020

This program calculates the EPA values of words in a given txt file (user can replace
"PoliticalSpeech.txt" with any txt file) calling readFile(filename), getWords(speech),
prepareSemanticDifferential(), and findPOS(word) to  determine whether the words are
adjectives or adverbs. If this is the case, the program runs through a file called
OsgoodOriginals, and calculates the sum total of EPA values for all adverbs or
adjectives in the txt file that are also included in OsgoodOriginals. Using the
functions countAdjectives(), countAdverbs(), getUniqueWords() and countWords(),
the program returns the number of adjectives, adverbs, unique words, and count of
each unique word in a given txt file.

"""

import nltk
nltk.download('brown')
nltk.download('universal_tagset')

"""
Importing the necessary NLTK libraries and modules.
"""
from nltk.tag import StanfordPOSTagger
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize
from nltk.corpus import words
from nltk.tokenize import word_tokenize



"""
To identify the part-of-speech of the words retrieved from
Word2vec, we used the conditional frequency feature of the NLTK module
which returns a frequency-ordered list of the possible parts of speech associated
with all of the English words that are found in the Brown Corpus. Our sys-
tem uses the Brown Corpus to generate the frequency-ordered list because
of the fact that the words contained in the Brown Corpus are annotated with
part-of-speech tags.
"""

wordtags = nltk.ConditionalFreqDist((w.lower(), t) 
        for w, t in nltk.corpus.brown.tagged_words(tagset="universal"))

"""
This function uses wordtags inside of a list to determine whether the word 
(which is the input parameter for this functon) is an adjective, adverb or 
noun, and then returns the respective part of speech that the word is to the user.
"""
def findPOS(word):
    lisPOS = list(wordtags[word])

    #checking and returning whether ADJ, ADV, or NN
    if "ADJ" in lisPOS:
        return "ADJECTIVE"
    if "ADV" in lisPOS:
        return "ADVERB"
    if "NN" in lisPOS:
        return "NOUN"
    
"""
This function takes an input parameter for a file name (determined by the user),
opens that file, reads the contents of the file, assigns it to a variable, and
then closes the file. Finally it returns the variable entailing the file.
"""
def readFile(filename):
    speechFile = open(filename, "r")

    #reading in each line of the file
    speech = speechFile.read()

    speechFile.close()
    return speech

"""
This function has one input parameter that is the variable "speech" which entails
the contents of a file called by the user. For the output, the function then splits 
the string into a list
"""
def getWords(speech):
    return speech.split()

"""
This function has no input parameters. This function reads in the OsgoodOriginal 
file, and then creates an array called allData. It then reads in each line of 
the file individually, strips the line, and then splits it by a comma to create
a dictionary. It then adds each of the words, and scores to the dictionary. Each
time a line is read, information on that line is saved into the values array. 
Finally it is appended to the wordData array, the file is closed, and the array
allData is returned. 
"""
def prepareSemanticDifferential():
    filename = ("OsgoodOriginal.csv") 
    fileIn = open(filename, 'r')
    allData = []

    #reading in each line of the file individually
    line = fileIn.readline()

    while line != "":

        #stripping contents of each line
        line = fileIn.readline().strip()

        if line != "":

            #seperating contents of each line by a comma
            values = line.split(',')

            wordData = {}

            #adding each word and EPA values to the dictionary
            wordData['word'] = str(values[0])
            wordData['evaluation'] = float(values[1])
            wordData['activity'] = float(values[2])
            wordData['potency'] = float(values[3])

            allData.append(wordData)
    fileIn.close()
    return allData

"""
This function has no input parameters. The purpose of the function is 
to calculate the evaluation, potency, and activity scores of a text
file (in this case we have input "PoliticalSpeech.txt", however this
can be replaced with any txt file). The function performs this calculation
through calling the readFile, getWords functios, iterating over the text 
file, determining if each word is an adjective or adverb by calling the 
findPOS function, then iterating over the OsgoodOriginal file to see 
whether each word is in the file, and then summing and printing the EPA 
values if they are in the file.
"""
def calculateSD():

    evaluationSum = 0
    activitySum = 0
    potencySum = 0
    osgoodWords = prepareSemanticDifferential()
    textFile = readFile("PoliticalSpeech.txt")
    textWord = getWords(textFile)

    for word in textWord:
        #separating punctuation from word and converting it to lowercase
        stripWord = word.strip("!., ")
        stripWord = stripWord.lower()

        #calling function findPOS and checking if an adjective or an adverb
        if findPOS(stripWord) == "ADJECTIVE" or findPOS(stripWord) == "ADVERB":

            #iterating over the list osgoodWords
            for index in range(len(osgoodWords)):

                 #checking each word(key) in each index of the list osgoodWords
                 if stripWord == osgoodWords[index]['word']:

                    #adding to sum total of evaluation/activity/potency if the word is in osgoodWords
                    evaluationSum += osgoodWords[index]['evaluation']
                    activitySum += osgoodWords[index]['activity']
                    potencySum += osgoodWords[index]['potency']

    #printing scores to two decimal places
    print("Evaluation Score: {:.2f}".format(evaluationSum))
    print("Activity Score is: {:.2f}".format(activitySum))
    print("Potency Score is: {:.2f}".format(potencySum))

calculateSD()

"""
This function does not have an input parameter. The functions
purpose is to iterate a given txt file, if it determines that
the word is an adjective, it increases the counter, and then 
returns the number of adjectives in the entire txt file.
"""
def countAdjectives():

    countAdj = 0
    textFile = readFile("PoliticalSpeech.txt")
    textWord = getWords(textFile)

    for word in textWord:

        #separating punctuation from word and converting it to lowercase
        stripWord = word.strip("!., ")
        stripWord = stripWord.lower()

        #calling function findPOS and checking if adjective
        if findPOS(stripWord) == "ADJECTIVE":

            #incrementing countAdj by one
            countAdj += 1
    return countAdj

countAdjectives()

"""
This function does not have an input parameter. The functions
purpose is to iterate a given txt file, if it determines that
the word is an adverb, it increases the counter, and then returns
the number of adverbs in the entire txt file.
"""
def countAdverbs():

    countAdv = 0
    textFile = readFile("PoliticalSpeech.txt")
    textWord = getWords(textFile)

    for word in textWord:

        #separating punctuation from word and converting it to lowercase
        stripWord = word.strip("!., ")
        stripWord = stripWord.lower()

        #calling function findPOS and checking if adverb
        if findPOS(stripWord) == "ADVERB":
            countAdv += 1

    return countAdv

countAdverbs()

"""
This function does not have input parameters. It iterates over a given
txt file, and returns the subset of unique words from the file
"""
def getUniqueWords():

    textFile = readFile("PoliticalSpeech.txt")
    textWord = getWords(textFile)
    uniqueList = []

    for word in textWord:

        #separating punctuation from word and converting to lowercase
        stripWord = word.strip("!., ")
        stripWord = stripWord.lower()

        #check if word is not already in the list
        if stripWord not in uniqueList:

            #add word to the list
            uniqueList.append(stripWord)

    return uniqueList

getUniqueWords()

"""
This function has no input parameters. The function iterates
over a txt file, and returns a dictionary showing each word
in the file and how many times it appears in the file.
"""
def countWords():

    countwordList = getUniqueWords()

    #assign variable to dictionary with specified keys and values
    countwordDict = dict.fromkeys(countwordList, 0)

    textFile = readFile("PoliticalSpeech.txt")
    textWord = getWords(textFile)

    for word in textWord:

        # separating punctuation from word and converting to lowercase
        stripWord = word.strip("!., ")
        stripWord = stripWord.lower()

        #increment the value of the key by one every time the stripped word appears
        countwordDict[stripWord] = (countwordDict[stripWord] + 1)

    return countwordDict

countWords()





