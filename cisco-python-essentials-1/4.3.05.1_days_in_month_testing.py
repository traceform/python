def is_year_leap(year):
    """Returns if a year is leap or not"""
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

def days_in_month(year, month):
    """Returns the amount of days in a month of a given year"""
    # If either the year or the month is invalid
    if year < 1582 or month < 1 or month > 12:
        return None
    # If it's february on a leap year
    if month == 2 and is_year_leap(year):
        return 29
    else:
        # Only load list into memory after leap check is done
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month - 1]

def test_is_year_leap():
    sample_input = [   2000,  2015,  1999, 1996, 1580]
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

def test_days_in_month():
    sample_years = [ 1900, 2000, 2015, 2016, 1999, 1996, 1580, 1987, 1945]
    sample_months = [   2,    2,    2,    2,    1,   11,    5,    0,   13]
    expected_output = [28,   29,   28,   29,   31,   30, None, None, None]
    print(">>> TESTING days_in_month()")
    for _ in range(len(sample_years)):
        year = sample_years[_]
        month = sample_months[_]
        print(f"{year} {month} -> ", end='')
        output = days_in_month(year, month)
        if output == expected_output[_]:
            status = "OK"
        else:
            status = "Failed"
        print(status, end='')
        #print(f" | Result: {output}", end='')
        print()

test_is_year_leap()
print()
test_days_in_month()
