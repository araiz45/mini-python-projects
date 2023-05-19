operand_1 = input("Enter Operand 1 : ")
operator = input("Enter Operator : ")
operand_2 = input("Enter Operand 2 : ")

operand_1 = int(operand_1)
operand_2 = int(operand_2)


if operator == "add":
    print("The Sum of {} and {} is {}".format(operand_1, operand_2, operand_1 + operand_2))
elif operator == "substract":
    print("The Subraction of {} and {} is {}".format(operand_1, operand_2, operand_1 - operand_2))
elif operator == "multiple":
    print("The Multiplication of {} and {} is {}".format(operand_1, operand_2, operand_1 * operand_2))
elif operator == "divide":
    print("The divison of {} and {} is {}".format(operand_1, operand_2, operand_1 / operand_2))
elif operator == "mod":
    print("The Modulus of {} and {} is {}".format(operand_1, operand_2, operand_1 % operand_2))
elif operator == "power":
    print("The Power of {} and {} is {}".format(operand_1, operand_2, operand_1 ** operand_2))

else:
    print("invalid operator")
