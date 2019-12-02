from time import time

class node():
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos
        self.g = 0
    def __eq__(self, other):
        return self.pos == other.pos

def distance(start, current, end):
    h = abs(current.pos[0] - end.pos[0]) + abs(current.pos[1] - end.pos[1])
    return h + current.g

def gbfs(maze, start, end):
    start_node = node(None, start)
    end_node = node(None, end)

    open_list = [

    open_list.append(start_node)
    # handle main
    while len(open_list) > 0:
        current_pos = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list): # find the point have coordinate nearest end_node
            if distance(start_node, current_pos, end_node) > distance(start_node, item, end_node):
                current_pos = item
                current_index = index

        open_list.pop(current_index)
        maze[current_pos.pos[0]][current_pos.pos[1]] = '.'

        if current_pos == end_node: # output path if find end_node
            path = []
            current = current_pos
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1]

        for new in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # find 4 way to get position
            temp_node = (current_pos.pos[0] + new[0], current_pos.pos[1] + new[1])
            if maze[temp_node[0]][temp_node[1]] != '#':
                new_node = node(current_pos, temp_node)
                if maze[new_node.pos[0]][new_node.pos[1]] != '.':
                    new_node.g = new_node.parent.g + 1
                    open_list.append(new_node)

def bfs(maze, start):

    start_node = node(None, start)

    open_list = [start_node]

    # handle main
    while len(open_list) > 0:
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

            if maze[temp_node[0]][temp_node[1]] != '#':
                new_node = node(current_pos, temp_node)
                if maze[new_node.pos[0]][new_node.pos[1]] != '.':
                    open_list.append(new_node)

def main():
    maze = []
    f = open('maze(L)2', 'r')
    maze_temp = f.read().split('\n')[:-1]

    for x in maze_temp:
        temp = []
        for y in x:
            temp.append(y)
        maze.append(temp)

    begin = time()
    move = gbfs(maze, (1, 1), (96, 97))
    print(str(time() - begin) + '\n')
    for x, i in enumerate(maze):
        for y in range(len(i)):
            if (x, y) in move:
                print('\x1b[6;30;42m{}\x1b[0m' .format(' '), end = '')
            elif maze[x][y] is '.':
                print('\x1b[6;30;41m{}\x1b[0m' .format(' '), end = '')
            else:
                print(maze[x][y], end='')
        print()

    maze.clear()
    for x in maze_temp:
        temp = []
        for y in x:
            temp.append(y)
        maze.append(temp)

    begin = time()
    move = bfs(maze, (1, 1))
    print(str(time() - begin) + '\n')

    for x, i in enumerate(maze):
        for y in range(len(i)):
            if (x, y) in move:
                print('\x1b[6;30;42m{}\x1b[0m' .format(' '), end = '')
            elif maze[x][y] is '.':
                print('\x1b[6;30;41m{}\x1b[0m' .format(' '), end = '')
            else:
                print(maze[x][y], end='')
        print()

if __name__ == '__main__':
    main()
