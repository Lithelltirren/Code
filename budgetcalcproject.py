masterlist = ('all','paycheck','rent','games','power','water','internet','car','pet','gas','food')
items_budget = {}
items_spent = {}
for x in masterlist:
    items_budget[f'{x}'] = 0
    items_spent[f'{x}'] = 0
 
def mainscreen_select():
    user_input = input('What would you like to view?\nBudget\nSpent\nSummary\n')
    if user_input.lower() == 'budget':
        budget_select()
    elif user_input.lower() == 'spent':
        spent_select()
    elif user_input.lower() == 'summary':
        summary_select()
    else:
        print('You have made an invalid selection, restarting.')
        mainscreen_select()
        
def decline():
    print('Have a great day!')
    
def budget_select():
    print(('\n'*10) + 'Please select a budget to modify.\nPaycheck, Rent, Games, Power, Water, Internet, Car, Pet, Gas, Food.')
    user_input = input().lower()
    if user_input in items_budget.keys():
        print(f'You want to edit {user_input}? y/n')
        answer = input().lower()
        if (f'{answer}') == 'y':
            amount_answer = (input(f'What you would like to set {user_input} to? $'))
            items_budget[user_input] = amount_answer
            print(f'You changed {user_input} to {amount_answer}!\nWould you like to perform another transaction? y/n')
            answer == input().lower()
            if answer == 'y':
                mainscreen_select()
            elif answer == 'n':
                decline()
        elif answer == 'n':
            decline()

            
        
def spent_select():
        print(('\n'*10) + 'Please select a spent to modify.\nPaycheck, Rent, Games, Power, Water, Internet, Car, Pet, Gas, Food.')
        user_input = input().lower()
        if user_input in items_spent.keys():
            print(f'You want to edit {user_input}? y/n')
            answer = input().lower()
        if (f'{answer}') == 'y':
            amount_answer = (input(f'What you would like to set {user_input} to? $'))
            print(f'You changed {user_input} to ' + str(f'{amount_answer}!\nWould you like to perform another transaction? y/n'))
            answer == input().lower()
            if answer == 'y':
                mainscreen_select()
            elif answer == 'n':
                decline()
        elif answer == 'n':
            decline()

def summary_select():
    print('This is your total Budget / Spent / Left over!')
    for x in masterlist:
        padding = 15 - len(x)
        print(f'{x}:' + items_budget[f'{x}'] + '|' + items_spent[f'{x}'].center(14) + "|" + str(int(items_budget[f'{x}']) - int(items_spent[f'{x}'])))

mainscreen_select()