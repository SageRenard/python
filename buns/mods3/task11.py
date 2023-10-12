field = [list(input().strip()) for _ in range(3)]

winners = ['X', 'O']

for winner in winners:
    for i in range(3):
        if all(field[i][j] == winner for j in range(3)) or all(field[j][i] == winner for j in range(3)):
            print(winner)
            exit()

    if all(field[i][i] == winner for i in range(3)) or all(field[i][2 - i] == winner for i in range(3)):
        print(winner)
        exit()

print("Ничья")
