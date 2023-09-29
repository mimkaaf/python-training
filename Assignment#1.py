# Ask the name of the player and print a greeting message with the name in capital case
# As users to enter the number of letters in their name
# Compare this number with the character lenghts and print True or False accordingly
userName = input("Enter your name: ")
print(f"Good Morning {userName.upper()}")
lettersNumber = int(input("How many letters are in your name?"))
print(len(userName) == lettersNumber)