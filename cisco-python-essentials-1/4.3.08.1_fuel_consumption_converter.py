MILE_IN_KM = 1.609344  # 1 mile = 1609.344 meters so 1.609344 kilometers
GALLON_IN_LITERS = 3.785411784

def liters_100km_to_miles_gallon(liters_per_100km):
    """Converts the liters per 100km rate (L/100KM) to miles per gallon (MPG)"""
    gallons_consumed = liters_per_100km / GALLON_IN_LITERS
    miles_traveled = 100 / MILE_IN_KM
    return miles_traveled / gallons_consumed

def miles_gallon_to_liters_100km(mpg):
    """Converts the miles per gallon (MPG) to liters per 100km rate (L/100KM)"""
    km_per_liter = (mpg * MILE_IN_KM) / GALLON_IN_LITERS
    liters_per_100km = 100 / km_per_liter
    return liters_per_100km

def test_function(function, sample_input, expected_output):
    """Tests a given function"""
    print(f">>> TESTING {function}")
    for _ in range(len(expected_output)):
        input = sample_input[_]
        expected = expected_output[_]

        print(f"{input} -> ", end='')
        output = function(input)
        if output == expected:
            status = 'OK'
        else:
            status = 'Failed'
        
        print(status, end='')
        print(f" | Result: {output}", end='')
        print()

def test_liters_100km_to_miles_gallon():
    sample_input = [3.9, 7.5, 10.]
    expected_output = [60.31143162393162,
                       31.36194444444444,
                       23.52145833333333]
    test_function(liters_100km_to_miles_gallon, sample_input, expected_output)

def test_miles_gallon_to_liters_100km():
    sample_input = [60.3, 31.4, 23.5]
    expected_output = [3.9007393587617467,
                        7.490910297239916,
                       10.009131205673757]
    test_function(miles_gallon_to_liters_100km, sample_input, expected_output)

test_liters_100km_to_miles_gallon()
test_miles_gallon_to_liters_100km()
