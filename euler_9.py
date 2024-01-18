for a in range(1,1001):
    for b in range(1,1001):
        x = a**2 + b**2
        c = 1000-a-b
        y = c**2
        if x == y:
            print(a*b*c)
            exit()