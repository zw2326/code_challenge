# Word Count
# by Zhou Wang @ Columbia University
# 2015-03-06

__author__="Zhou Wang  <zw2288@columbia.edu>"
__date__ ="$Mar 6th, 2015"

import string
import os
import platform
import sys
import math

# go through all input files and add their word counts to wordCount
def UpdateAllWordCount(wordCount, allFiles):
    countFile = 0
    for i in allFiles:
        print "\r" + str(countFile) + " out of " + str(len(allFiles)) + " input files analyzed ...",
        try:
            fid = open(inputFilesPath + "/" + i, "r")
            UpdateCurrentWordCount(wordCount, fid)
            fid.close()
        except: # current input file access permission denied
            print "\nError: file " + i + " cannot be analyzed."
            exit()
        countFile += 1

    print "\r" + str(countFile) + " out of " + str(len(allFiles)) + " input files analyzed ..."
    return


# add current file's word counts to wordCount
def UpdateCurrentWordCount(wordCount, fid):
    backUp = ""
    toNextLine = False
    for i in fid: # go through all sentences in the current file
        currentLine = (i.strip()).lower()      # remove \n and space at the end of the sentence, to lower
        if toNextLine == True:
            currentLine = backUp + currentLine
            toNextLine = False
        if len(currentLine) == 0:
            continue
        if currentLine[-1] == "-":
            toNextLine = True
        currentLine = currentLine.translate(table, string.punctuation) # remove punctuations
        currentFields = currentLine.split(" ") # split words by space
        if toNextLine == True:
            backUp = currentFields[-1]
            del currentFields[-1]
        for j in currentFields:
            if j == "": # ignore null words
                continue
            try: # NOTE: this is much faster than: if not k in wordCount.keys()
                wordCount[j] += 1
            except:
                wordCount[j] = 1
    return


def usage():
    print """
    python word_count.py
        Read in all input files and output word counts.
    """




if __name__ == "__main__":
    if platform.platform() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    # no extra parameter expected
    if len(sys.argv) != 1:
        usage()
        exit()

    inputFilesPath = "wc_input"
    outputFilesPath = "wc_output"
    outputFileName = "wc_result.txt"
    wordCount = {}
    table = string.maketrans("", "")

    if not os.path.isdir(inputFilesPath): # input file directory not exist
        print "Error: input file directory " + inputFilesPath + " does not exist."
        exit()

    # go through all files in wc_input
    allFiles = os.listdir(inputFilesPath)
    print "Analyzing input files:"
    UpdateAllWordCount(wordCount, allFiles)
    print "Analysis: Done."

    # make sure the output file directory exists
    if not os.path.isdir(outputFilesPath):
        os.makedirs(outputFilesPath)

    # go through all words recorded, write to wc_result.txt
    print "Exporting results:",
    fid = open(outputFilesPath + "/" + outputFileName, "w")
    for key, value in sorted(wordCount.items()): # write in alphabetical order
        fid.write(key + "\t" + str(value) + "\n")
    fid.close()
    print "Done\n"

