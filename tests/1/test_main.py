# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim 

import pytest

@pytest.mark.parametrize("filename, user_input, output",[
    ("alumni/190015417/1/main.py",'',"Hello"),
    ("alumni/190015417/1/recursion.py",'3','6'),
    ("alumni/190015417/1/recursion.py",'5',"120")
])
def test_main(filename: str, user_input: str, output: str):
    result = run(filename, user_input)
    assert result.output == output