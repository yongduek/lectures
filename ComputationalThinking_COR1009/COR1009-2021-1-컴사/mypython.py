print('hello this is yongduek')

mystring = 'this is a string.'

print(mystring)

# print one char by one char

for char in mystring:
    print(char, ' --- ')

for darcy in mystring:
    print(darcy, ' darcy ')


length_of_mystring = len(mystring)
print('length of my string is ', length_of_mystring)

for i in range(length_of_mystring):
    print(i)

numbers = [-3, 10, -1, -2, 0, 1, 2, 99, 4, 6]
print(numbers)
for n in numbers:
    print(n, ' haha ')
print(numbers[0], numbers[2])

for i in range(3):
    print( i )

for i in range(3):
    print( i , mystring[i], mystring[i+2])

# algorithm to find a maximum of list of numbers
m = numbers[0]
if m < numbers[1]:
    m = numbers[1]
if m < numbers[2]:
    m = numbers[2]
if m < numbers[3]: m = numbers[3]
if m < numbers[4]: m = numbers[4]

m = numbers[0]
for num in numbers:
    if m < num:
        m = num

numlist = [2.5, 3, 10, 3.3, 31, 23, 7]
# maximum of numlist

m = numlist[0]
for num in numlist:
    if m < num:
        m = num
print(' --> ', m, numlist)

# -----------------------------
def maximum(alistofnumbers):
    """
    The variable alistofnumbers should be a list of numbers
    """
    m = alistofnumbers[0]
    for num in alistofnumbers:
        if m < num:
            m = num
    return m
# -----------------------------
print('!!! ', maximum(numlist), maximum(numbers))

print('maximum is ', m, ' in ', numbers)
print(max(numbers))

# max_number = maximum(numbers)


s = 'this is a string.'
listofchars = []
for c in s:
    listofchars.append(c)
print(listofchars, len(listofchars))

bb = [c for c in s]
print(bb, len(bb))
aa = list(s)
print(aa, len(aa))

unique = []
for c in s:
    if c not in unique:
        unique.append(c)
print(unique)

counts = []
print(unique, counts)
for key in unique:
    cnt = 0
    for c in s:
        if c == key:
            cnt = cnt + 1
    counts.append(cnt)
print(unique, counts)

print(s, list(s))