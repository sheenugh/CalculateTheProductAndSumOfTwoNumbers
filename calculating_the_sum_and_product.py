#Delima, Sheena Mae D.
#BSCpE 1-5


#=================================================================================================================================

# ----- FUNCTIONS -----
# - Given A: Using def and if-else statement/function to find whether the total of the two number is product or sum, and print the result.
def product_or_sum_of_two_numbers(num1, num2):
    result = num1 * num2
    if result <= 1000:
        return result
    else:
        result = num1 + num2
        return result

#>>>>>>>>>> PSEUDO CODE <<<<<<<<<<
# ------ ACTUAL CODES -----
# - This section is for the result and printing the result
resultA = product_or_sum_of_two_numbers(20, 30)
print("The result in Given A is " + str(resultA) + ".")


print("\n")
print("-------------------------------------------")
print("\n")



# - Given B: Using def and if-else statement/function to find whether the total of the two number is product or sum, and print the result
# Instead of using the same method in Given A, I used an alternative method.
def sum_or_product_of_two_numbers():
    number1 = 40
    number2 = 30
    result = number1 * number2
    if result <= 1000:
        return result
    else:
        return number1 + number2
    
resultB = sum_or_product_of_two_numbers()
print("The result of Given B is " + str(resultB) + ".")