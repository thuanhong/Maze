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

def find_path(board, player):
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
    return path


# def main():
#     maze = []
#     f = open('new', 'r')
#     maze = f.read().split('\n')[:-2]
#
#     move = find_path(maze, (1, 1), (37, 97))
#     for x, i in enumerate(maze):
#         for y in range(len(i)):
#             if (x, y) in move:
#                 print("\033[93m{}\033[00m" .format('O'), end = '')
#             else:
#                 print(maze[x][y], end='')
#         print()
#
# if __name__ == '__main__':
#     main()
