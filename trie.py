#


class Node:

    def __init__(self, letter):
        self.children = {}
        self.isWord = False
        self.letter = letter




class Trie:

    def __init__(self):
        self.root = Node('')


    def addWord(self, word):

        if len(word) == 0:
            return

        root = self.root
        i = 0
        wlen = len(word)

        while True:
            if i < wlen:
                children = root.children
                if word[i] in children.keys():
                    root = children[word[i]]
                else:
                    n = Node(word[i])
                    root.children[word[i]] = n
                    root = n
                i += 1
            else:
                # We have added the word. Now mark it as a word in itself.
                root.isword = True
                return
   
    def findNode(self, prefix):
        if len(prefix) == 0:
            return None

        root = self.root
        i = 0

        while True:
            children = root.children

            print('Children are: ', children.keys())
            if i == len(prefix):
                return root
            if prefix[i] in children.keys():
                root = children[prefix[i]]
                i += 1
                print('Found prefix %s' % prefix[:i])
            else:
                return None


    def getWordsRelative(self, root):
        children = root.getChildren()
        print('Looking for words starting with', children.keys())
        if len(children.keys()) == 0:
            return ['']

        res = []
        for char in children.keys():     
            child = children[char]
            words = self.getWordsRelative(child)
            for word in words:
                res.append(char + word)

        return res

    def getWords(self, prefix):
        root = self.findNode(prefix)
        if root == None:
            return []
       
        print('Found node for prefix %s' % prefix)
        print('Node char is %s' % root.getLetter())

        words = self.getWordsRelative(root)
        print('words=', words)
        if words == []:
            return [prefix]
        words = [ prefix + word for word in words]
        if root.isword:
            words.append(prefix)
        return words

t = Trie()
t.addWord('abld')
t.addWord('abcd')
t.addWord('ablp')
t.addWord('ab')
print(t.getWords('ab'))
print(t.getWords('abl'))
