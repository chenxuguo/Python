if __name__ == '__main__':

    import functools

    def insert_time(func):
        def info(func):
            @functools.wraps(func)
            def wrap(a, b):
                return func(a, b)

            return wrap
        if isinstance(func, float):
            print('FUNC=', func)
            return info
        else:
            return info(func)

    @insert_time(0.5)
    def multiply(x, y):
        return x * y

    print(multiply(1.0, 2.0))
    print('multiply name:', multiply.__name__)
