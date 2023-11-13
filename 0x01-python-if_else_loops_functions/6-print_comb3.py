#!/usr/bin/python3
for x in range(0, 90):
    if (x / 10 != x % 10 and x / 10 < x % 10):
        print("{:02}".format(x), end=', ')
print("{:02}".format(x))
