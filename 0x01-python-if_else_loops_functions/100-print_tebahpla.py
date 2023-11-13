#!/usr/bin/python3
for x in range(-122, -96):
    x = -x
    if (x % 2 == 1):
        x -= 32
    print("{:c}".format(x), end='')
