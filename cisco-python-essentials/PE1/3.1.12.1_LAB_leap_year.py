''' # Version 1
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        msg = "Common year"
    elif year % 100 != 0:
        msg = "Leap year"
    elif year % 400 != 0:
        msg = "Common year"
    else:
        msg = "Leap year"

'''

# Version 2
def is_leap_year(year):
    if year < 1582:
        msg = "Not within the Gregorian calendar period"
    else:
        if year % 4 != 0:
            msg = "Common year"
        elif year % 100 != 0:
            msg = "Leap year"
        elif year % 400 != 0:
            msg = "Common year"
        else:
            msg = "Leap year"
    return msg

def test_code():
    sample_input = [2000, 2015, 1999, 1996, 1580]
    expected_output = ["Leap year", "Common year", "Common year", "Leap year", "Not within the Gregorian calendar period"]
    for _ in range(len(sample_input)):
        input = sample_input[_]
        output = is_leap_year(input)
        if output == expected_output[_]:
            print(f"Success! {input} is {output}")
        else:
            print(f"Error! {input} is {output}")

#print(is_leap_year(int(input("Enter a year: "))))
test_code()
