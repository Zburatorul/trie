'''
    A Trie implementation where each node is actually a dictionary.

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
                root.pop('.', None)


                # if this node is not a parent, delete it
                while True:
                    # walk back up the tree until we find another branch.
                    node = vertices.pop()
                    if len(node.keys) > 1:
                        

                    if node == self.root:
                        self.root = {}
                        return


                return

            if word[i] in children:
                vertices.append(root)
                root = root[word[i]]
                i += 1
                #print('Found prefix %s' % word[:i])
            else:
                return None


    def findNode(self, prefix):
        if len(prefix) == 0:
            return None

        root = self.root
        i = 0

        while True:
            children = root.keys()

            #print('Children are: ', children)

            # if we have descended this may times, the current node
            # is the root of this prefix
            if i == len(prefix):
                return root
            if prefix[i] in children:
                root = root[prefix[i]]
                i += 1
                print('Found prefix %s' % prefix[:i])
            else:
                return None


    def getWordsRelative(self, root):
        # this node corresponds to the key '.' of the parent node,
        # which signifies that the  parent node is a word.
        if root == None:
            return ['']

        children = root.keys()

        #print('Looking for words with', children)
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

        #print('Found node for prefix %s' % prefix)
        #print('Node char is %s' % prefix[-1])

        words = self.getWordsRelative(root)
        print('words=', words)
        if words == []:
            return [prefix]
        words = [ prefix + word for word in words]
        return words

    def printAllWords(self):
        return self.getWordsRelative(self.root)


if __name__ == "__main__":
    t = Trie()
    t.addWord('abld')
    t.addWord('abcd')
    t.addWord('ablp')
    print(t.getWords('ab'))
    t.addWord('ab')

    #print(t.printAllWords())
    print(t.getWords('ab'))
    print(t.getWords('abl'))
    t.deleteWord('abcd')
    print(t.getWords('ab'))
