# Implement Dooz for only a single round
# Use "x" for user1 and "o" for user2
# user1 starts the game and enters the row first and then the column
# user2 does the same
# Print the Dooz table; empty cells with " "

#Initialize the board
#row1 = [" ", " ", " "]
#row2 = [" ", " ", " "]
#row3 = [" ", " ", " "]

board = {
    "row1" : [" ", " ", " "],
    "row2" : [" ", " ", " "],
    "row3" : [" ", " ", " "]
}
#Pre-set the users
user1 = "x"
user2 = "o"

#Tracing users inputs
user1_input = []
user2_input = []

# Get the input from user 1 (first row and then column)
row_number = int(input("Enter your row number: "))
column_number = int(input("Enter your column number: "))

user1_input.append(row_number)
user1_input.append(column_number)

# Update the board
row_number == 1 

# Get the input from user 2 (first row and then column)
row_number = int(input("Enter your row number: "))
column_number = int(input("Enter your column number: "))

user2_input.append(row_number)
user2_input.append(column_number)


# Initialize the board
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

# Pre-set the users
user1 = "x"
user2 = "o"

# Get the input from users (first row and then column)
row_number = int(input("Enter your row number (1, 2, or 3): ")) - 1  # Subtract 1 to convert to list index
column_number = int(input("Enter your column number (1, 2, or 3): ")) - 1  # Subtract 1 to convert to list index

# Check if the selected cell is empty, and update the board if it is
if row_number in [0, 1, 2] and column_number in [0, 1, 2]:
    if row_number == 0:
        row1[column_number] = user1
    elif row_number == 1:
        row2[column_number] = user1
    elif row_number == 2:
        row3[column_number] = user1

# Print the updated Dooz table
print("Updated Dooz Table:")
print(" ".join(row1))
print(" ".join(row2))
print(" ".join(row3))
