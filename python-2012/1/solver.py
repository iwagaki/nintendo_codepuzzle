#!/usr/bin/env python

i = 0

while True:
    if pow(i, 17) % 3569 == 915:
        print i
        break
    i += 1
