def fib1(Max):
    n,a,b = 0,0,1
    while n < Max:
        print(a)
        a,b = b,a + b
        n = n + 1
    return "done"
    
def fib2(Max):
    n,a,b = 0,0,1
    while n < Max:
        yield a
        a,b = b,a + b
        n = n + 1
    return "Done"
    
# fib1(6)


fib2(6)