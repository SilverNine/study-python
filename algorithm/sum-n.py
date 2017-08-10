def sum_n(n):
    s = 0
    for i in range(1, n + 1):
        #print(i)
        s = s + i

    return s

def sum_n2(n):
    return n * (n + 1) // 2

print(sum_n(10))
print(sum_n(100))

print(sum_n2(10))
print(sum_n2(100))