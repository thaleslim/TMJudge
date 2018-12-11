# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim

import pytest

import sys
from collections import namedtuple

sys.path.append('src/')
from recursion import *
# import importlib
# importlib.import_module('recursion')
# locals()['fatorial'] = sys.modules['recursion'].fatorial

Program = namedtuple("Program", "input output locals globals")

# import subprocess as console
# def test_main():
#     assert console.check_output('python src/main.py', timeout=1, shell=True).decode('utf-8') == 'hello'

@pytest.mark.parametrize("filename, output",[
    ("src/main.py","Hello"),
    ("src/recursion.py",'6')
])
def test_main(filename: str, output: str, user_input: str = ''):
    __globals__ = {}
    __locals__ = {}

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

    # @contextlib.contextmanager
    # def stdinIO(stdin=None):
    #     old = sys.stdin
    #     if stdin is None:
    #         stdin = StringIO()
    #     sys.stdin = stdin
    #     yield stdin
    #     sys.stdin = old

    with stdoutIO() as consoleout:
        # with stdinIO(StringIO(user_input)) as consolein:
        __globals__ = globals().copy()
        __locals__  = locals().copy()
        eval(compile(   source=open(filename).read(),
                        filename=filename,     # subject' attempt
                        mode='exec'))

    _globals_ = {}
    for _ in globals():
        if __globals__.get(_) == None and _[0] != '_':
            _globals_[_] = globals()[_]
    
    _locals_ = {}
    for _ in locals():
        if __locals__.get(_) == None and _[0] != '_':
            _locals_[_] = locals()[_]

    # stores the output
    that    = Program( input = user_input, output = consoleout.getvalue() , locals=_locals_, globals = _globals_ )
    print(that)
    assert that.output == output