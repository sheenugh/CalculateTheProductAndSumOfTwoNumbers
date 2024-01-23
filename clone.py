#Delima, Sheena Mae D.
#BSCpE 1-5


#--------------------------------------------------------
# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
# A.
# Given: 
# number1 = 20
# number2 =   30

# B. 
# Given:
# number1 = 40
# number2 = 30


# ----- FUNCTIONS -----
# Given A
def product_or_sum_of_two_numbers(num1, num2):
    result = num1 * num2
    if result <= 1000:
        print("The product is " + str(result) + ".")
    else:
        result = num1 + num2
        print("The sum is " + str(result) + ".")
        
value_of_the_two_number = product_or_sum_of_two_numbers(20, 30)


print("\n")


#Given B.
def sum_or_product_of_two_numbers():
    number1 = 40
    number2 = 30
    result = number1 * number2
    if result <= 1000:
        print("The product is " + str(result) + ".")
    else:
        print("The sum is " + str(result) + ".")
    
sum_or_product_of_two_numbers()