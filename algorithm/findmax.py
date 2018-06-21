def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

v = [17,1,2,3,19,20,30,99,92,12]
print(find_max(v))
