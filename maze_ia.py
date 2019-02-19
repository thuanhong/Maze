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
    for x in range(len(maze)):
        for y in x:
            if maze[x][y] == '!' or maze[x][y] == 'o':
                meal.append([x,y])
            if maze[x][y] == 'A':
                meal.insert([x, y])
    return meal

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


if __name__ == '__main__':
    get_sring()
    while True:
        maze = get_maze()
        meal = get_meal()
        start_x = maze[0][0]
        start_y = maze[0][1]
        
