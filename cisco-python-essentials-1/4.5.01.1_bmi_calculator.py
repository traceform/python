import re
import logging
from time import sleep

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,   # Change to show debug and above
    format="[%(levelname)s] %(message)s"
)


# --- Utility functions ---
def bmi(weight: float, height: float) -> float | None:
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
        raise Exception(f"ERROR: Invalid data. The given data is biologically invalid for adults.")
    return None

def lb_to_kg(pounds: float) -> float:
    """Converts pounds to kilograms"""
    logging.debug(f"pounds: {pounds}, type: {type(pounds)}")
    return pounds * 0.45359237

def ft_and_inch_to_m(feet: int, inches: int = 0) -> float:
    """Converts feet and inches to meters"""
    logging.debug(f"feet: {feet}, type: {type(feet)} | inches: {inches}, type: {type(inches)}")
    return feet * 0.3048 + inches * 0.0254

def classify_bmi(bmi: float) -> str:
    """Returns the respective BMI classification"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obesity Class I"
    elif bmi < 40:
        return "Obesity Class II"
    else:
        return "Obesity Class III"


# --- Input/output functions ---
def receive_input(
    option: int,
    weight_text: str,
    height_text: str
) -> tuple[float, float] | tuple[float, int, int] | None:

    """Receives and parses the user inputted weight and height values"""
    # Validating weight input
    while True:
        try:
            weight = float(input(f"Enter your weight in {weight_text}: "))
            break
        except ValueError:
            print("Invalid weight, try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            quit()

    # Validating height input
    while True:
        try:
            msg = ''
            height = input(f"Enter your height in {height_text}: ")
            logging.debug(f"Height bmi_result after input: {height}")
            # Depending on the option chosen, different things happen
            if option == 1:
                height = float(height)
                break
            elif option == 2:
                # Selecting only the numbers in the string, in order
                height = re.findall(r"\d+", height)
                logging.debug(f"Height bmi_result after regex: {height}")
                # Checking if only 2 values were inputted at most
                if len(height) == 1:
                    height.append(0)
                if len(height) == 2:
                    for _ in range(len(height)):
                        # Validating the numbers as integers
                        if isinstance(int(_), int):
                            # Replacing list items with the integers
                            height[_] = int(height[_])
                    logging.debug(f"Height after type casting: {height}")
                    return weight, height[0], height[1]
                else:
                    msg = "You entered too many numbers. Minimum is one, maximum is two. Ex.: 5'10\". "
                    raise ValueError
            else:
                return
        except ValueError:
            print(f"ERROR: Invalid height. {msg}Try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated.")
        
    return weight, height

def choose_option(options: list, prompt: str, default_option = 1) -> int:
    """Receives and returns a valid option to continue"""
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
            if number in OPTIONS:
                return number
            else:
                _ = ' valid'
        except ValueError:
            _ = ' valid'
        except KeyboardInterrupt:
            raise KeyboardInterrupt

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
        print(f" | bmi_result: {output}", end='')
        print()


# --- Master Section ---
def master():
    try:
        if option == 0:
            print("\n>>> AUTOMATIC TESTING MODE ACTIVE")
            test_bmi()
            quit()
        elif option == 1:
            weight, height = receive_input(option, 'kilograms', 'meters')
            logging.debug(f"option 1 > receive_input() returned weight: {weight} | height: {height}")
            bmi_result = bmi(weight, height)
            logging.debug(f"option 1 > bmi_result() returned bmi: {bmi_result}")
        elif option == 2:
            weight, height_feet, height_inches = receive_input(option, 'pounds', 'feet (inches is optional)')
            logging.debug(f"option 2 > receive_input() returned weight: {weight} | height feet: {height_feet} | height inches: {height_inches}")
            weight, height = lb_to_kg(weight), ft_and_inch_to_m(height_feet, height_inches)
            logging.debug(f"option 2 > lb_to_kg() returned weight: {weight}")
            logging.debug(f"option 2 > ft_and_inch_to_m() returned height: {height}")
            bmi_result = bmi(weight, height)
            logging.debug(f"option 2 > bmi_result() returned bmi: {bmi_result}")
        else:
            bmi_result = None

        if bmi_result:
            category = classify_bmi(bmi_result)
            print(f"BMI = {bmi_result:.2f}, Category = {category}")
        else:
            raise Exception(f"ERROR: Invalid data.")
    except Exception as e:
        print(e)

    sleep(3)

if __name__ == "__main__":
    DEBUGGING_ON = False
    OPTIONS = [0, 1, 2, 9]
    menu = """
===== BODY MASS INDEX CALCULATOR =====

Choose the measurement unit:
0. Activate automatic testing mode
1. Metric: kilograms, meters (Default)
2. Imperial: pounds, feet, inches
CTRL-C to quit
======================================"""

    while True:
        try:
            option = choose_option(OPTIONS, menu)

            if option == 9 and not DEBUGGING_ON:
                logging.getLogger().setLevel(logging.DEBUG)
                print("\n>>> DEBUGGING MODE ACTIVE")
                print("Restart the program to deactivate.")

                option = choose_option(OPTIONS, '')

            round = 0
            while True:
                if round > 0:
                    option = choose_option(OPTIONS, menu)
                master()
                round += 1
        except KeyboardInterrupt:
            print(f"\nProgram terminated.")
            quit()
