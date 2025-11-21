# --- Utility functions ---
def factorial_function(n: int) -> int:
    """Returns the factorial of a non-negative integer"""
    # Must be an integer
    if not isinstance(n, int):
        return None
    else:
        # Must be positive
        if n < 0:
            return None
        # Base case convention: 0! = 1
        elif n == 0:
            return 1
        else:
            factorial = 1
            for n in range(1, n + 1):
                factorial *= n
            return factorial

# --- Input/output functions ---
def receive_num() -> int:
    """Receives, validates and returns the user input"""
    while True:
        try:
            n = int(input("Enter a non-negative integer: "))
            if not n >= 0:
                raise ValueError
            return n
        except ValueError:
            print("Only positive integers are accepted. ", end='')
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            quit()

# --- Test functions ---
def test_function(function, sample_input, expected_output):
    """Tests a given function"""
    print(f">>> TESTING {function}")
    for _ in range(len(expected_output)):
        input = sample_input[_]
        expected = expected_output[_]

        print(f"{input}! -> ", end='')
        output = function(input)
        if output == expected:
            status = 'OK'
        else:
            status = 'Failed'
        
        print(status, end='')
        print(f" | Result: {output}", end='')
        print()

def test_actorial_function():
    function = factorial_function
    sample_input = [   0, 1, 2, 3,  4,   5,   -1,  1.0,  'a']
    expected_output = [1, 1, 2, 6, 24, 120, None, None, None]

    return test_function(function, sample_input, expected_output)

# --- Master ---
def master():
    print("""\
=== FACTORIAL CALCULATOR ===
Calculate the factorial of
any non-integer number!
""")

    n = receive_num()
    factorial = factorial_function(n)
    if factorial:
        print(f"{n}! = {factorial}")

if __name__ == '__main__':
    # Debugging
    #test_actorial_function()

    master()
