'''
    A Trie implementation where each node is actually a dictionary.
    The '.' key of a node signifies that a word ending on that very letter is present
    in the tree.
'''


class Trie:

    def __init__(self):
        self.root = {}
        self.counter = 0


    def addWord(self, word):

        if len(word) == 0:
            return

        root = self.root
        for char in word:
            if char not in root.keys():
                root[char] = {}
            root = root[char]

        if '.' not in root.keys():
            root['.'] = None
            self.counter += 1


    def pruneBranch(self, root, char):
            if root == None:
                return
            if char == None:
                return
            self.root.pop(char, None)

    def deleteWord(self, word):
        '''
        Deletion is tricky because one must potentially delete many vertices.
        But must first inspect the final vertex.

        First we descend to the node corresponding to the final letter of the word.
        Then we walk back up deleting childless nodes.
        '''

        if len(word) == 0:
            return None

        root = self.root
        vertices = []
        i = 0

        while True:
            children = root.keys()
            if i == len(word):
                # we have found the right node
                # delete the '.'
                # does nothing if key wasn't there
                root.pop('.', None)
                if len(root.keys()) > 0:
                    # there are other valid children
                    # nothing else to do
                    return

                # the bottom node is unneeded now, potentially more cleanup
                break

            if word[i] in children:
                vertices.append(root)
                root = root[word[i]]
                i += 1
            else:
                return


        # Now we must walk back up the tree deleting unnecessary nodes.
        node = vertices.pop() # start at second to bottom node
        i -= 1

        while node != self.root and len(node.keys()) == 1:
            # walk back up the tree until we find another branch
            # stop when branch or when reading tree root
            node = vertices.pop()
            i -= 1 # keep track of letter corresponding to node

        # easy case
        if node == self.root:
            if len(node.keys()) == 1:
                self.root = {}
            else:
                # at the root, but it has branches
                node.pop(word[0], None)
            return

        # if here then there are at least two branches.
        # remove the walk we walked
        node.pop(word[i], None)



    def findNode(self, prefix):
        if len(prefix) == 0:
            return None

        root = self.root
        i = 0

        while True:
            children = root.keys()

            # if we have descended this many times, the current node
            # is the root of this prefix
            if i == len(prefix):
                return root
            if prefix[i] in children:
                root = root[prefix[i]]
                i += 1
            else:
                return None


    def getWordsRelative(self, root):
        # this node corresponds to the key '.' of the parent node,
        # which signifies that the  parent node is a word.
        if root == None:
            return ['']

        children = root.keys()

        if len(children) == 0:
            return ['']

        res = []
        for char in children:
            if char == '.':
                res.append('')
            else:
                child = root[char]
                words = self.getWordsRelative(child)
                for word in words:
                    res.append(char + word)

        return res

    def getWords(self, prefix):
        root = self.findNode(prefix)
        if root == None:
            return []

        # this prefix exists in the tree
        # now find all words originating at this node

        words = self.getWordsRelative(root)
        if words == []:
            return [prefix]
        words = [ prefix + word for word in words]
        return words

    def printAllWords(self):
        return self.getWordsRelative(self.root)


if __name__ == "__main__":
    t = Trie()
    #t.addWord('abld')
    #t.addWord('abcd')
    t.addWord('ab')
    t.addWord('a')
    t.addWord('ablp')
    print(t.getWords('ab'))
    print(t.getWords('abl'))
    print('Deleting ab')
    t.deleteWord('ab')
    print(t.getWords('a'))
