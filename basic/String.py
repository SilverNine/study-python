food = "Python's favorite food is perl"
print(food)

food = '"Python is very easy." he says.'
print(food)

food = 'Python\'s favorite food is perl'
print(food)

food = "\"Python is very easy.\" he says."
print(food)

food = "Life is too short\nYou need python"
print(food)

food = '''
Python's
favorite
food is perl'''
print(food)

food = """
Python's
favorite
food is perl"""
print(food)

head = "Python"
tail = " is fun!"
print(head + tail)

a = "Python"
print(a*2)

print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short, You need Python"
print(a[2])
print(a[-2])
print(a[0] + a[-0])
print(a[0:4])
print(a[:4])
print(a[4:])

a = "I eat %d apples." % 3
print(a)

a = "I eat %s apples." % "five"
print(a)

number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)

a = "Error is %d%%" % 98
print(a)

a = "%10s" % "hi"
print(a)

a = "%10.4f" % 3.2141415354
print(a)

a = "hobby"
print(a.count('b'))

a = "Python is best choice"
print(a.find('i'))
# print(a.index('x'))

print(a.lower())
print(a.upper())

a = " hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())
print(a.replace("h","i"))

a = "a:b:c:d"
print(a.split(":"))


a = "I ate {0} apples. I ate {1} apples.".format("1",4)
print(a)

a = "I ate {number} apples. so I was sick for {day} days."\
    .format(number=10, day=3)
print(a)

a = "{0:<10}".format("hi")
print(a)

a = "{0:^10}".format("hi")
print(a)

a = "{0:=^10}".format("hi")
print(a)

y = 3.42134234
a = "{0:0.4f}".format(y)
print(a)

a = "{0:10.4f}".format(y)
print(a)

a = "{{0}}".format()
print(a)

