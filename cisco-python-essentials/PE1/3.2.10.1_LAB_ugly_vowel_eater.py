''' # Version 1
user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in ['A','E','I','O','U']:
        continue
    print(letter)

'''

'''
# Version 2
user_word = input("Enter a word: ").upper()
vowels = ['A','E','I','O','U']

for letter in user_word:
    if letter in vowels:
        continue
    print(letter)

'''

# Version 3
try:
    user_word = input("Enter a word: ")
    alt_word = user_word.upper()
    vowels = ['A','E','I','O','U']
    
    for letter in alt_word:
        if letter in vowels:
            continue
        print(letter)
except KeyboardInterrupt:
    print("\nProgram terminated.")
except:
    print("Something went wrong!")
