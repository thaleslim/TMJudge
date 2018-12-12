class InvalidArgument(Exception):
    '''Raise when a specific argument is missing'''
    def __init__(self, message, cause, *args):
        self.message = message
        self.cause = cause
        super().__init__(message, cause, *args) 