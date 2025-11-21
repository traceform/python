import logging


# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,   # Change to show debug and above
    format="[%(levelname)s] %(message)s"
)


# --- Utility functions ---
def is_a_triangle(a, b, c):
    """Returns if a triangle is valid"""
    # Checking if arguments are valid
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        return False
    # Positive Side Lengths: All sides must be greater than zero
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Triangle inequality: The sum of any two sides must be greater than the third
    return  a + b > c and a + c > b and b + c > a

def is_a_right_triangle(a, b, c):
    """Returns if a triangle is a right triangle"""
    if not is_a_triangle(a, b, c):
        return False
    else:
        # Pythagorean Theorem: A triangle is right-angled if one side (the hypotenuse)
        # squared equals the sum of the squares of the other two sides
        sides = [a, b, c]
        hipotenuse = max(sides)
        sides.remove(hipotenuse)

        return hipotenuse == (sides[0] ** 2 + sides[1] ** 2) ** 0.5

def heron(a, b, c):
    """Returns the area of a given triangle"""
    s = (a + b + c) / 2  # semi-perimeter
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # area

def area_of_triangle(a, b, c):
    """Returns the area of a given triangle if valid"""
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


# --- Input/output functions ---
def receive_sides():
    """Receives and validates the given sides"""
    sides = []
    logging.debug(f"receive_sides(): sides before while: {sides}")
    count = 1
    logging.debug(f"receive_sides(): count before while: {count}")
    while not sides or len(sides) < 3:
        try:
            side = int(input(f"Enter the length of side {count}: "))
            if side > 0:
                sides.append(side)
                logging.debug(f"receive_sides(): sides after sucessful try: {sides}")
                count += 1
                logging.debug(f"receive_sides(): count after sucessful try: {count}")
            else:
                raise ValueError
        except ValueError:
            print("Only floating point numbers greater than 0 are accepted. ", end='')
        except KeyboardInterrupt:
            print("\nProgram terminated.")
        except:
            print("Invalid operation, try again. ", end='')
    return sides[0], sides[1], sides[2]


# --- Test functions ---
def test_function(function, sample_a, sample_b, sample_c, expected_output):
    """Tests a given function"""
    print(f">>> TESTING {function}")
    for _ in range(len(expected_output)):
        a = sample_a[_]
        b = sample_b[_]
        c = sample_c[_]
        expected = expected_output[_]

        print(f"a: {a} | b: {b} | c: {c} -> ", end='')
        output = function(a, b, c)
        if output == expected:
            status = 'OK'
        else:
            status = 'Failed'
        
        print(status, end='')
        print(f" | Result: {output}", end='')
        print()

def test_is_a_triangle():
    function = is_a_triangle
    sample_a = [          1,     1,    3,          1,         0,            -3,         'a']
    sample_b = [          1,     1,    4,          2,         4,             4,          3 ]
    sample_c = [          1,     3,    5,          3,         5,             5,          4 ]
    expected_output = [True, False, True,      False,     False,         False,       False]
    #                                     degenerate, zero side, negative side, non-numeric

    return test_function(function, sample_a, sample_b, sample_c, expected_output)

def test_is_a_right_triangle():
    function = is_a_right_triangle
    sample_a = [          5,     1]
    sample_b = [          3,     3]
    sample_c = [          4,     4]
    expected_output = [True, False]

    return test_function(function, sample_a, sample_b, sample_c, expected_output)

def test_area_of_triangle():
    function = area_of_triangle
    sample_a = [                        1.]
    sample_b = [                        1.]
    sample_c = [                  2. ** .5]
    expected_output = [0.49999999999999983]

    return test_function(function, sample_a, sample_b, sample_c, expected_output)

# --- Master ---
def master():
    print("""
==== TRIANGLE VALIDATOR ====
Check if a triangle is valid,
see if it's a right triangle
and calculate its area!
""")

    a, b, c = receive_sides()
    if is_a_triangle(a, b, c):
        print(f"{a}, {b} and {c} make a triangle.", end='')

        if is_a_right_triangle(a, b, c):
            print(f" A right triangle.")

        area = area_of_triangle(a, b, c)
        if area:
            print(f"Area of the triangle: {area}")
    else:
        print(f"{a}, {b} and {c} DO NOT make a triangle.")

if __name__ == '__main__':
    # Testing
    #test_is_a_triangle()
    #test_is_a_right_triangle()
    #test_area_of_triangle()

    master()
