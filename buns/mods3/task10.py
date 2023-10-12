size = int(input())

matrix = [[i for i in range(1, size+1)] for _ in range(size)]

for line in matrix:
    print(", ".join(map(str, line)))

for i in range(size):
    for j in range(i+1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print()
for line in matrix:
    print(", ".join(map(str, line)))
