# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim

from collections import namedtuple
Program = namedtuple("Program", "input output globals")

import sys
import contextlib
from io import StringIO

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

@contextlib.contextmanager
def stdinIO(stdin=None):
    old = sys.stdin
    if stdin is None:
        stdin = StringIO()
    sys.stdin = stdin
    yield stdin
    sys.stdin = old

## Test Parameters
filename = "src/recursion_with_input.py"
user_input = input()
# output = int(user_input)! # "expected output"

resources_cpy = resources = {}
## Run 
with stdoutIO() as consoleout:
    with stdinIO(StringIO(user_input)) as consolein:
        resources_cpy = globals().copy()
        eval(compile(   source=open(filename).read(),
                        filename=filename,     # subject' attempt
                        mode='exec'), resources)

## Less dependency on globals() to grab subjects resources (functions and variables) with, possibly, less iterations
for _ in resources_cpy:
    if resources.get(_) != None:
        resources.pop(_)

## Stores the Subject' program test output
that    = Program( input = user_input, output = consoleout.getvalue() , globals = resources )
print(that)