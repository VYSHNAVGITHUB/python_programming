fixed_amount=100000
withdrawal_amount=float(input('enter the amount to withdraw'))
balance_amount=fixed_amount-withdrawal_amount
if fixed_amount>=withdrawal_amount:
    print('your ac has been debited the amount of rs. ', withdrawal_amount)
    print('your balance is', balance_amount)
else:
    print('insufficient balance')

