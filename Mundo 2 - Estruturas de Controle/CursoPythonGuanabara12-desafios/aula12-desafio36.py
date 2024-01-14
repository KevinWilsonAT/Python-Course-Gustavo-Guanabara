house_price = float(input('How much does the house cost? '))
salary = float(input('How much do you get per month? '))
loan_years = int(input('For how many years do you want to pay? '))
installments = house_price / (loan_years * 12)
limit = salary * 0.3

print('House price: R${:.2f}'.format(house_price))
print('Years of installment payment: {}'.format(loan_years))
print('Installment price: R${:.2f}'.format(installments))

if installments <= limit:
    print('The loan can be granted!')
else:
    print('The loan was denied!')
