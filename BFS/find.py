from string import ascii_uppercase

class node():
    '''
    create a node and set current position and it parent position
    '''
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos

    def __eq__(self, other):
        return self.pos == other.pos


def find_path(maze, start):
    '''
    use BFS algorithm to find shortest way
    '''
    # declare start point
    start_node = node(None, start)

    open_list = [start_node]

    # handle main
    while open_list:
        current_pos = open_list.pop(0)

        if maze[current_pos.pos[0]][current_pos.pos[1]] is '.':
            continue

        if maze[current_pos.pos[0]][current_pos.pos[1]] == 'o':
            path = []
            current = current_pos
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1]

        maze[current_pos.pos[0]][current_pos.pos[1]] = '.'
        for new in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            index_1 = current_pos.pos[0] + new[0]
            index_2 = current_pos.pos[1] + new[1]
            temp_node = (index_1, index_2)

            if maze[temp_node[0]][temp_node[1]] != '#' and \
                not maze[temp_node[0]][temp_node[1]] in ascii_uppercase:
                new_node = node(current_pos, temp_node)
                if maze[new_node.pos[0]][new_node.pos[1]] != '.':
                    open_list.append(new_node)
