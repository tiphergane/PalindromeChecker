#! /usr/bin/env python3

import sys
import pwn

baseString = sys.argv[1]


def reverseString(a):  # {{{
    x = str(a)[::-1]
    pwn.info("nous testons le mot {}".format(a))
    testString(x, baseString)
    return  # }}}


def testString(a, b):  # {{{
    src = a
    tgt = b
    if str(src) == str(tgt):
        pwn.success("{} est un palindrome".format(tgt))
    else:
        pwn.warn("{} n'est pas un palindrome".format(tgt))
    return  # }}}


reverseString(baseString)
