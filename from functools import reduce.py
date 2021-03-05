from functools import reduce

class TrieNode:
    def __init__(self):
        self.c = dict()
        self.sym = None
    
def bracket(words, symbols):
    root = TrieNode()
    for s in symbols:
        t = root
        for char in s:
            if char not in t.c:
                t.c[char] = TrieNode()
            t = t.c[char]
        t.sym = s
    result = dict()
    for word in words:
        i = 0
        symlist = list()
        while i < len(word):
            j, t = i, root
            while j < len(word) and word[j] in t.c:
                t = t.c[word[j]]
                if t.sym is not None:
                    symlist.append((j+1-len(t.sym), j+1, t.sym))
                j += 1
            i += 1
        if len(symlist) > 0:
            sym = reduce(lambda x, y: x if x[1]-x[0] >= y[1]-y[0] else y, symlist)
            result[word] = "{}[{}]{}".format(word[:sym[0]], sym[2], word[sym[1]:])
    return tuple(word if word not in result else result[word] for word in words)