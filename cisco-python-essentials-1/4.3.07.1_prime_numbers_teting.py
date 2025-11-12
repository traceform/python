def is_prime(number):
    """Returns if a number is prime"""
    # Checking if number is integer and above 1
    if not isinstance(number, int) or number <= 1:
        return None
    else:
        # Checking if the number is divisible by any number
        # from 2 to the number right before itself
        for n in range(2, number):
            if number % n == 0:
                return False
        return True
        
def test_is_prime():
    sample_input = [      -3,  3.0,    3,     8]
    expected_output = [ None, None, True, False]
    print(">>> TESTING is_prime()")
    for _ in range(len(expected_output)):
        input = sample_input[_]
        print(f"{input} -> ", end='')
        output = is_prime(input)
        if output == expected_output[_]:
            status = "OK"
        else:
            status = "Failed"
        print(status, end='')
        #print(f" | Result: {output}", end='')
        print()

def test_is_prime_2():
    output = []
    expected_output = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for n in range(0, 100):
        if is_prime(n):
            output.append(n)
            #print(n, end=' ')
    if output == expected_output:
        print("Success! Only primes have been collected.")
    else:
        print("Failed.")
    #print(output)

#test_is_prime()
test_is_prime_2()
