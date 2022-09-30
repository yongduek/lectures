
done = False
while not done:
    n = int(input())
    if n == 0: break
    
    r = [3 for _ in range(32)]
    for _ in range(n):
        sl = input().split()
        if sl[0] == 'SET':
            r[int(sl[1])] = 1
        elif sl[0] == 'CLEAR':
            r[int(sl[1])] = 0
        elif sl[0] == 'OR':
            i = int(sl[1])
            b1 = r[i]
            b2 = r[int(sl[2])]
            if b1 == 1 or b2 == 1:
                r[i] = 1
            elif b1 == 0 and b2 == 0:
                r[i] = 0 
            else:
                r[i] = 3
        elif sl[0] == 'AND':
            i = int(sl[1])
            b1 = r[i]
            b2 = r[int(sl[2])]
            if b1 == 0 or b2 == 0:
                r[i] = 0
            elif b1 == 1 and b2 == 1:
                r[i] = 1
            else:
                r[i] = 3
        #
    #
    o = ''.join([str(k) for k in r[::-1]]).replace('3', '?')
    print(o)