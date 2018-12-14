# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim

import pytest

def test_recursive(filename, run, log):
    assert 0

@pytest.mark.parametrize("user_input, output",[
    ('2',"0 3"),
    ('1',"0 2"),
    ('0',"0 0")
])
def test_main(filename, run, log, user_input: str, output: str):
    if filename != None:
        returns = run(filename, user_input)
        # if returns.output != output:
        #     message = "Something went wrong"
        #     try:
        #         path = filename.split('\\')
        #         name = path[path.index('alumni')+1]
        #         log( message, output, returns.output, name + ".txt")
        #     except IndexError:
        #         log( message, output, returns.output, "log_from_Unknown.txt")
        assert returns.output == output
    else:
        pytest.fail("missing args")
