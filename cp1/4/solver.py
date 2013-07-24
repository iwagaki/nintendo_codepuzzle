#!/usr/bin/env python

from second_code import Bars
from third_code import decode_morse

bs = Bars("ITT TI I T TIii")
while True:
    prev = bs[:]
    bs.next()
    if ''.join(bs) == "ITT TI I T TIii":
        break

print decode_morse(''.join(prev))
