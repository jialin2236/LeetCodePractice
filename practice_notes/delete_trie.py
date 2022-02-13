class TrieNode(object):
    def __init__(self):
        self.child = [None] * 26
        self.EndChar = False

class Trie(object):
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def toIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pi = self.root
        depth = len(key)
        for lvl in range(depth):
            lvl_i = self.toIndex(lvl)
            if not pi.child[lvl_i]:
                pi.child[lvl_i] = self.getNode()
            pi = pi.child[lvl_i]
        pi.EndChar = True

    def search(self, key):
        pi = self.root
        if not pi:
            return False
        depth = len(key)
        for lvl in range(depth):
            lvl_i = self.toIndex(lvl)
            if not pi.child[lvl_i]:
                return False
            pi = pi.child[lvl_i]
        if pi.EndChar:
            return True

    def isEmpty(self, node):
        for i in range(26):
            if node.child[i]:
                return False
        return True

    def remove(self, root, key, depth):
        if not root:
            return None
        if depth == len(key) - 1:
            if root.EndChar:
                root.EndChar = False
            if self.isEmpty(root):
                root = None
        index = self.toIndex(key[depth])
        root.child[index] = self.remove(root.child[index], key, depth+1)
        if self.isEmpty(root) and root.EndChar is False:
            root = None
        return root
