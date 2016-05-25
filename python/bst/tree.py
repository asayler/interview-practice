import collections

class Node(object):

    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right

class Tree(object):

    def __init__(self, init=None):

        self.root = None
        if init:
            for val in init:
                self.insert(val)

    def _insert(self, new, root):

        assert(isinstance(new, Node))
        assert(isinstance(root, Node))

        if new.value < root.value:
            if not root.left:
                root.left = new
            else:
                self._insert(new, root.left)
        else:
            if not root.right:
                root.right = new
            else:
                self._insert(new, root.right)

    def insert(self, val):

        new = Node(val)
        if not self.root:
            self.root = new
        else:
            self._insert(new, self.root)


    def _find(self, val, root):

        if not root:
            return False
        else:
            if val < root.value:
                return self._find(val, root.left)
            elif val > root.value:
                return self._find(val, root.right)
            else:
                return True

    def find(self, val):
        return self._find(val, self.root)

    def _traverse_depth(self, root):

        out = []
        if root:
            out.append(root.value)
            out += self._traverse_depth(root.left)
            out += self._traverse_depth(root.right)
        return out

    def traverse_depth(self):
        return self._traverse_depth(self.root)

    def traverse_depth_2(self):

        out = []
        s = []
        s.append(self.root)

        while s:
            node = s.pop()
            if node:
                out.append(node.value)
                s.append(node.right)
                s.append(node.left)

        return out

    def traverse_breadth(self):

        out = []
        q = collections.deque()
        q.append(self.root)

        while q:
            node = q.popleft()
            if node:
                out.append(node.value)
                q.append(node.left)
                q.append(node.right)

        return out
