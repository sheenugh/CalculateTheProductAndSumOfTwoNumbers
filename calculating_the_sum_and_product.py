#Delima, Sheena Mae D.
#BSCpE 1-5


#--------------------------------------------------------

# ----- FUNCTIONS -----
# Given A
print("Direction: Given the number1 = 20, number 3 = 30, display the output if the product and only the product of the two number is less than or equal to 1000. Otherwise, display the sum.")

# - Using def and if-else statement/function to find whether the total of the two number is product or sum, and print the result
def product_or_sum_of_two_numbers(num1, num2):
    result = num1 * num2
    if result <= 1000:
        print("The result is " + str(result) + ".")
    else:
        result = num1 + num2
        print("The result is " + str(result) + ".")
        
value_of_the_two_number = product_or_sum_of_two_numbers(20, 30)


print("\n")
print("-------------------------------------------")
print("\n")


#Given B.
print("Direction: Given the number1 = 40, number 3 = 30, display the output if the product and only the product of the two number is less than or equal to 1000. Otherwise, display the sum.")

# - Using def and if-else statement/function to find whether the total of the two number is product or sum, and print the result
def sum_or_product_of_two_numbers():
    number1 = 40
    number2 = 30
    result = number1 * number2
    if result <= 1000:
        print("The result is " + str(result) + ".")
    else:
        print("The result is " + str(result) + ".")
    
sum_or_product_of_two_numbers()