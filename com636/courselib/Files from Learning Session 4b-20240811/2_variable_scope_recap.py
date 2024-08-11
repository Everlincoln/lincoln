
interest_rate = 0.05

def interest_calc():
    interest = interest_rate * balance
    return interest

def balance_calc(balance_local):
    balance_local = balance_local + interest
    # print()
    return balance_local

amount_borrowed = 10000
balance = amount_borrowed

for period in range(13):
    interest = interest_calc()
    balance = balance_calc(balance)
    print(balance)

