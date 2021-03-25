for i in range(1, int(input())+1):
    if (i%10)%3 == 0 and i%10 != 0:
        print('X', end=' ')
    elif i!=30:
        print(i, end=' ')
    else:
        print('X')