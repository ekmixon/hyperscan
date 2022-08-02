#!/usr/bin/env python

from itertools import *
from optparse import OptionParser

LIMITED_ALPHABET = "abc[](){}*?+^$|:=.\\-"

parser = OptionParser()
parser.add_option("-d", "--depth",
                  action="store", type="int", dest="depth", default=200,
                  help="Depth of generation (akin to maximum length)")

parser.add_option("-f", "--full",
                  action="store_true", dest="full", default=False,
                  help="Use a full character set including unprintables")

parser.add_option(
    "-l",
    "--limited",
    action="store_true",
    dest="limited",
    default=False,
    help=f"Use a very limited character set: just {LIMITED_ALPHABET}",
)


(options, args) = parser.parse_args()
if len(args) != 0:
    parser.error("incorrect number of arguments")

if options.full:
    crange = range(256)
    crange.remove(ord('\n'))
elif (options.limited):
    crange = [ ord(c) for c in LIMITED_ALPHABET ]
else:
    crange = range(32, 127)

srange = [ chr(c) for c in crange ]

for i, x in enumerate(product(srange, repeat = options.depth)):
    line = f"{str(i)}:/" + "".join(x) + "/"
    line = str(i) + ":/" + "".join(x) + "/"
