# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim

import pytest

@pytest.mark.parametrize("user_input, output",[
    ('1',"0 2"),
])
def test_main(filename, run, log, user_input: str, output: str):
    if filename != None:
        returns = run(filename, user_input)
        if returns.output != output:
            message = "Something went wrong" + returns.output 
            try:
                path = filename.split('\\')
                name = path[path.index('alumni')+1]
                log( message, name + ".txt")
            except IndexError:
                log( message, "log_from_Unknown.txt")
    else:
        pytest.fail("missing args")
