def pot(x, n):
    if n == 0:
        return 1
    elif n %2 == 0:
        p = pot(x, n//2)
        return p*p
    else:
        p = pot(x, n//2)
        return p*p*x
