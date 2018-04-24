'''
  Set of tests of the Trie datastructure implementation.
'''

from random import randrange, choice
import sys
import string
from trie_dict import Trie


# Upper and lower-case
letters = string.ascii_letters


# Generate n random words, up to length m
words = []

for i in range(n):
    thisWordLength = randrange(1, m)
    lst = [choice(letters) for x in range(thisWordLength)]
    word = reduce(lambda x,y : x+y, lst)
    words.append(word)

t = Trie()

for word in words:
    t.addWord(word)
