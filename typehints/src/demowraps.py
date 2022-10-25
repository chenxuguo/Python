if __name__ == '__main__':
    import functools
    def func_1(x: str):
        '''
        function
        :param x:
        :return:
        '''
        print('func_1', x)

    @functools.wraps(func_1)
    def demo():
        '''
        demo
        :return:
        '''
        print('demo')

    func_1('hello')
    demo()
    print('demo name:{}'.format(demo.__name__))
    print('demo doc:{}'.format(demo.__doc__))
    print('demo annotations:{}'.format(demo.__annotations__))
    print("*"*10)
    print("func_1 is demo's wrap: {}".format(func_1 is demo.__wrapped__))
