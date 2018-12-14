# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim

import pytest

@pytest.mark.parametrize("user_input, output",[
    ('',"Hello"),
])
def test_main(filename, run, user_input: str, output: str):
    if filename != None:
        assert run(filename, user_input).output == output
    else:
        pytest.fail("missing args")
