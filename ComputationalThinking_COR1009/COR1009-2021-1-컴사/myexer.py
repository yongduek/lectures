import numpy

alist = ['a', 'b', 1, 2, 10, 'a', 'b', 'b', 'a', 1, 1, 1, 2]

u = numpy.unique(alist)
print(u)


string = 'this is a string.'
print(string, type(str))

# convert a string to list

listofchars = []
for c in string:
    listofchars.append(c)
print(listofchars)

unique_items = []
# for c in string:
#     if c in unique_items:
#         pass
#     else:
#         unique_items.append(c)
for c in string:
    if c not in unique_items:
        unique_items.append(c)
#
print(unique_items)

# count the unique items
print(unique_items[0])
ui = unique_items[0]
cnt = 0
for c in string:
    if ui == c:
        cnt = cnt + 1
print(f'unique item [{ui}] appears {cnt} times.')

counts = []
for ui in unique_items:
    print('before: ', counts)
    cnt = 0
    for c in string:
        if ui == c:
            cnt = cnt + 1
    counts.append(cnt)
    print('after: ', counts)
#
print(unique_items, '\n', counts)

counts = []
for index, ui in enumerate(unique_items):
    print('before: ', index, counts)
    cnt = 0
    for c in string:
        if ui == c:
            cnt = cnt + 1
    counts.append(cnt)
    print('after: ', index, counts)
#
print(unique_items, '\n', counts)

print('string: ', string)
for iiii, c in enumerate(string):
    print(iiii, c)

def unique(array):
    # 1. find unique items in the array
    # 2. counts of them
    unique_items = []
    counts = []
    # do stuff
    # go home and do it yourself. # submit your code to eclass.sogang.ac.kr
    #
    return unique_items, counts
#

uis, counts = unique(string)
print(uis, counts)
