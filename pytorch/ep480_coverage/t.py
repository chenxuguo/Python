def print_age(i: int) -> None:
    if i >= 0 : # pragma: no branch
        # print('you are not of age yet')
    # else:
        print(f'hello, your age is {i}')
    
        
def test_print_age(capsys):
    print_age(2)
    
    out, err = capsys.readouterr()
    assert out == 'hello, your age is 2\n'
    assert err == ''
    
    
# def test_print_age_negative_age(capsys):
    # print_age(-1)
    
    # out, err = capsys.readouterr()
    # assert out == 'you are not of age yet\n'
    # assert err == ''