from math import sqrt
from time import time

class node():
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos

    def __eq__(self, other):
        return self.pos == other.pos

def distance(cur, goal):
    return sqrt((goal[0] - cur[0])**2 + (goal[1] - cur[1])**2)

def gbfs(maze, start, end):
    start_node = node(None, start)
    end_node = node(None, end)

    open_list = []
    closed_list = []

    open_list.append(start_node)
    # handle main
    while len(open_list) > 0:
        current_pos = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list): # find the point have coordinate nearest end_node
            if distance(current_pos.pos, end_node.pos) > distance(item.pos, end_node.pos):
                current_pos = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_pos)

        if current_pos == end_node: # output path if find end_node
            path = []
            current = current_pos
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1]

        for new in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # find 4 way to get position
            temp_node = (current_pos.pos[0] + new[0], current_pos.pos[1] + new[1])
            try:
                if maze[temp_node[0]][temp_node[1]] != '#':
                    new_node = node(current_pos, temp_node)
                    if new_node not in closed_list:
                        open_list.append(new_node)
            except:
                pass


def main():
    maze = []
    f = open('maze(L)1', 'r')
    maze = f.read().split('\n')[:-1]
    begin = time()
    move = gbfs(maze, (1, 1), (96, 97))
    print(str(time() - begin) + '\n')
    for x, i in enumerate(maze):
        for y in range(len(i)):
            if (x, y) in move:
                print('\x1b[6;30;42m{}\x1b[0m' .format(' '), end = '')
            else:
                print(maze[x][y], end='')
        print()

if __name__ == '__main__':
    main()
