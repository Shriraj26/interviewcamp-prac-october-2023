"""
Watch the neetcode video for more details!! - 
https://www.youtube.com/watch?v=oobqoCJlHA0
"""
class Trie:
    
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['isWord'] = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return curr.get('isWord', False)

    def startsWith(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return True
