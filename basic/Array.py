x={'data1':[1,2,3,4],'data2':['a','b','c','d']}

for xx in x['data1']:
    print(xx)


if(x['data1'] != False):
    print(x['data2'])


def eval(x,y):
    return x+y, x-y, x*y, x/y

print(eval(10,20)[0])
