import re;


class NonRomanNumberError(ValueError): pass


def from_roman(roman):
    pattern = '''
    ^                   # begining of string
    M{0,3}              # thousands
    (CM|CD|D?C{0,3})    # hundreds
    (XC|XL|L?x{0,3})    # tens
    (IX|IV|V?I{0,3})    # ones
    $                   # end of string
    '''
    if re.search(pattern, roman):
        re.sub()
        return n
    else:
        raise NonRomanNumberError('number is not a roman number!')
