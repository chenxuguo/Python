class C():
    def __del__(self):
        raise AssertionError('Oh, No!')
