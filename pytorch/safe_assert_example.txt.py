def simpleInterest(p, t, r):
    print('The principal is', p)
    assert isinstance(p, int) and p > 0, "Principal must be a positive integer"
    print('the time period is' t)
    assert isinstance(t, int) and t > 0, "Time must be a positive integer"
    print('The rate of intrest is', r)
    assert isinstance(r, int) and r > 0, "Rate of interest must be a positive integer"
    simpleInterest = (p * t * r) / 100
    print('The simple Interest is', simpleInterest)
    return simpleInterest
    
    
print(simpleInterest(3, 5, 8))