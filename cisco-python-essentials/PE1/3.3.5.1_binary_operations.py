var =    0b11111 # 0001 1111 = 31
target =  0b1000 # 0000 1000 =  8

print(f"{bin(var)} ← Current value. ", end='')

# Check state of bit
if var & target:
    print(f"Bit {target} is already set")
else:
    print(f"Bit {target} is reset")

# Reset target bit
var = var & ~target
print(f"{bin(var)} ← bit reset")

# Set target bit
var = var | target
print(f"{bin(var)} ← bit set")

# Flip target bit
var = var ^ target
print(f"{bin(var)} ← bit flipped")
