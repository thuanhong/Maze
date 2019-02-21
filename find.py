from math import sqrt
import sys
import collections
import string

class node():
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos

    def __eq__(self, other):
        return self.pos == other.pos

def distance(cur, goal):
    return sqrt((goal[0] - cur[0])**2 + (goal[1] - cur[1])**2)

def find_path(board, player, end):
    # declare start point vs end point
    # start_node = node(None, start)
    # end_node = node(None, end)
    #
    # # create two list emppty
    # open_list = []
    # closed_list = []
    #
    # open_list.append(start_node)
    # # handle main
    # while len(open_list) > 0:
    #     current_pos = open_list[0]
    #     current_index = 0
    #
    #     for index, item in enumerate(open_list): # find the point have coordinate nearest end_node
    #         if distance(current_pos.pos, end_node.pos) > distance(item.pos, end_node.pos):
    #             current_pos = item
    #             current_index = index
    #
    #     open_list.pop(current_index)
    #     closed_list.append(current_pos)
    #
    #     if current_pos == end_node: # output path if find end_node
    #         path = []
    #         current = current_pos
    #         while current is not None:
    #             path.append(current.pos)
    #             current = current.parent
    #         return path[::-1]
    #
    #     for new in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # find 4 way to get position
    #         temp_node = (current_pos.pos[0] + new[0], current_pos.pos[1] + new[1])
    #         if maze[temp_node[0]][temp_node[1]] == '#':
    #             continue
    #         new_node = node(current_pos, temp_node)
    #         if new_node not in closed_list:
    #             open_list.append(new_node)


    queue = collections.deque([[player]])
    seen = list(player)
    while queue:
        path = queue.popleft()
        row, col = path[-1]
        if board[row][col] == '!' and len(path) <= 20:
            return path
        elif board[row][col] == 'o':
            return path
        for y, x in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
            if board[y][x] != '#' and \
               board[y][x] not in string.ascii_uppercase and \
               [y, x] not in seen:
                queue.append(path + [[y, x]])
                seen.append([y, x])
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for r, c in move:
        pr = r + player[0]
        pc = c + player[1]
        if board[pr][pc] != '#' and \
           board[pr][pc] not in string.ascii_uppercase:
            path = [player, [pr, pc]]
            break
