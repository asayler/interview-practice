TYPE_MIN = "min"
TYPE_MAX = "max"

class Heap(object):

    def __init__(self, typ=TYPE_MAX):
        self._typ = typ
        self._ary = []
        if typ == TYPE_MIN:
            self._ordered = lambda parent, child: parent <= child
        elif typ == TYPE_MAX:
            self._ordered = lambda parent, child: parent >= child
        else:
            raise ValueError("Unsupported typ value: '{}'".format(typ))

    def _l_child_idx(self, cur):
        idx = (cur * 2) + 1
        return idx if idx < len(self._ary) else None

    def _r_child_idx(self, cur):
        idx = (cur * 2) + 2
        return idx if idx < len(self._ary) else None

    def _parent_idx(self, cur):
        return (cur - 1) // 2 if cur else None

    def insert(self, val):
        self._ary.append(val)
        lower = len(self._ary) - 1
        while True:
            pnt = self._parent_idx(lower)
            if (pnt is not None) and (not self._ordered(self._ary[pnt], self._ary[lower])):
                self._ary[pnt], self._ary[lower] = self._ary[lower], self._ary[pnt]
                lower = pnt
            else:
                break

    def remove(self):

        if len(self._ary) == 0:
            return None
        elif len(self._ary) == 1:
            return self._ary.pop()
        else:
            ret = self._ary[0]
            self._ary[0] = self._ary.pop()
            pnt = 0
            while True:
                upper = pnt
                lchd = self._l_child_idx(pnt)
                rchd = self._r_child_idx(pnt)
                if (lchd is not None) and (not self._ordered(self._ary[upper], self._ary[lchd])):
                    upper = lchd
                if (rchd is not None) and (not self._ordered(self._ary[upper], self._ary[rchd])):
                    upper = rchd
                if pnt != upper:
                    self._ary[pnt], self._ary[upper] = self._ary[upper], self._ary[pnt]
                    pnt = upper
                else:
                    break
            return ret
