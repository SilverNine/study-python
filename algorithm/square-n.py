def square_n(n):
    s = 0
    for i in range(1, n + 1):
        s = s + pow(i, 2)

    return s

print(square_n(10))

def square_n2(n):
    return n * (n + 1) * (2 * n + 1) // 6

print(square_n2(10))


