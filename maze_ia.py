#!/usr/bin/env python3

import sys
from find import gbfs
from time import time
from string import ascii_uppercase

def get_meal(maze):
    '''
    get coordinate of coin and player
    '''
    meal = []
    start = ''
    for x in range(len(maze)):
        for j, y in enumerate(maze[x]):
            try:
                if y == 'o':
                    meal.append([x, j])
                if y == 'A':
                    start = [x, j]
            except IndexError:
                continue
    return start, meal

def dist(start, current):
    return abs(start[0] - current[0]) + abs(start[1] - current[1])

def get_pos_nearest(pos_A, list_meal):
    '''
    get coordinate of coin nearest player# from math import sqrt
    '''
    min = list_meal[0]
    for x in list_meal:
        if dist(pos_A, x) < dist(pos_A, min):
            min = x
    return min


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
    return board


def moved(path):
    '''
    convert from coordinate to step
    '''
    f = open('debu', 'w')
    f.write(str(path))
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
            start, meal = get_meal(maze)
            end = get_pos_nearest(start, meal)
            started = time()  # start calculate time run
            move = gbfs(maze, tuple(start), tuple(end))  # find pathing
            sys.stderr.write(str(time()-started)+'\n')  # print time run
            sys.stdout.write(moved(move))  # print step
        elif "HELLO" in data:
            sys.stdout.write('I AM A\n\n')
        elif 'YOU' in data:
            sys.stdout.write('OK\n\n')

        data = sys.stdin.readline()
