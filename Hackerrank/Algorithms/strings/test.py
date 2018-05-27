#!/bin/python

import sys


def ans(s):
    return len(set(s))

n = int(raw_input().strip())
for a0 in xrange(n):
    s = raw_input().strip()
    print ans(s)
