import re

def bmi(weight, height):
    """
    Calculates the Body Mass Index based on
    given weight (kg) and height (meters)
    """
    # Validating height and weight matematically
    if weight > 0 and height > 0:
        # Validating them biologically
        if 40 <= weight <= 150 \
        and 1.40 <= height <= 2.10:
            try:
                return weight / (height ** 2)
            except ZeroDivisionError:
                return None
    return None

def receive_input(option, weight_text, height_text):
    while True:
        try:
            weight = float(input(f"Enter your weight in {weight_text}: "))
            break
        except ValueError:
            print("Invalid weight, try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated.")

    while True:
        try:
            height = input(f"Enter your height in {height_text}: ")
            if option == 1:
                height = float(height)
                break
            elif option == 2:
                # Removing special characters, making a list of unique characters
                height = set(re.sub(r"[^0-9]", ' ', height).split()).discard(' ')
                # Keeping only the integers
                valid_integers = []
                for _ in height:
                    if isinstance(int(_), int):
                        valid_integers.append(_)
                if 0 >= len(valid_integers) >= 3:
                    raise ValueError
                return weight, valid_integers[0], valid_integers[1]
            else:
                return
        except ValueError:
            print("Invalid height, try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated.")
        
    return weight, height

def lb_to_kg(pounds):
    """Converts pounds to kilograms"""
    return pounds * 0.45359237

def ft_and_inch_to_m(feet, inches = 0.0):
    """Converts feet and inches to meters"""
    return feet * 0.3048 + inches * 0.0254

def choose_option(options, prompt, number = 1):
    """Returns a valid option to continue"""
    option_list = []
    for n in range(1, options + 1):
        option_list.append(n)
    print(option_list)

    _ = 'n'

    print(prompt)

    while True:
        try:
            received_number = input(f"Choose a{_} option: ")
            # If the user presses ENTER, return default option number
            if received_number == '':
                return number
            # If the user inputted value is valid, return value
            received_number = int(received_number)
            if received_number in option_list:
                return received_number
            else:
                _ = ' valid'
        except ValueError:
            _ = ' valid'

def test_bmi():
    function = bmi
    sample_weight = [52.5, 352.5]
    sample_height = [1.65, 1.65]
    expected_output = [19.283746556473833, None]

    print(f">>> TESTING {function}")
    for _ in range(len(expected_output)):
        input_weight = sample_weight[_]
        input_height = sample_height[_]
        expected = expected_output[_]

        print(f"W: {input_weight} | H: {input_height} -> ", end='')
        output = function(input_weight, input_height)
        if output == expected:
            status = 'OK'
        else:
            status = 'Failed'
        
        print(status, end='')
        print(f" | Result: {output}", end='')
        print()

if __name__ == "__main__":
    # Debugging
    #test_bmi()

    option = choose_option(2, """
=== BODY MASS INDEX CALCULATOR ===

Choose the measurement unit:
1. Metric: kg, m (Default)
2. Imperial: pounds, feet, inches""")

    if option == 1:
        weight, height = receive_input(option, 'kilograms', 'meters')
        result = bmi(weight, height)
    elif option == 2:
        weight, height_feet, height_inches = receive_input(option, 'pounds', 'feet (inches is optional)')
        result = bmi(lb_to_kg(weight), ft_and_inch_to_m(height_feet, height_inches))
    else:
        result = 'fuck'
    print(result)
        