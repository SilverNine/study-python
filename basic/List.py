a = []
print(a)

a = [0, 3, 4, 5]
print(a[-1])

a = [1, 3, ['a', 'b', ['Life']]]
print(a[2][2][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[:2])
print(a[2:])

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[3][:2])

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(str(a[2]) + "hi")

a = [1, 2, 3]
a[2] = 4
print(a)
a[1] = [9, 9, 9]
print(a)
a = [1, 2, 3]
a[1:3] = [9, 9, 9]
print(a)
a[1:3] = []
print(a)

del a[1]
print(a)

a = [1, 2, 3, 4, [5, 6]]
print(a)
print(a)
a = [1, 2, 5, 6, 3, 4]
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(1))
a.insert(0, 4)
print(a)
a.remove(4)
print(a)
print(a.pop())
print(a)
print(a.pop(1))
print(a)
print(a.count(6))
a.extend([1, 2, 3, 4])
print(a)
