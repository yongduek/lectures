def count_clean(bowls, plates, dishes):
    for dish in dishes:
        if dish == 1:
            bowls -= 1
        elif dish == 2:
            if bowls > 0:
                bowls = bowls - 1
            elif plates > 0:
                plates = plates - 1
            else:
                bowls = bowls - 1 
        #
    #
    if bowls < 0:
        return -bowls
    else:
        return 0
#

print(count_clean(1,1, [1,2,1]))

print(count_clean(3,1, [1,1,1,1]))