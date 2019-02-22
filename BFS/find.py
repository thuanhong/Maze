from collections import deque
from string import ascii_uppercase


class node():
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos

    def __eq__(self, other):
        return self.pos == other.pos


def find_path(maze, start):
    start_node = node(None, start)

    open_list = deque([start_node])
    closed_list = []
    # handle main
    while len(open_list) > 0:
        current_pos = open_list.popleft()

        if current_pos in closed_list:
            continue

        closed_list.append(current_pos)

        if maze[current_pos.pos[0]][current_pos.pos[1]] == '!' \
           or maze[current_pos.pos[0]][current_pos.pos[1]] == 'o':
            path = []
            current = current_pos
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1]

        for new in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            index_1 = current_pos.pos[0] + new[0]
            index_2 = current_pos.pos[1] + new[1]
            temp_node = (index_1, index_2)
            if maze[temp_node[0]][temp_node[1]] == '#' or\
               maze[temp_node[0]][temp_node[1]] in ascii_uppercase:
                continue
            new_node = node(current_pos, temp_node)
            if new_node not in closed_list:
                open_list.append(new_node)
