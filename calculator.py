#SIMPLE CALCULATOR TO PERFORM BASIC ARITHMETIC OPERATION2




def add(num1, num2):
    	return num1 + num2




def subtract(num1, num2):
	return num1 - num2



def multiply(num1, num2):
	return num1 * num2




def divide(num1, num2):
	return num1 / num2



print("Please select the operation to be performed-\n" \
		"1. Addittion\n"
		"2. Subtraction\n" \
		"3. Multiplication\n" \
		"4. Division\n")



a = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))



if a == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))
	

elif a == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif a == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif a == 4: 
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Invalid input")
