import re

def bmi(weight: float, height: float) -> float:
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

def receive_input(option: int, weight_text: str, height_text: str) -> :
    # Validating weight input
    while True:
        try:
            weight = float(input(f"Enter your weight in {weight_text}: "))
            break
        except ValueError:
            print("Invalid weight, try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated.")

    # Validating height input
    while True:
        try:
            msg = ''
            height = input(f"Enter your height in {height_text}: ")
            #print(f"[DEBUG] Height result after input: {height}")
            # Depending on the option chosen, different things happen
            if option == 1:
                height = float(height)
                break
            elif option == 2:
                # Selecting only the numbers in the string, in order
                height = re.findall(r"\d+", height)
                #print(f"[DEBUG] Height result after regex: {height}")
                # Checking if only 2 values were inputted at most
                if len(height) == 1:
                    height.append(0)
                if len(height) == 2:
                    for _ in range(len(height)):
                        # Validating the numbers as integers
                        if isinstance(int(_), int):
                            # Replacing list items with the integers
                            height[_] = int(height[_])
                    #print(f"[DEBUG] Height after type casting: {height}")
                    return weight, height[0], height[1]
                else:
                    msg = "You entered too many numbers. Minimum is one, maximum is two. Ex.: 5'10\". "
                    raise ValueError
            else:
                return
        except ValueError:
            print(f"Invalid height. {msg}Try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated.")
        
    return weight, height

def lb_to_kg(pounds: float) -> float:
    """Converts pounds to kilograms"""
    #print(f"[DEBUG] pounds: {pounds}, type: {type(pounds)}")
    return pounds * 0.45359237

def ft_and_inch_to_m(feet: int, inches: int = 0) -> float:
    """Converts feet and inches to meters"""
    #print(f"[DEBUG] feet: {feet}, type: {type(feet)} | inches: {inches}, type: {type(inches)}")
    return feet * 0.3048 + inches * 0.0254

def choose_option(options: int, prompt: str, default_option = 1):
    """Returns a valid option to continue"""
    option_list = []
    for n in range(options + 1):
        option_list.append(n)
    #print(f"[DEBUG] Result of option_list after for loop based on options argument given: {option_list}")

    _ = 'n'

    print(prompt)

    while True:
        try:
            number = input(f"Choose a{_} option: ")
            # If the user presses ENTER, return default option number
            if number == '':
                return default_option
            # If the user inputted value is valid, return value
            number = int(number)
            if number in option_list:
                return number
            else:
                _ = ' valid'
        except ValueError:
            _ = ' valid'

def test_bmi():
    function = bmi
    sample_weight = [                52.5, 352.5,          lb_to_kg(176)]
    sample_height = [                1.65,  1.65, ft_and_inch_to_m(5, 7)]
    expected_output = [19.283746556473833,  None,     27.565214082533313]

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

def main_debug():
    print("\n>>> DEBUGGING MODE ACTIVE")
    print(f"[DEBUG] choose_option() returned option: {option}")
    if option == 0:
        print("\n>>> AUOMATIC TESTING MODE ACTIVE")
        test_bmi()
        quit()
    if option == 1:
        weight, height = receive_input(option, 'kilograms', 'meters')
        print(f"[DEBUG] option 1 > receive_input() returned weight: {weight} | height: {height}")
        result = bmi(weight, height)
    elif option == 2:
        weight, height_feet, height_inches = receive_input(option, 'pounds', 'feet (inches is optional)')
        print(f"[DEBUG] option 2 > receive_input() returned weight: {weight} | height feet: {height_feet} | height inches: {height_inches}")
        weight, height = lb_to_kg(weight), ft_and_inch_to_m(height_feet, height_inches)
        print(f"[DEBUG] option 2 > lb_to_kg() returned weight: {weight}")
        print(f"[DEBUG] option 2 > ft_and_inch_to_m() returned height: {height}")
        result = bmi(weight, height)
    else:
        result = 'fuck'
    print(result)
    quit()

def main():
    if option == 0:
        while True:
            try:
                main_debug()
            except KeyboardInterrupt:
                print(f"\nProgram terminated.")
                quit()
    if option == 1:
        weight, height = receive_input(option, 'kilograms', 'meters')
        result = bmi(weight, height)
    elif option == 2:
        weight, height_feet, height_inches = receive_input(option, 'pounds', 'feet (inches is optional)')
        weight, height = lb_to_kg(weight), ft_and_inch_to_m(height_feet, height_inches)
        result = bmi(weight, height)
    else:
        result = 'fuck'
    print(result)

if __name__ == "__main__":
    while True:
        try:
            option = choose_option(3, 
"""=== BODY MASS INDEX CALCULATOR ===

Choose the measurement unit (or press CTRL-C to exit):
0. Activate debugging mode
1. Metric: kilograms, meters (Default)
2. Imperial: pounds, feet, inches""")
            main()
        except KeyboardInterrupt:
            print(f"\nProgram terminated.")
