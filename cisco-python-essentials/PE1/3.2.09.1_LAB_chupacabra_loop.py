''' # Version 1
while True:
    word = input("Enter a word: ")
    if word == 'chupacabra':
        break
print("You've successfully left the loop.")
'''

# Version 2
chupacabra = None
while not chupacabra:
    word = input("Enter a word: ").strip()
    if word == 'chupacabra': chupacabra = word
print("You've successfully left the loop.")
