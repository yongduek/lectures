def between(a,b):
    """
    returns a2b = [a, a+1, a+2, ..., b]
    """
    a2b = []
    for i in range(a, b+1):
        if i >= a:
            a2b.append(i)
    #
    return a2b
#
r = between(1, 5)
print(r) # [1, 2, 3, 4, 5]

r2 = between(5, 10)
print('r2: ', r2)

for i in range(100, 105, 2):
    print(i)

a=4
b=7
a2b = [i for i in range(a, b+1)]
print(a2b)

alist = ['hllow', 2.5]
atuple = ('hellow', 5.5)

print(alist, atuple)

alist[0] = 'world'      # mutable
print('alist: ', alist)

atuple[0] = 'good' # immutable
print(atuple)