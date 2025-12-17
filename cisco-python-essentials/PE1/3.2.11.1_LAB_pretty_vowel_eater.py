'''
# Version 1
user_word = input("Enter a word: ")
alt_word = user_word.upper()
vowels = ['A','E','I','O','U']

word_without_vowels = ''
for letter in alt_word:
    if letter in vowels:
        continue
    word_without_vowels += letter
print(word_without_vowels)

'''

# Version 2
try:
    user_word = input("Enter a word: ")
    alt_word = user_word.upper()
    vowels = ['A','E','I','O','U']

    word_without_vowels = ''
    for letter in alt_word:
        if letter in vowels:
            continue
        word_without_vowels += letter
    print(word_without_vowels)
except KeyboardInterrupt:
    print("\nProgram terminated.")
except:
    print("Error!")
