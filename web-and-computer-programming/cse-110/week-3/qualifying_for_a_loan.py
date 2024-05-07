# Activity Instructions:
# For this activity, you will implement a simplistic system
# to determine if a user can qualify for a loan.

print("Please, answer the following questions with a rating from 1–10:")
loan_size = int(input("\nHow large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

can_loan = False

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        can_loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            can_loan = True
        else:
            can_loan = False
    else:
        can_loan = False
else:
    if credit < 4:
        can_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            can_loan = True
        elif income >= 4 and down_payment >= 4:
            can_loan = True
        else:
            can_loan = False

if can_loan:
    print("Loan decision is yes.")
else:
    print("Loan decision is no.")
