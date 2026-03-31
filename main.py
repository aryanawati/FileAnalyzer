import string

def countWords(lineList):
    words = 0
    chars = 0
    spaces = 0

    #Iterate through each line in the file
    for line in lineList:
        #Iterate through each character on the line
        for letter in line:
            if letter == " " or letter == "\n" or letter == "\t":
                spaces += 1
            else:
                chars += 1
        #Creates a new list of all words, splitting at each instance of a space, linebreak, or tab
        wordlist = line.split()
        words += len(wordlist)
    return (words, chars, spaces)
def longestWords(lineList):

    words = []
    for line in lineList:
        wordlist = line.split()
        for word in wordlist:
            words.append(word.strip(string.punctuation))

    words.sort(reverse=True, key=len)

    for word in reversed(range(len(words) - 1)):
        if words[word] == words[word - 1]:
            words.pop(word)
    
    longest10 = []
    for i in range(0,9):
        longest10.append(words[i])
    
    return longest10         



inputFile = open("inputfile.txt" , "r")
outputFile = open("outputfile.txt" , "w")

contents = inputFile.readlines()
lines = len(contents)
wordCount, charCount, spaceCount = countWords(contents)

outputFile.write(f"Number of Lines: {lines}\n")
outputFile.write(f"Number of Words: {wordCount}\n")
outputFile.write(f"Number of Characters: {charCount}\n")
outputFile.write(f"Number of Characters (No Spaces): {charCount - spaceCount}\n")
outputFile.write(f"Longest Words: {longestWords(contents)}\n")

outputFile.close()
inputFile.close()