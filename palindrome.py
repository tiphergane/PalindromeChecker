#! /usr/bin/env python3

import sys
import pwn

baseString = sys.argv[1]


def reverseString(a):
    x = str(a)[::-1]
    pwn.success("nous testons le mot {}".format(x))
    testString(x, baseString)
    return


def testString(a, b):
    src = a
    tgt = b
    if str(src) == str(tgt):
        pwn.success("{} est un palindrome".format(src))
    else:
        pwn.warn("{} n'est pas un palindrome".format(src))
    return


reverseString(baseString)
