from random import randint

gay = int(input("Please enter a number: "))
matrix = [[randint(0,99) for _ in range(gay)] for _ in range(gay)]

print("Here is randomly generated matrix:")
for y in matrix:
    for x in y:
        print(f"{x} " if x >= 10 else f"{x}  ", end="")
    print()

diagonal_dif = 0

for n in range(gay):
    diagonal_dif = diagonal_dif + matrix[n][n] - matrix[n][-(n+1)]


print(f"The diagonal dif is: {abs(diagonal_dif)}")
