from tree import Node

class KnightPathFinder():
    def __init__(self, position):
        self._root = Node(position)
        self._considered_positions = set([position])


    def get_valid_moves(self, pos):
        x, y = pos
        moves = [(x+1, y+2), (x+1, y-2), (x+2, y+1), (x+2, y-1),
                 (x-1, y+2), (x-1, y-2), (x-2, y+1), (x-2, y-1)]

        def valid_pos(p):
            x, y = p
            return 0 <= x <= 7 and 0 <= y <= 7

        valid_moves = set(filter(valid_pos, moves))

        return valid_moves

    def new_move_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        new_postitons = valid_moves - self._considered_positions
        self._considered_positions.update(new_postitons)

        return new_postitons

    def build_move_tree(self):

       queue = [self._root]
       while queue:
        currNode = queue.pop(0)
        new_moves = self.new_move_positions(currNode._value)
        for move in new_moves:
            child_node = Node(move)
            currNode.add_child(child_node)
            queue.append(child_node)




    def find_path(self, end_position):
        node = self._root.depth_search(end_position)
        return self.trace_to_root(node)

    def trace_to_root(self, end_node):
        res = []
        currNode = end_node
        while currNode:
            res.append(currNode._value)
            currNode = currNode._parent

        res.reverse()
        return res




# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}

# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder._root.children)


finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((2, 1))) # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3))) # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
print(finder.find_path((7, 6))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
