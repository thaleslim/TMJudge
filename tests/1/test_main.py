# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim 

import sys
sys.path.insert(0, "\\".join( __file__.split('\\')[0:4] ) + '\\TMJudge\\')
from engine import Tester

import pytest
#from engine.PytestConfig import *
@pytest.mark.parametrize("filename, user_input, output",[
    ("alumni/190015417/1/main.py",'',"Hello"),
    ("alumni/190015417/1/recursion.py",'3','6'),
    ("alumni/190015417/1/recursion.py",'5',"120")
])
def test_main(filename: str, user_input: str, output: str):
    # try:
    result = Tester.run(filename, user_input)
    assert result.output == output
    # except custom_error.InvalidArgument as err:
    #     print("Invalid Argument: ", err)
    #     assert 0