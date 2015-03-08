Last updated: 2015-03-08
By Zhou Wang @ Columbia University
zw2288@columbia.edu

1. Word Counts
The word count program is implemented simply by reading in lines of words, adding single word counts to a hash table (key: word, value: count) and then printing the whole hash table with ascending order in keys.
The hyphen is handled properly, by concatenating the two parts together. Punctuations are deleted and letters are turned to lower case immediately after reading in a new line of words.

Limitations: this program only deals with characters in ASCII.

Efficiency: the time complexity is O(n) (n is the number of words in the text), the space complexity is O(m) (m is the number of distinct words in the text).


2. Running Median
The running median program is implemented using max heap and min heap. There are roughly three steps:
(1) Add new line count to heap
For a new line with k words, if k is smaller than the root of the max heap, push k to the max heap, otherwise to the min heap.
(2) Balance the two heaps
If the difference in number of nodes of the two heaps is greater than 1, balance the two heaps to reduce this difference to 0.
(3) Calculate the current running median
If the numbers of nodes are equal for the two heaps, the current median is (maxheap.root + minheap.root) / 2, otherwise the current median is the root of the heap with more elements.

Limitations: this program has to keep each line's number of words in memory, so cannot deal with extremely long text, but it is possible to use skiplist to improve the space complexity.

Efficiency: the time complexity is upper bounded by O(nlogn) (n is the number of lines), the space complexity is O(n).