''' # Version 1
n = float(input("Type a number: ))
print(n >= 100)

'''

# Version 2
def greater_than_or_equal_to_100(n):
    return = n >= 100

def test_code():
    input = [55, 99, 100, 101, -5, +123]
    output = [False, False, True, True, False, True]
    for _ in range(len(input)):
        if greater_than_or_equal_to_100(input[_]) == output[_]:
            print(f"Success! Is {input[_]} greater than or equal to 100? {output[_]}!")
        else:
            print(f"Error! Is {input[_]} greater than or equal to 100? {output[_]}?")

#test_code()
print(greater_than_or_equal_to_100(float(input("Type a number: "))))
