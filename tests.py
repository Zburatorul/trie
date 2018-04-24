'''
  Set of tests of the Trie datastructure implementation.
'''

from random import randrange, choice
import sys
import string
from trie_dict import Trie


# Magic constants
n = 10**3
m = 10

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

# populate
for word in words:
    t.addWord(word)

# test addition
for word in words:
    # is the word in the tree. It should be.
    res = t.getWords(word)
    for res_word in res:
        try:
            index = words.index(res_word)
        except:
            print('""%s" is missing from tree.' % res_word)

# test deletion
wordsToDelete = [choice(words) for x in range(n//10)]
for word in wordsToDelete:
    t.deleteWord(word)
    # is the word in the tree. Should not be.
    res = t.getWords(word)
    for res_word in res:
        # only check the deleted word, not  entire prefix
        if word == res_word:
            try:
                index = words.index(res_word)
                print('""%s" is in tree after deletion.' % res_word)
            except:
                pass

# test search

print('success.')
