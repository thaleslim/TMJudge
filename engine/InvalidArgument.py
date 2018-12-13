# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim 

class InvalidArgument(Exception):
    '''Raise when a specific argument is missing'''
    def __init__(self, message, cause):
        self.message = message
        self.cause = cause
        super().__init__(message, cause)