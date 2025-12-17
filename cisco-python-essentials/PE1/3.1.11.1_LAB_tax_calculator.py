def tax_calculator(income):
    threshold = 85528
    tax_relief = 556.02

    income = float(income)

    if income < threshold:
        # tax equal to 18% of the income minus 556 thalers and 2 cents of tax relief
        tax = (income * 0.18) - tax_relief
    else:
        # tax equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers
        tax = 14839.02 + ((income - threshold) * 0.32)
    if tax < 0:
        # country never returns any money to its citizens
        tax = 0.0
    tax = round(tax, 0)
    return f"The tax is: {tax} thalers"

def test_code():
    sample_input = [10000, 100000, 1000, -100]
    expected_output = ["The tax is: 1244.0 thalers", "The tax is: 19470.0 thalers", "The tax is: 0.0 thalers", "The tax is: 0.0 thalers"]

    for _ in range(len(sample_input)):
        input = sample_input[_]
        output = tax_calculator(input)
        if output == expected_output[_]:
            print(f"Success! Input: {input} | Output: {output}")
        else:
            print(f"Error! Input: {input} | Output: {output}")

#print(tax_calculator(input("Inform your income: ")))
test_code()
