string = ' '.join(input("Type something: ").strip().split())
if 'Spathiphyllum' in string:
    print("Yes - Spathiphyllum is the best plant ever!")
elif 'spathiphyllum' in string:
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {string}!")
