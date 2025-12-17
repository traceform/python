def test_code():
    """Tests the code with predefined values"""
    input_list = [1, 10, 100, -5, 0, 'a', True, False]
    output_list = [0.6000000000000001, 0.09901951266867294, 0.009999000199950014, -0.19258202567760344, None, None, 0.6000000000000001, None]
    for i in range(0,len(input_list)):
        input = input_list[i]
        output = output_list[i]
        result, msg = math_expression(input)
        if result == output:
            print(f"Success! {input} returns {output}")
        else:
            print(f"Error! {input} does NOT result in {output}")

def math_expression(x):
    """Evaluates the math expression with a given number"""
    y, msg = None, None
    try:
        y = 1/(x + 1/(x + 1/(x + 1/x)))
    except ZeroDivisionError:
        msg = "Error! Division by zero is not allowed!"
    except:
        msg = "Something went wrong!"
    return y, msg

#test_code()

if __name__ == "__main__":
    y, msg = math_expression(float(input("Enter value for x: ")))
    if y is None:
        print(msg)
    else:
        print("y =", y)
