def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)

print(gcd(1293, 534))
print(gcd(534, 1293))
