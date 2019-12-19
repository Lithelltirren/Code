def mainscreen_select():
    main_catagory_select = input('What would you like to view?\nBudget, Spend, or Summary\n\n')
    if main_catagory_select.lower() == 'budget':
        budget_select()
    elif main_catagory_select.lower() == 'spend':
        spent_select()
    elif main_catagory_select.lower() == 'summary':
        summary_select()
    else:
        print('You have made an invalid selection, restarting.')
        mainscreen_select()
    
def budget_select():
    global main_catagory_select
    main_catagory_select = input(('\n'*20) + 'Please type "all" or choose from one of the following catagories!\n' + str(masterlist).replace("'", '') + "\n\n")
    if main_catagory_select in items_budget.keys():
        answer_input = input(f'You want to edit {main_catagory_select}? yes/no\n\n')
        if (answer_input.lower() == 'yes') or (answer_input.lower() == 'y'):
            budget_modify()
        elif (answer_input.lower() == 'no') or (answer_input.lower() =='n'):
            mainscreen_select()
        else:
            print('Error: Returning to budget screen.')
            budget_select()
    elif (main_catagory_select.lower() == 'all'):
        all_budget_mod()
    else:
        print('Error: Returning to budget screen.')
        budget_select()
        
def budget_modify():
    global main_catagory_select
    amount_answer = (input(f'\n'*20 + f'What you would like to set {main_catagory_select} to? \nIt is currently $' + str(items_budget[main_catagory_select]) + '\n\n$'))
    items_budget[main_catagory_select] = amount_answer
    answer_check = input(f'You changed {main_catagory_select} to {amount_answer}!\n\nWould you like to edit more budgets? yes/no\n\n')
    if (answer_check.lower() == 'yes') or (answer_check.lower() == 'y'):
        budget_select()
    elif (answer_check.lower() == 'no') or (answer_check.lower() =='n'):
        mainscreen_select()
    else:
        print('Error: Returning to budget screen.')
        mainscreen_select()

def spent_select():
    global main_catagory_select 
    main_catagory_select = input(('\n'*20) + 'Please type "all" or choose from one of the following catagories!\n' + str(masterlist).replace("'", '') + "\n\n")
    if (main_catagory_select.lower() in items_spent.keys()):
        answer = input(f'You want to edit {main_catagory_select}? yes/no\n\n')
        if (answer.lower() == 'yes') or (answer.lower() == 'y'):
            spent_modify()
        elif (answer.lower() == 'no') or (answer.lower() == 'n'):
            mainscreen_select()
        else:
            print('Error: Returning to budget screen.')
            budget_select()
    elif (main_catagory_select.lower() == 'all') or (answer.lower() == 'a'):
        all_spent_mod()
    else:
        mainscreen_select()

def spent_modify():
    global main_catagory_select
    amount_answer = (input(f'\n'*20 + f'What you would like to set {main_catagory_select} to? $'))
    items_spent[main_catagory_select] = amount_answer
    answer_check = input(f'You changed {main_catagory_select} to {amount_answer}!\nWould you like to edit more spends? yes/no\n\n')
    if (answer_check.lower() == 'yes') or (answer_check.lower() == 'y'):
        spent_select()
    elif (answer_check.lower() == 'no') or (answer_check.lower() =='n'):
        mainscreen_select()
    else:
        print('Error: Returning to spend screen.')
        mainscreen_select()

#still needs total spent and saved
def summary_select():
    total_budget = 0
    total_spent = 0
    print('\n'*20 +'This is your total Budget / Spend / Left over!')
    for x in masterlist:
        padding = 15 - len(x)
        print(f'{x}:' + str(items_budget[f'{x}']).rjust(padding) + '|' + str(items_spent[f'{x}']).center(14) + "|" + str(int(items_budget[f'{x}']) - int(items_spent[f'{x}'])))
        if x != "paycheck":
            total_budget += int(items_budget[x])
            total_spent += int(items_spent[x])
    print('\n\nYour combined budgets are $' + str(f'{total_budget}\nYour combined spend is {total_spent}'))
    answer_check = input('\n\nWould you like to perform another transaction?' 'yes / no')
    if (answer_check.lower() == 'yes') or (answer_check.lower() == 'y'):
        mainscreen_select()
    if (answer_check.lower() == 'no') or (answer_check.lower() == 'n'):
        exit()

#############################################################################################
    for key in masterlist:
        str_len = len(key)
        padding = 25 - str_len
        print(key + ":" + str(f"{item_spent[key]:.>{padding}}/{item_budget[key]} dollars"))
        if key != "paycheck" :
            total_budget += int(item_budget[key])
            total_spent += int(item_spent[key])
#############################################################################################










  

def all_budget_mod():
    for x in items_budget:
        items_budget[x] = input(f'How much for {x}? It is currently $' + str(items_budget[x]) + "\n\n")
    mainscreen_select()
def all_spent_mod():
    for x in items_spent:
        items_spent[x] = input(f'How much for {x}? It is currently $' + str(items_spent[x]) + "\n\n")
    mainscreen_select()

masterlist = ('paycheck','rent','games','power','water','internet','car','pet','gas','food')
items_budget = {}
items_spent = {}
for x in masterlist:
    items_budget[f'{x}'] = 0
    items_spent[f'{x}'] = 0

main_catagory_select = ()
answer_input = ()
answer_input2 = ()
spent_catagory_selected = ()

mainscreen_select() 