# Hayden Fillmore

    # This program is a rudimentary calculator that can perform a simple calculation of two inputs.
    # It is capable of performing addition, subtraction, multiplication, division, exponentiation, and root calculations.
    # It can also handle both integer and float inputs.

print("==================================================================================")
print("")
print("The following code was made to calculate two values given an assigned operation:")
print("")

# =====

# This block finds the first value and converting it to an float for calculation.
Value1 = input("What is your first value? ")
Value1 = float(Value1)

# This block checks if the input value is an integer or a float and converts it to the appropriate type for calculation.
if Value1.is_integer() == False:
    Value1 = float(Value1)

else:
    Value1 = int(Value1)

# This line determinines what operation to perform.
Result = input("What operation would you like to perform? (Add, Subtract, Multiply, Divide, Exponent, Root): ").upper()

# This block finds the second value and determines the proper verbage, followed by an float conversion.
if Result == "EXPONENT":
    Value2 = input("To what power? ")

elif Result == "ROOT":
    Value2 = input("What root will you take? ")

else:
    Value2 = input("What is your second value? ")
Value2 = float(Value2)

# This block checks if the input value is an integer or a float and converts it to the appropriate type for calculations.
if Value2.is_integer() == False:
    Value2 = float(Value2)
    
else:
    Value2 = int(Value2)

# =====

# This block defines the six operations that the user can perform.
ADD = Value1 + Value2
SUBTRACT = Value1 - Value2
MULTIPLY = Value1 * Value2
DIVIDE = Value1 / Value2
EXPONENT = Value1 ** Value2
ROOT = Value1 ** (1/Value2)

# =====

# This block visualizes the operation that will be performed on the two values based on the user's inputs.
if Result == "ADD":                                                                               
    print("")
    print(f"The result of adding {Value1} and {Value2} is: {ADD}")
    print("")
    print("==================================================================================")   

if Result == "SUBTRACT":
    print("")
    print(f"The result of subtracting {Value2} from {Value1} is: {SUBTRACT}")
    print("")
    print("==================================================================================")

if Result == "MULTIPLY":
    print("")
    print(f"The result of multiplying {Value1} and {Value2} is: {MULTIPLY}")
    print("")
    print("==================================================================================")

if Result == "DIVIDE":
    print("")
    print(f"The result of dividing {Value1} by {Value2} is: {DIVIDE}")
    print("")
    print("==================================================================================")

if Result == "EXPONENT":
    print("")
    print(f"The result of exponentiating {Value1} by {Value2} is: {EXPONENT}")
    print("")
    print("==================================================================================")

if Result == "ROOT":
    print("")
    print(f"The result of taking the {Value2} root of {Value1} is: {ROOT}")
    print("")
    print("==================================================================================")