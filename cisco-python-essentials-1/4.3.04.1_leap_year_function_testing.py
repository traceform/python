def is_year_leap(year):
    """Returns if an year is leap or not"""
    if year < 1582:
        leap = None  # Not within the Gregorian calendar period
    else:
        if year % 4 != 0:
            leap = False  # Common year
        elif year % 100 != 0:
            leap = True  # Leap year
        elif year % 400 != 0:
            leap = False  # Common year
        else:
            leap = True  # Leap year
    return leap

def test_is_year_leap():
    sample_input =    [2000,  2015,  1999, 1996, 1580]
    expected_output = [True, False, False, True, None]
    print(">>> TESTING is_year_leap()")
    for _ in range(len(sample_input)):
        input = sample_input[_]
        print(f"{input} -> ", end='')
        output = is_year_leap(input)
        if output == expected_output[_]:
            status = "OK"
        else:
            status = "Failed"
        print(status, end='')
        #print(f" | Result: {output}", end='')
        print()
