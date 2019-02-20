#!/usr/bin/env python3

import sys
import math
from random import choice
from find import *

def get_sring():
    data = sys.stdin.readline()
    while data != '':
        if "HELLO" in data:
            sys.stdout.write('I AM A\n\n')
        elif 'YOU' in data:
            sys.stdout.write('OK\n\n')
            return
        data = sys.stdin.readline()

# def distance(cur, goal):
#     return math.sqrt((goal[0] - cur[0])**2 - (goal[1] - cur[1])**2)

def get_meal(maze):
    meal = []
    start = ''
    for x in range(len(maze)):
        for j, y in enumerate(maze[x]):
            try:
                if y == 'o':
                    meal.append([x, j])
                if y == 'A':
                    start = [x, j]
            except:
                continue
    f = open('de', 'w')
    f.write(str(start) + '\n' + str(meal))
    return start , meal

# def get_pos_nearest(pos_A, list_meal):
#     if distance(pos_A, list_meal[0]) > distance(pos_A, list_meal[1]):
#         return list_meal[1] if \
#                 distance(pos_A, list_meal[2]) > distance(pos_A, list_meal[1]) \
#                 else list_meal[2]
#     else:
#         return list_meal[0] if \
#                 distance(pos_A, list_meal[2]) > distance(pos_A, list_meal[0]) \
#                 else list_meal[2]

def get_maze():
    output = ''
    maze = input()
    count = 0

    while count < 4:
        if ' ' not in maze:
            count += 1
        output += maze + '\n'
        maze = input()
    return output.split('\n')[2:-1]

def find(maze, pos_A, pos):
    list = find_path(maze, pos_A, pos)
    f = open('debu', 'w')
    f.write(str(list))
    current = pos_A
    output = []
    for x in list:
        if x[0] > pos_A[0]:
            output.append('MOVE DOWN')
        elif x[0] < pos_A[0]:
            output.append('MOVE UP')
        elif x[1] > pos_A[1]:
            output.append('MOVE RIGHT')
        else:
            output.append('MOVE LEFT')
        current = x
    return output

if __name__ == '__main__':
    get_sring()

    while True:
        maze = get_maze()
        start, meal = get_meal(maze)
        # f = open('de', 'w')
        # f.write(str(start))
        move = find(maze, tuple(start), tuple(meal[1]))

        for x in move:
            print(x+'\n')
