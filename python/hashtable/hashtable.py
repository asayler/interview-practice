#!/use/env python3

# Create a hash table for ints using only arrays and base operators

def cormen_div(bins, val):
    return val % bins

def knuth_div(bins, val):
    return (val * (val + 3)) % bins

_DEFAULT_BINS = 947 # Should be prime
_DEFAULT_FUNC = knuth_div

class Node(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None

class IntHashTable(object):

    def __init__(self, bins=_DEFAULT_BINS, func=_DEFAULT_FUNC):

        self._func = func
        self._array = [None] * bins

    def put(self, key, val):

        b = self._func(len(self._array), key)

        if not self._array[b]:
            self._array[b] = Node(key, val)
        else:
            node = self._array[b]
            while node.key != key:
                if node.nxt:
                    node = node.nxt
                else:
                    break
            if node.key == key:
                node.val = val
            else:
                node.nxt == Node(key, val)

    def get(self, key):

        b = self._func(len(self._array), key)

        if not self._array[b]:
            raise KeyError("{} not found".format(key))
        else:
            node = self._array[b]
            while node.key != key:
                if node.nxt:
                    node = node.nxt
                else:
                    break
            if node.key == key:
                return node.val
            else:
                raise KeyError("{} not found".format(key))
