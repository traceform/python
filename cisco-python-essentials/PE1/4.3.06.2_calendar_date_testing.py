# This calculates a calendar date insteadf of calculating the ordinal number of the day in a year
# because the lab activity statement was confusing

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
    """Returns the written date"""
    # Checking if both year, month and day are valid
    month_days = days_in_month(year, month)
    if year > 1582 and 1 <= month <= 12 and 1 <= day <= month_days:
        # Written month
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        # Calculating day suffix
        day_str = str(day)
        if day_str.endswith(('11','12','13')):
            suffix = 'th'
        else:
            if day_str.endswith('1'):
                suffix = 'st'
            elif day_str.endswith('2'):
                suffix = 'nd'
            elif day_str.endswith('3'):
                suffix = 'rd'
            else:
                suffix = 'th'
        return f"{months[month - 1]} {day}{suffix}, {year}"
    else:
        return None

def test_day_of_year():
    sample_years = [2000, 2001, 2001, 2001, 2001, 2001, 2001, 2001, 2001, 2001, 2001, 2015, 2015, 2016, 1500, 2010, 2010, 2010, 2010]
    sample_months = [ 12,    1,    1,    1,    1,    1,    1,    1,    1,    1,    1,    2,    2,    2,    5,    0,   13,    1,    1]
    sample_days = [   31,    1,    2,    3,    4,   11,   12,   13,   21,   22,   23,   28,   29,   29,    3,    1,    1,    0,   32]
    expected_output = ["December 31st, 2000",
                       "January 1st, 2001",
                       "January 2nd, 2001",
                       "January 3rd, 2001",
                       "January 4th, 2001",
                       "January 11th, 2001",
                       "January 12th, 2001",
                       "January 13th, 2001",
                       "January 21st, 2001",
                       "January 22nd, 2001",
                       "January 23rd, 2001",
                       "February 28th, 2015",
                       None,
                       "February 29th, 2016",
                       None,
                       None,
                       None,
                       None,
                       None
                       ]
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
