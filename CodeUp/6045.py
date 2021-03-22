a,b,c = input().split(' ')
s = int(a)+int(b)+int(c)
avg = round(float(s)/3, 2)
print(str(s) + " " + str('%.2f'%avg))