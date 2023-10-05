num = input()

zeros = 0
ones = 0
for numeral in num:
    if numeral == '0':
        zeros += 1
    elif numeral == '1':
        ones += 1
        
if zeros == ones:
    print('yes')
else:
    print('no')
