#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        if x == 4 and y == 7:
            print('89')
        else:
            print('{}{}, '.format(x, y), end='')
