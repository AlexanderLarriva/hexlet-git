def fib(arg):
    Summ = 0
    for i in range(0,arg):
        Summ = Summ + (i+1)
    return Summ


print(fib(10))