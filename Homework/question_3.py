# Input the table size
board = int(input("Input Addition Table Size smaller 10: "))

# Print the table
print("Addition Table")
print("-------------------------------------------------------")
#for function to print the board
for i in range(1, board + 1):
    for j in range(1, board + 1):
        sum = i + j
        print(f"{i} + {j} = {sum}", end=" ")
    print()
print("-------------------------------------------------------")
