# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim

import sys
sys.path.append(__file__ + '\\..\\..\\')
from engine import Tester

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--filename", action="store", default=None, help="file to be tested by runnin' the test suite"
    )
    parser.addoption(
        "-F", action="store", default=None, help="equal to --filename"
    )

@pytest.fixture
def filename(request):
    '''
        The file to be tested.
        pass filename according to open() restrictions
        NOTE: remember the cmd directory your sending queries from
    '''
    filename = request.config.getoption("--filename")
    if filename != None:
        return filename
    filename = request.config.getoption("-F")
    if filename != None:
        return filename
    pytest.fail("Missing arg filename")

@pytest.fixture
def run():
    def __run__(filename, *user_input):
        return Tester.run(filename, *user_input)
    return __run__

@pytest.fixture
def log():
    def __log__(message, expected_output, captured_output, *args):
        return Tester.log(message, expected_output, captured_output, *args)
    return __log__