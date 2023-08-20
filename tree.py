class Node():
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            if node.parent is not self:
                node.parent = self

    def remove_child(self, node):
        self._children.remove(node)
        if node.parent is not self:
            node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent:
            self._parent.remove_child(self)

        self._parent = node
        if node:
            node.add_child(self)

    def depth_search(self, value):

        if self._value == value:
            return self

        for child in self._children:
            res = child.depth_search(value)
            if res:
                return res

    def breadth_search(self, value):
        if self._value == value:
            return self

        queue = self._children.copy()

        while queue:
            curr_child = queue.pop(0)
            if curr_child._value == value:
                return curr_child
            queue.extend(curr_child._children)




# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)
