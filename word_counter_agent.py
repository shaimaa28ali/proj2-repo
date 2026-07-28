# Read the text file
with open("tasks.txt", "r") as file:
    text = file.read()
 
# Ask the user for a word
word = input("Enter a word to count: ")
 
# Count how many times it appears (case-insensitive)
count = text.lower().count(word.lower())
 
# Display the result
print(f'\nThe word "{word}" appears {count} time(s).')