if __name__ == '__main__':

    import functools

    def info(func):
        def wrap(a, b):
            return func(a, b)

        return wrap

    @info
    def multiply(x, y):
        return x * y

    print('multiply name:', multiply.__name__)
