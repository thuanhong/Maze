#!/usr/bin/env python3

import sys
from random import choice

def get_maze():
    output = ''
    maze = input()
    count = 0

    while count < 3:
        if ' ' not in maze:
            count += 1
        output += maze + '\n'
        maze = input()

    return output.split('\n')[2:-1]


if __name__ == '__main__':
    data = sys.stdin.readline()

    while data != '':
        if "HELLO" in data:
            sys.stdout.write('I AM A\n')
        elif 'YOU' in data:
            sys.stdout.write('OK\n')

        data = sys.stdin.readline()

    ls = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    while True:
        print('MOVE ' + choice(ls) + '\n')
