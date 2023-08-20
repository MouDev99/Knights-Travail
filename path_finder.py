from tree import Node

class KnightPathFinder():
    def __init__(self, position):
        self._root = Node(position)
        self._considered_positions = set([self._root])


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


# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}
