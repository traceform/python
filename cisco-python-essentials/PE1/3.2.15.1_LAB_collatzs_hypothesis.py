# Version 1
steps = 0

try:
    # Step 1: take any non-negative and non-zero integer number and name it c0
    c0 = int(input("Type any non-negative non-zero integer number: "))
    if c0 < 1:
        raise ValueError
except ValueError:
    print("Only non-negative non-zero integer numbers allowed!")

# Step 4: if c0 ≠ 1, go back to point 2
while c0 != 1:
    # Step 2: if it's even, evaluate a new c0 as c0 ÷ 2
    if c0 % 2 == 0:
        c0 //= 2
    # Step 3: otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1
    else:
        c0 = 3 * c0 + 1

    print(c0)
    steps += 1

print(f"steps = {steps}")
