#!/usr/bin/env python3

import sys
from random import choice

def get_sring():
    data = sys.stdin.readline()
    while data != '':
        if "HELLO" in data:
            sys.stdout.write('I AM A\n\n')
        elif 'YOU' in data:
            sys.stdout.write('OK\n\n')
            return
        data = sys.stdin.readline()

def distance(cur, goal):
    return math.sqrt((goal[0] - cur[0])**2 - (goal[1] - cur[1])**2)

def get_meal(maze):
    meal = []
    for x in range(1, len(maze)-1):
        for y in x:
            if maze[x][y] == 'o':
                meal.append([x,y])
            if maze[x][y] == 'A':
                meal.insert([x, y])
    return meal

def get_pos_nearest(pos_A, list_meal):
    if distance(pos_A, list_meal[0]) > distance(pos_A, list_meal[1]):
        return list_meal[1] if \
                distance(pos_A, list_meal[2]) > distance(pos_A, list_meal[1])
                else list_meal[2]
    else:
        return list_meal[0] if \
                distance(pos_A, list_meal[2]) > distance(pos_A, list_meal[0])
                else list_meal[2]

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

def find_path (pos_A, pos):
    pass

if __name__ == '__main__':
    get_sring()
    while True:
        maze = get_maze()
        meal = get_meal()
        start_x = maze[0][0]
        start_y = maze[0][1]
        meal.pop(0)
        get_pos_nearest([start_x, start_y], meal)
        move = find_path([start_x, start_y], get_pos_nearest([start_x, start_y], meal))
        for x in move:
            sys.stdin.write(x)
