print("This is a calculator that takes 3 numbersand operation to be carried out on them and returns the answer")
import math
value_1 = (input("Enter 1st number"))
operator_1 = (input("Enter an operation"))
value_2 = (input("Enter 2nd number"))
operator_2 = (input("Enter an operation"))
value_3 = print(input("Enter 3rd number"))
# operators = {+, -, /, *}
add = "+"
subtract = "-" 
divide = "/"
multiply ="*"
if operator_1 == add and operator_2 == add:
    print(value_1 + value_2 + value_3)
elif operator_1 - - add and operator_2 - - subtract:
    print(value_1 + value_3)
elif operator_1 - - add and operator_2 - - multiply:
    print(value_1 + value_2  * value_3)
elif operator_1 - -add and operator_2 - - divide:
    print(value_1 + value_2 / value_3)
elif operator