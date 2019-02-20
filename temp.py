#!/usr/bin/env python3
import sys
import collections
import string


def player_coordinate(board, name='A'):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == name:
                player = [row, col]
    return player


def return_board():
    board = []
    while True:
        k = sys.stdin.readline()
        if k[0] != '#':
            break
        board.append(k)
    return board


def return_path(board, player):
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


def move(path):
    if path[1][0] - path[0][0] == 1:
        return 'MOVE DOWN\n\n'
    elif path[1][0] - path[0][0] == -1:
        return 'MOVE UP\n\n'
    elif path[1][1] - path[0][1] == 1:
        return 'MOVE RIGHT\n\n'
    elif path[1][1] - path[0][1] == -1:
        return 'MOVE LEFT\n\n'


if __name__ == "__main__":
    s = sys.stdin.readline()
    while s != '':
        if 'HELLO' in s:
            sys.stdout.write('I AM A\n\n')
        elif 'YOU' in s:
            number_of_players = []
            letter = s[-2]
            number_of_players.append(letter)
            sys.stdout.write('OK\n\n')
        elif 'MAZE' in s:
            stt = 0
            board = return_board()
            player = player_coordinate(board, number_of_players[stt])
            path = return_path(board, player)
            sys.stdout.write(move(path))
            if stt == len(number_of_players) - 1:
                stt = 0
            else:
                stt += 1
        s = sys.stdin.readline()
