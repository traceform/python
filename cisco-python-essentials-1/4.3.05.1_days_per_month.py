def is_year_leap(year):
    if year < 1582:
        msg = False  # "Not within the Gregorian calendar period"
    else:
        if year % 4 != 0:
            msg = False  # "Common year"
        elif year % 100 != 0:
            msg = True  # "Leap year"
        elif year % 400 != 0:
            msg = False  # "Common year"
        else:
            msg = True  # "Leap year"
    return msg

def days_in_month(year, month):
    if month == 2 and is_year_leap(year):
        return 29
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
