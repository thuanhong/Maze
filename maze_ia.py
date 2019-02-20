#!/usr/bin/env python3

import sys
import math
from random import choice
from temp import *

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
    for x in range(len(maze)):
        for j, y in enumerate(maze[x]):
            try:
                if y == 'o':
                    meal.append([x,j])
                if y == 'A':
                    meal.insert(0, [x, j])
            except:
                continue
    return meal

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

def find_path (maze, pos_A, pos):
    list = astar(maze, pos_A, pos)
    current = pos_A
    output = []

    for x in list:
        if x[0] == pos_A[0]:
            if x[1] - pos_A[1] < 0:
                output.append('MOVE LEFT')
            else:
                output.append('MOVE RIGHT')
        else:
            if x[0] - pos_A[0] < 0:
                output.append('MOVE UP')
            else:
                output.append('MOVE DOWN')
    return output

if __name__ == '__main__':
    get_sring()
    while True:
        maze = get_maze()
        meal = get_meal(maze)
        start = meal[0]
        meal.pop(0)

        # get_pos_nearest([start_x, start_y], meal[0])
        move = find_path(maze, start, meal[2])
        for x in move:
            sys.stdin.write(x)
