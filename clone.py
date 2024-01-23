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
def product_of_two_number(num1, num2):
    result = num1 * num2
    if result <= 1000:
        print("The product is " + str(result) + ".")
    else:
        result = num1 + num2
        print(result)
        
value_of_the_two_number = product_of_two_number(20, 30)

