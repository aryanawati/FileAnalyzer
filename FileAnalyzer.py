import string
import tkinter as tk
from tkinter import filedialog

import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

def getFileContents():
    choice = input("Use Example .txt File? (y/n)").lower()

    if choice == "y":
        filename = "inputfile.txt"
        with open(filename, "r") as f:
            return f.readlines()
    elif choice == "n":
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        root.update()
        try:
            filename = filedialog.askopenfilename(
                title="Select a .txt file",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
        finally:
            root.quit()
            root.destroy()
        if not filename:
            print("No file selected.")
            return None
    else:
        print("Invalid Choice")
        return None
    
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print("File not found.")
        return None
    
contents = getFileContents()
if contents:
    print("File loaded successfully.")

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

def freqWords(lineList):
    words = []
    for line in lineList:
        wordlist = line.split()
        for word in wordlist:
            words.append(word.strip(string.punctuation))
    wordCounts = Counter(words)
    freqWordsList = wordCounts.most_common(10)

    return freqWordsList

def graph(lineList):
    graphPref = input("Would you like to graph word frequencies (y/n)").lower()
    if graphPref == "y":
        df = pd.DataFrame(freqWords(lineList), columns=["Word", "Frequency"])
        plt.bar(df["Word"], df["Frequency"])
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
    elif graphPref == "n":
        return None
    else:
        print("Invalid Option")
        return None


outputFile = open("outputfile.txt" , "w")

lines = len(contents)
wordCount, charCount, spaceCount = countWords(contents)

outputFile.write(f"Number of Lines: {lines}\n")
outputFile.write(f"Number of Words: {wordCount}\n")
outputFile.write(f"Number of Characters: {charCount}\n")
outputFile.write(f"Number of Characters (No Spaces): {charCount - spaceCount}\n")
outputFile.write(f"Longest Words: {longestWords(contents)}\n")
outputFile.write(f"Most Frequent Words: {freqWords(contents)}\n")

print(
    f"Number of Lines: {lines}\n",
    f"Number of Words: {wordCount}\n",
    f"Number of Characters: {charCount}\n",
    f"Number of Characters (No Spaces): {charCount - spaceCount}\n",
    f"Longest Words: {longestWords(contents)}\n",
    f"Most Frequent Words: {freqWords(contents)}\n"
)

graph(contents)

outputFile.close()