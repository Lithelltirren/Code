# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#dictionary creation
masterlist = ('paycheck','rent','games','power','water','internet','car','pet','gas','food')
item_budget = {}
item_spent = {}

for x in masterlist:
    item_budget[f'{x}_budget'] = 0
    item_spent[f'{x}_spent'] = 0

print("Please enter the following amounts for budgets.")

for x in item_budget:
    item_budget[x] = int(input(f"How much for {x}? $"))


print('You entered:')
for key in item_budget:
    print(key + ":" + " $" + {str(item_budget[key]:>20)})
    
test = "right_align"
print(f"{test:>50}")
    