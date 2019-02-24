#!/usr/bin/env python3
'''
This is file handle main
Copyright 2019
Hong Thanh Thuan
'''
import sys
from time import time
from find import find_path


def get_pos_player(maze):
    '''
    get coordinate of player
    '''
    for row, _ in enumerate(maze):
        for column, char in enumerate(maze[row]):
            if char == 'A':
                return (row, column)
    return 0, 0


def lost_way(maze, player_pos):
    '''
    random way if IA not found continue
    '''
    for new in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        index_1 = player_pos[0] + new[0]
        index_2 = player_pos[1] + new[1]
        if maze[index_1][index_2] != '#':
            return change_move([(player_pos), (index_1, index_2)])



def get_maze():
    '''
    get maze from VM
    '''
    board = []
    while True:  # get maze from VM linux
        line = sys.stdin.readline()
        if line[0] != '#':
            break
        board.append(line)

    maze = []
    for row in board:  # change maze become list
        temp = []
        for char in row:
            temp.append(char)
        maze.append(temp)
    return maze


def change_move(path):
    '''
    convert from coordinate to step
    '''
    if path[1][0] - path[0][0] == 1:
        return 'MOVE DOWN\n\n'
    if path[1][0] - path[0][0] == -1:
        return 'MOVE UP\n\n'
    if path[1][1] - path[0][1] == 1:
        return 'MOVE RIGHT\n\n'
    if path[1][1] - path[0][1] == -1:
        return 'MOVE LEFT\n\n'


if __name__ == '__main__':
    data = sys.stdin.readline()
    while data != '':
        if 'MAZE' in data:
            the_maze = get_maze()
            start = get_pos_player(the_maze)
            steps = find_path(the_maze, tuple(start))  # find pathing
            if steps:
                sys.stdout.write(change_move(steps))  # print step
            else:
                sys.stdout.write(lost_way(the_maze, start))
        elif "HELLO" in data:
            sys.stdout.write('I AM A\n\n')
        elif 'YOU' in data:
            sys.stdout.write('OK\n\n')

        data = sys.stdin.readline()
