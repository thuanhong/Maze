#!/usr/bin/env python3
import sys

def get_string(str):
    take = input()
    while str not in take:
        take = input()

    take = input()
    return True

def get_maze():
    output = ''
    maze = input()
    count = 0
    while count < 3:
        if ' ' not in maze:
            count += 1
        output += maze + '\n'
        maze = input()
    print(output)


if __name__ == '__main__':
    if get_string('HELLO'):
        print('I AM A\n')
    if get_string('YOU'):
        print('OK\n')
    get_maze()
