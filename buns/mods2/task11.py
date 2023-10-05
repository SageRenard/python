nums = input()
check = ''
change = nums.replace(' ', '')
for i in range(len(change)):
    check = change[:i] + change[i + 1:]
    if change[i] in check:
        print(True)
        break
    if change[i] not in check:
        print(False)
        break
