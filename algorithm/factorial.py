def fact(n):
    if(n >= 1):
        return n * fact(n - 1)
    else:
        return 1

def fact2(n):
    if(n <= 1):
        return 1
    return n * fact(n - 1)

print(fact(5))
print(fact2(5))
