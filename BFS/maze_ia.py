#!/usr/bin/env python3
import sys
from find import *
from time import time


def get_A(maze):
    '''
    get coordinate of coin and player
    '''
    for x in range(len(maze)):
        for j, y in enumerate(maze[x]):
            try:
                if y == 'A':
                    return (x, j)
            except IndexError:
                continue
    return 0, 0


def get_maze():
    '''
    get maze from VM
    '''
    board = []
    while True:
        data = sys.stdin.readline()
        if data[0] != '#':
            break
        board.append(data)
    maze = []
    for x in board:
        temp = []
        for y in x:
            temp.append(y)
        maze.append(temp)
    return maze


def moved(path):
    '''
    convert from coordinate to step
    '''
    if path[1][0] - path[0][0] == 1:
        return 'MOVE DOWN\n\n'
    elif path[1][0] - path[0][0] == -1:
        return 'MOVE UP\n\n'
    elif path[1][1] - path[0][1] == 1:
        return 'MOVE RIGHT\n\n'
    elif path[1][1] - path[0][1] == -1:
        return 'MOVE LEFT\n\n'


if __name__ == '__main__':
    data = sys.stdin.readline()
    while data != '':
        if 'MAZE' in data:
            maze = get_maze()
            start = get_A(maze)
            started = time()  # start calculate time run
            move = find_path(maze, tuple(start))  # find pathing
            sys.stderr.write(str(time()-started)+'\n')  # print time run
            f = open('debu', 'w')
            f.write(str(move))
            sys.stdout.write(moved(move))  # print step
        elif "HELLO" in data:
            sys.stdout.write('I AM A\n\n')
        elif 'YOU' in data:
            sys.stdout.write('OK\n\n')

        data = sys.stdin.readline()
