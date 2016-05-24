TYPE_MIN = "min"
TYPE_MAX = "max"

class Heap(object):

    def __init__(self, typ=TYPE_MAX, heapify=None):
        self._typ = typ
        if typ == TYPE_MIN:
            self._ordered = lambda parent, child: parent <= child
        elif typ == TYPE_MAX:
            self._ordered = lambda parent, child: parent >= child
        else:
            raise ValueError("Unsupported typ value: '{}'".format(typ))
        if heapify:
            self._ary = heapify
            self._len = len(self._ary)
            for i in reversed(range(0, self._len // 2)):
                self._sift_down(i)
        else:
            self._ary = []
            self._len = 0

    def _l_child_idx(self, cur):
        idx = (cur * 2) + 1
        return idx if idx < self._len else None

    def _r_child_idx(self, cur):
        idx = (cur * 2) + 2
        return idx if idx < self._len else None

    def _parent_idx(self, cur):
        return (cur - 1) // 2 if cur else None

    def _sift_up(self, idx):

        child = idx
        parent = self._parent_idx(child)
        if (parent is not None) and (not self._ordered(self._ary[parent], self._ary[child])):
            self._ary[parent], self._ary[child] = self._ary[child], self._ary[parent]
            self._sift_up(parent)

    def _sift_down(self, idx):

        parent = idx
        lchild = self._l_child_idx(parent)
        rchild = self._r_child_idx(parent)
        if (lchild is not None) and (not self._ordered(self._ary[parent], self._ary[lchild])):
            parent = lchild
        if (rchild is not None) and (not self._ordered(self._ary[parent], self._ary[rchild])):
            parent = rchild
        if idx != parent:
            self._ary[idx], self._ary[parent] = self._ary[parent], self._ary[idx]
            self._sift_down(parent)

    def insert(self, val):

        if len(self._ary) > self._len:
            self._ary[self._len] = val
        else:
            self._ary.append(val)
        child = self._len
        self._len += 1
        self._sift_up(child)

    def remove(self):

        if self._len == 0:
            return None
        elif self._len == 1:
            self._len -= 1
            return self._ary[0]
        else:
            ret = self._ary[0]
            self._ary[0] = self._ary[self._len-1]
            self._len -= 1
            idx = 0
            self._sift_down(idx)
            return ret

    def sort(self):

        while(self._len):
            val = self.remove()
            self._ary[self._len] = val
        return self._ary
