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

def day_of_year(year, month, day):
    """Returns the ordinal number of the day in a year"""
    # Checking if both year, month and day are valid
    month_days = days_in_month(year, month)
    if year > 1582 and 1 <= month <= 12 and 1 <= day <= month_days:
        # Counting all of the days up until the chosen day
        ord_day = 0  # Ordinal day
        for _ in range(1, month):
            ord_day += days_in_month(year, _)
        ord_day += day
        return ord_day
    else:
        return None

def test_day_of_year():
    sample_years = [  2000, 2001, 2000, 2001]
    sample_months = [   12,    1,    2,    2]
    sample_days = [     31,    1,   29,   29]
    expected_output = [366,    1,   60, None]
    print(">>> TESTING day_of_year()")
    for _ in range(len(expected_output)):
        year = sample_years[_]
        month = sample_months[_]
        day = sample_days[_]
        print(f"{year} {month} {day} -> ", end='')
        output = day_of_year(year, month, day)
        if output == expected_output[_]:
            status = "OK"
        else:
            status = "Failed"
        print(status, end='')
        #print(f" | Result: {output}", end='')
        print()        

test_day_of_year()
