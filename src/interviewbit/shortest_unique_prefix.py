#https://www.interviewbit.com/problems/shortest-unique-prefix/
class Trie:
    def __init__(self, children={}):
        self.children = children

    def __str__(self):
        return str(self.children)

    def add(self, word):
        if word:
            if word[0] not in self.children:
                self.children[word[0]] = Trie({})
            self.children[word[0]].add(word[1:])

def shortest_prefix(t, word, pfx):
    if word:
        if len(t.children.keys()) > 1:
            return (pfx + word[0] + shortest_prefix(t.children[word[0]], word[1:], ''))
        else:
            return(shortest_prefix(t.children[word[0]], word[1:], pfx + word[0]))
    else:
        return('')

words = ["zebra", "dogs", "duck", "dove", "doggie", "zenbot"]
tree = Trie({})
for word in words:
    tree.add(word)

output = [shortest_prefix(tree, word, "") for word in words]
print(output)

