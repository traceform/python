# Here's the list: 8, 10, 6, 2, 4
# 
# As you can see, the essence of this algorithm is simple: we compare the adjacent
# elements, and by swapping some of them, we achieve our goal.
# 
# Let's code into Python all the actions performed during a single pass through the
# list, and then we'll consider how many passes we actually need in order to perform
# it. We haven't explained this so far, and we'll do that a little later.
#
# How many passes do we need to sort the entire list?
#
# Note: this was done before the method .sort() was introduced

''' # Version 1
list = [8, 10, 6, 2, 4]
swapped = True # set to True to enter the loop

while swapped:
    swapped = False
    for n in range(len(list) - 1):
        if list[n] > list[n + 1]:
            list[n], list[n + 1] = list[n + 1], list[n]
            swapped = True # swap occurred

print(list)
'''

''' # Version 2
try:
    n_values = int(input("Enter the amount of elements in the list: "))
except:
    print("Invalid character.")
    quit()
    
list = []

for n in range(n_values):
    try:
        list.append(float(input(f"Enter the element nº {n + 1}: ")))
    except:
        print("Invalid element.")
        quit()

swapped = True # set to True to enter the loop

while swapped:
    swapped = False
    for n in range(len(list) - 1):
        if list[n] > list[n + 1]:
            list[n], list[n + 1] = list[n + 1], list[n]
            swapped = True # swap occurred

print(list)
'''

# Version 3
def receive_element_number(prompt: str) -> int:
    """Receives an integer value to represent the total element amount in a list"""
    while True:
        try:
            element_amount = int(input(prompt))
            return element_amount
        except ValueError:
            print("Invalid character.")

def receive_values(element_amount: int) -> list[float]:
    """Receives and stores numerical values in a list"""
    values = []

    for element in range(element_amount):
        received = False
        while not received:
            try:
                values.append(float(input(f"Enter the element nº {element + 1}: ")))
                received =  True
            except ValueError:
                print("Invalid element.")
    return values

def bubble_sort(values: list[float]) -> list[float]:
    """Sorts a list using bubble sorting"""
    swapped = True # set to True to enter the loop

    while swapped:
        swapped = False

        for i in range(len(values) - 1):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True # swap occurred
    return values

def fix_integers(values: list[float]) -> list[float]:
    """Replaces integers formatted as floating points with integer formatting"""
    for i in range(len(values)):
        if int(values[i]) == values[i]:
            values[i] = int(values[i])
    return values

if __name__ == "__main__":
    element_amount = receive_element_number("Enter the amount of elements in the list: ")
    values = receive_values(element_amount)
    values = bubble_sort(values)
    values = fix_integers(values)
    print(f"Sorted: {values}")
