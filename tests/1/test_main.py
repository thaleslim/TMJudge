# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim 

import sys
sys.path.append(__file__ + '\\..\\..\\..\\')
from engine import Tester

import pytest

@pytest.mark.parametrize("user_input, output",[
    ('',"Hello"),
])
def test_main(filename, user_input: str, output: str):
    if filename != None:
        result = Tester.run(filename, user_input)
        assert result.output == output
    else:
        pytest.fail("missing args")
