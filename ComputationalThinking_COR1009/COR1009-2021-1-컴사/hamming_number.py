def comp(nth):
    hnum_list = [1]
    nn = 2
    while len(hnum_list) < nth:
        n = nn
        while n % 2 == 0:
            n = n // 2
        while n % 3 == 0:
            n = n // 3
        while (n % 5 == 0):  # common divisor
            n = n // 5
        
        if n == 1:
            hnum_list.append(nn)
            
        nn += 1
    return hnum_list
#

def common(n, nums):
    """ check if n is a common multiple of any of nums """
    for k in nums[::-1]:
        while n % k == 0:
            n = n // k 
            if n == 1: return True
    return False

def comp2(nth):
    hnum_list = [1, 2, 3, 4, 5]
    nn = 6
    while len(hnum_list) < nth:
        n = nn
        if common(n, hnum_list[1:]):
            hnum_list.append(nn)
            
        nn += 1
    return hnum_list[:nth]
#

def comp3(nth):
    n = nth
    h=[1]        
    i=j=k=0
    # while nth >= 0:
    while len(h) < nth:
        # print (h[-1])
        while h[i]*2<=h[-1]:
            i+=1
        while h[j]*3<=h[-1]:
            j+=1
        while h[k]*5<=h[-1]:
            k+=1
        h.append(min(h[i]*2,h[j]*3,h[k]*5))
        n -= 1    
    #
    # print('H: ', h)
    return h #[:nth]

def hamming(n):
    """ return the n-th hamming number """
    hl = comp3(n)
    return hl[-1]

if __name__ == "__main__":
    for n in range(1, 20):
        print(f'hamming({n}) ', hamming(n))