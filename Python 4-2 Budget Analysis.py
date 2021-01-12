# This looped program asks user to enter the
# amount that they have bdigeted for the month.
print('Enter the budgeted amount')
print(' or enter 0 to end')
budget = float(input('Enter budgeted amount: $'))   # Budgeted Amount
another = 'y'                                       # Variable to control loop
expense = float(input("Enter expense: $"))          # Expenses

# Continue processing expenses as long
# as user does not enter 0.
while expense != 0:

    # Display budget balance after expenses.
    budget -= expense                               # Unused Budget Remaining

    expense = float(input("Enter expense: $"))          # Expenses
 
# Display Remaining Budget
print('The Balance Budget Amount: $ ',
format(budget, ',.2f'), sep='')















               
