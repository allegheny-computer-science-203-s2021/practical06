"""Compute term frequencies for an input file using a pipeline style."""

import sys
import re
import operator
import string

# TODO: fix faults in the program


def read_file(path_to_file):

    """Take a path to a file and return the entire contents of the file as a string"""

    with open(path_to_file) as f:
        data = f.read()
    return data


def filter_chars_and_normalize(str_data):

    """Take a string and return a copy with all non-alphanumeric chars replaced by white space"""

    # perform pattern matching to extract the words
    # TODO: hint - \W matches a "non-word", \w will match a word.
    # TODO: + will match 1 or more of the preceding token
    pattern = re.compile(r"[\w_]+")
    return pattern.sub(" ", str_data).lower()


def scan(str_data):

    """Takes a string and scans for words and return a list of words"""

    return str_data.split()


def remove_stop_words(word_list):

    """Take a list of words and return a copy with all stop words removed"""

    # load the list of stop words from the file
    with open("stopwords/stop_words.txt") as f:
        stop_words = f.read().split(",")
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if w not in stop_words]


def frequencies(word_list):

    """Take a list of words and return a dictionary of words with frequencies of occurrence"""

    word_freqs = {}
    # iterate through the list of words
    for w in word_list:
        # the word has already been found
        if w in word_freqs:
            word_freqs[w] += 1
        # the word has not yet already been found
        else:
            word_freqs[w] = 1
    return word_freqs


def sort(word_freq):

    """Take a dictionary of word frequencies and return a list of pairs sorted by frequency"""

    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)


def print_all(word_freqs):

    """Takes a list of pairs where the entries are sorted by frequency and print them recursively"""

    if word_freqs:
        print(word_freqs[0][0], ' - ', word_freqs[0][1])
        print_all(word_freqs[1:])


#
# The main function
#

if __name__ == "__main__":
    print_all(
        sort(
            frequencies(
                remove_stop_words(
                    scan(filter_chars_and_normalize(read_file(sys.argv[1])))
                )
            )
        )
    )
