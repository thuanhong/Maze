from math import sqrt
import sys

class node():
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos

    def __eq__(self, other):
        return self.pos == other.pos

def distance(cur, goal):
    return sqrt((goal[0] - cur[0])**2 + (goal[1] - cur[1])**2)

def find_path(maze, start, end):
    # declare start point vs end point
    start_node = node(None, start)
    end_node = node(None, end)

    # create two list emppty
    open_list = []
    closed_list = []

    open_list.append(start_node)
    # handle main
    while len(open_list) > 0:
        current_pos = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if distance(current_pos.pos, end_node.pos) > distance(item.pos, end_node.pos):
                current_pos = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_pos)

        if current_pos == end_node:
            path = []
            current = current_pos
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1]

        for new in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            temp_node = (current_pos.pos[0] + new[0], current_pos.pos[1] + new[1])
            sys.stderr.write(str(temp_node))
            if maze[temp_node[0]][temp_node[1]] == '#':

                continue
            new_node = node(current_pos, temp_node)
            if new_node not in closed_list:
                open_list.append(new_node)

# def main():
#
#     maze = ['####################',
#             '#                  #',
#             '#                  #',
#             '#                  #',
#             '#                  #',
#             '#                  #',
#             '#                  #',
#             '#                  #',
#             '#                  #',
#             '####################']
#
#     start = (2, 1)
#     end = (1, 12)
#
#     path = find_path(maze, start, end)
#     print(path)
#
# if __name__ == '__main__':
#     main()
