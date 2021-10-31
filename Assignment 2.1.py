#Name: George Sono
#Class: CSE20 
#Prof: Harikishna Kuttivelli
#Description: This is a program that acts as a basic four function calculator. It computes addition, subtraction, multiplication and division given two operands

#input function asking for name (as a string)
name = input("Welcome to George's Four Function Calculator... \n What is your name? \n Name: ")
#print function asking for two numbers (\n creates a new line)
print (f"\nHi {name}!\n What two numbers would you like to use?\n")
#allows for input for first number and converts the input from a string to a integer
firstnum = float(input("  First Number: "))
#^^ same stuff but second number
secondnum = float(input("\n  Second Number: "))

#performs operations on numbers and rounds to two decimal places
sum1 = round(firstnum+secondnum,2)
diff = round(firstnum-secondnum,2)
product = round(firstnum*secondnum,2)
quotient = round(firstnum/secondnum,2)

#prints the results into a formatted string to integrate the variables into the text

print(f"\n RESULTS\n\n  The sum is: {sum1}\n  The difference is: {diff}\n  The product {product}\n  The quotient is: {quotient}")

#acknoledgments: Harikishna Kuttivelli, GiraffeAcademy, Python Doccumentation