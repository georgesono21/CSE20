#Name: George Sono 
#Class: CSE20
#Assingment 2.1
#Purpose: The program allows you to track your monthly budget by checking if you are currently over or under your budget, based off of spending.

#input functions asks for name
name = input("Hello what is your name? \n Name: ")

#input function for budget converts answer from string to floating value
budget = float(input(f"Welcome to George's budget calculator {name}, what is your monthly budget?\n  Budget (in USD): "))

#input function for amount spent converts answer form string to floating value
totalspent = float(input(f"  Your inputted monthly budget in dollars is {budget:.2f}. \nHow much have you spent this month? "))

#if the total spent is greater than the budget, then the program would output the print function regarding exceeding the monthly budget
#round function makes it so it follows actual USD with 0.01 USD being a cent
if totalspent > budget:
  print(f"  YOU HAVE EXCEEDED YOUR MONTHLY BUDGET. Exceeding {round(totalspent-budget,2):.2f} dollar(s) over!")

#if the if operation isn't satisfoed (by going over the budget) the formatted print function will output a congratulations message and show the remaining amount of money left in their budget
else:
  print(f"  GOOD JOB! You have stayed within your budget and have {round(budget-totalspent,2):.2f} dollar(s) remaining!!")

#acknowledgements: Hari Kuttivelli, Stackoverflow