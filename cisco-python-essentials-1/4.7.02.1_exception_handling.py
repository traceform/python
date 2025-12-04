try:
    value = int(input("Enter a natural number: "))
    if value < 0:
        raise ValueError
    print(f"The reciprocal of {value} is {1/value}")
except ValueError:
    print("Error! You must enter a non-negative integer.")
except ZeroDivisionError:
    print("Error! Zero is not allowed!")
except:
    print("Something went wrong.")
