# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim 

# Model to store general test suite' result information
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

def run(filename: str, user_input: str):
    '''
        Executes the code from <filename>.py passing <user_input> as input().
        Returns  Program() with general information about the code execution. 
    '''
    # resources is globals() from <filename>.py
    resources_cpy = resources = {}
    
    open_file = open(filename)
    # consoleout is stdout from <filename>.py  
    with stdoutIO() as consoleout:
        with stdinIO(StringIO(user_input)):
            resources_cpy = globals().copy()
            eval(compile(   source=open_file.read(),
                            filename=filename,
                            mode='exec' ), resources)
    open_file.close()
    # filters unnecessary globals() items
    for _ in resources_cpy:
        if resources.get(_) != None:
            resources.pop(_)
    # Subject' program test output
    return Program( input = user_input, output = consoleout.getvalue() , globals = resources )

def log(error_message: str, logfile: str = "log.txt", fancy = False):
    '''
        Appends a error_message to a error logging file.
        :return: <logfile> or None, if fails
    '''
    log = open(logfile, 'a')
    if log.writable():
        if log.write(error_message) != len(error_message):
            try:
                log.close()
            except:
                return None
        return logfile
    return None