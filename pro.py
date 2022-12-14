
def personal_finanace(income,additonalincome,household,utilities,food,extra):
     monthly_income = income + additonalincome
     your_expenditure = household + utilities + food + extra
     total_expenditure= monthly_income - your_expenditure
     print("The total amount you have spended this month is Rs:",your_expenditure)
     print("The total amount left with you now is:",total_expenditure)



true=True
while true:
    print(''' 
------------------------------------------------------------------------------------------------------    
------------------------------------WELCOME TO PERSONAL FINANCE TOOL----------------------------------
------------------------------------------------------------------------------------------------------ 
Here we will help you to calculate your monthly expenditure
''')
    salary_money = float(input('Enter your monthly salary (RS.):\n'))
    additional_money= float(input('Enter your additonal salary (RS.):\n'))
    print("The total salary you have is:-",salary_money + additional_money)
    household_money = float(input('Enter monthly housing housing expenses (RS.):\n'))
    utilities_money = float(input('Enter monthly utilities  expenses(RS.):\n'))
    food_money = float(input('Enter monthly food expenses (RS.):\n'))
    extra_money = float(input('Enter  any additional expenses (RS.):\n'))
    maximum = max(household_money, utilities_money, food_money, extra_money)

    if maximum == household_money:
        print("The maximum amount you have spent on household:", maximum)
    elif maximum == utilities_money:
        print("The maximum amount you have spent on utilities:", maximum)
    elif maximum == food_money:
        print("The maximum amount you have spent on food:", maximum)
    elif maximum == extra_money:
        print("The maximum amount you have spent on extra money:", maximum)
    else:
        pass
    expenditure = personal_finanace(salary_money,additional_money,household_money,utilities_money,food_money,extra_money)





    print('''
                 If you want to reapeat again press : '1'
                 If you want to end this press : '0' 
    ''')
    select=int(input("Enter the number what you want to choose:\n"))
    if select==1:
        print("ok let's begin with a new finance")
    elif select==0:
        print('              !!!RATE PLEASE!!!    ')

        inp = str(input("Enter the ratings('*')"))

        if inp == "*":
            print('VERY BAD :(')
        elif inp == "**":
            print("BAD '_' ")
        elif inp == "***":
            print('GOOD :-)')
        else:
            print('EXCELLENT ( ^_^ ) ')

        print('''
                             !!!!!!!!!!!!THANK YOU FOR USING MONTHLY BUDGET TOOL!!!!!!!!!!!!''')
        break
    else:
        print("You have entered wrong number you exited directly:")
        break




