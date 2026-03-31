def countWords(lineList):
    words = 0
    chars = 0
    spaces = 0
    for line in lineList:
        for letter in line:
            if letter == " " or letter == "\n" or letter == "\t":
                spaces += 1
            else:
                chars += 1
        wordlist = line.split()
        words += len(wordlist)
    return (words, chars, spaces)


inputFile = open("inputfile.txt" , "r")
outputFile = open("outputfile.txt" , "w")

contents = inputFile.readlines()
lines = len(contents)
wordCount, charCount, spaceCount = countWords(contents)

outputFile.write(f"Number of Lines: {lines}\n")
outputFile.write(f"Number of Words: {wordCount}\n")
outputFile.write(f"Number of Characters: {charCount}\n")
outputFile.write(f"Number of Characters (No Spaces): {charCount - spaceCount}\n")

outputFile.close()
inputFile.close()