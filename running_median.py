# Running Median
# by Zhou Wang @ Columbia University
# 2015-03-07

__author__="Zhou Wang  <zw2288@columbia.edu>"
__date__ ="$Mar 7th, 2015"

from heapq import *
import math
import os
import platform
import string
import sys


# calculate current file's running median
def CalculateCurrentRunningMedian(fidIn, fidOut, minHeap, maxHeap):
    backUp = ""
    toNextLine = False
    for i in fidIn:
        currentLine = (i.strip()).lower() # remove \n and space at the end of the sentence, to lower
        if toNextLine == True:
            currentLine = backUp + currentLine
            toNextLine = False
        if len(currentLine) == 0: # this is an empty line
            lenCurrentLine = 0
        else:
            if currentLine[-1] == "-":
                toNextLine = True
            currentLine = currentLine.translate(table, string.punctuation) # remove punctuations
            currentFields = currentLine.split(" ") # split words by space
            if toNextLine == True:
                backUp = currentFields[-1]
                del currentFields[-1]
            lenCurrentLine = len(currentFields)
            for j in currentFields:
                if j == "":
                    lenCurrentLine -= 1

        # add the new item to one of the heaps

        if len(maxHeap) == 0:
            heappush(maxHeap, -lenCurrentLine)
        else:
            maxMaxHeap = -heappop(maxHeap)
            heappush(maxHeap, -maxMaxHeap)
            if lenCurrentLine < maxMaxHeap:
                heappush(maxHeap, -lenCurrentLine)
            else:
                heappush(minHeap, lenCurrentLine)

        # print maxHeap, minHeap
        # balance the heaps
        if len(maxHeap) > len(minHeap) + 1:
            tmp = heappop(maxHeap)
            heappush(minHeap, -tmp)
        elif len(minHeap) > len(maxHeap) + 1:
            tmp = heappop(minHeap)
            heappush(maxHeap, -tmp)

        currentMedian = -1
        # calculate current running median
        if len(maxHeap) > len(minHeap):
            maxMaxHeap = heappop(maxHeap)
            currentMedian = -maxMaxHeap
            heappush(maxHeap, maxMaxHeap)
        elif len(maxHeap) == len(minHeap):
            maxMaxHeap = heappop(maxHeap)
            maxMinHeap = heappop(minHeap)
            currentMedian =float(-maxMaxHeap + maxMinHeap) / 2
            heappush(maxHeap, maxMaxHeap)
            heappush(minHeap, maxMinHeap)
        else:
            maxMinHeap = heappop(minHeap)
            currentMedian = maxMinHeap
            heappush(minHeap, maxMinHeap)

        currentMedian = "%.1f" % currentMedian
        fidOut.write(currentMedian + "\n")
        # print currentMedian
        # print maxHeap, minHeap
        # print "\n"
        # a = raw_input()
    return


# calculate all files' running median
def CalculateAllRunningMedian(allFiles, fidOut):
    minHeap, maxHeap = [], []

    for i in allFiles: # go through all files
        print i
        fidIn = open(inputFilesPath + "/" + i, "r")
        CalculateCurrentRunningMedian(fidIn, fidOut, minHeap, maxHeap)
        fidIn.close()
    return


def usage():
    print """
    python running_median.py
        Read in all input files and output running median.
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
    outputFileName = "med_result.txt"
    wordCount = {}
    table = string.maketrans("", "")

    # make sure the input file directory exists
    if not os.path.isdir(inputFilesPath):
        print "Error: input file directory " + inputFilesPath + " does not exist."
        exit()
    # make sure the output file directory exists
    if not os.path.isdir(outputFilesPath):
        os.makedirs(outputFilesPath)

    # go through all files in wc_input, output running median
    allFiles = os.listdir(inputFilesPath)
    allFiles.sort()
    fidOut = open(outputFilesPath + "/" + outputFileName, "w")
    print "Analyzing input files:"
    CalculateAllRunningMedian(allFiles, fidOut)
    print "Analysis: Done."
    fidOut.close()

