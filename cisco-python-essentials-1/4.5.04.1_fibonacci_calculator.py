# --- Utility functions ---
def fib(num):
    """Returns the fibonacci of a given number"""
    # Must be an integer
    if not isinstance(num, int):
        return None
    else:
        # Rule: must be positive in this case
        if num < 0:
            return None
        else:
            # Rule: Fibonacci of 0 is 0 itself
            if num == 0:
                return 0
            # Rule: Fibonacci of both 1 and 2 is 1
            elif 1 <= num <= 2:
                return 1
            else:
                # Rule: each Fibonacci number is the sum
                # of the two previous Fibonacci numbers
                #
                # WARNING: The following code was removed
                # because of optimization issues when
                # calculating fibonacci numbers over 20
                #
                #fibonacci = 1
                #for n in range(num, num + 1):
                #    return fib(n - 1) + fib(n - 2)
                #
                # Optimized code:
                penultimate = last = 1
                next_fibonacci = 0
                for i in range(3, num + 1):
                    next_fibonacci = penultimate + last
                    penultimate, last = last, next_fibonacci
                return next_fibonacci

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
def test_function(function, test_type, sample_input, expected_output):
    """Tests a given function"""
    print(f">>> TESTING FOR [{test_type.upper()}] {function}")
    for _ in range(len(expected_output)):
        input = sample_input[_]
        expected = expected_output[_]

        print(f"Number: {input} -> ", end='')
        output = function(input)
        if output == expected:
            status = 'OK'
        else:
            status = 'Failed'
        
        print(status, end='')
        print(f" | Result: {output}", end='')
        print()

def test_fib():
    print(">>> Trying the first 10 fibonacci numbers: ")
    for n in range(0, 10):
        print(fib(n), end=' ')
    print()

    function = fib

    # Regular cases
    test_type = "Regular cases"
    sample_input = [   0, 1, 2, 3, 4, 5, 6,  7]
    expected_output = [0, 1, 1, 2, 3, 5, 8, 13]
    test_function(function, test_type, sample_input, expected_output)

    # Edge cases
    test_type = "Edge cases"
    sample_input = [     -1,  1.0,  'a']
    expected_output = [None, None, None]
    test_function(function, test_type, sample_input, expected_output)

# --- Master ---
def master():
    print("""
==== FIBONACCI CALCULATOR ====
Calculate any Fibonacci number!
""")
    n = receive_num()
    print(fib(n))

if __name__ == '__main__':
    # Debugging
    #test_fib()

    master()
