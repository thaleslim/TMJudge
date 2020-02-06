# TMJudge: A Code Judge Environment
# Copyright (C) 2018 Thales Menezes @thaleslim 

class InvalidArgument(Exception):
    '''Raise when a specific argument is missing'''
    def __init__(self, message, *args):
        self.message = message
        self.args = args
        super().__init__(message, *args)

if __name__ == "__main__":
    try:
        import sys
        if len(sys.argv) > 1:
            raise InvalidArgument("Received a arg, Expected None", *sys.argv[1:])
        print('No argv were found')
    except InvalidArgument as err:
        print("Exception InvalidArgument triggered OK","Message: " + str(err),sep='\n')
    input("Pressione qualquer tecla para continuar")