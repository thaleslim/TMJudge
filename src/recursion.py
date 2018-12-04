# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim

def fatorial(n: int):
    if(n < 2):
        return 1
    return n * fatorial(n-1)

print( fatorial(3), end='')