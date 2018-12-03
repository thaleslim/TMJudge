# TMJudge: A Code Judge Environment
# Copyright (C) 2018  Thales Lima Menezes @thaleslim

import pytest
import subprocess as console

def test_main():
    assert console.check_output('python src/main.py', timeout=1, shell=True).decode('utf-8') == 'hello'