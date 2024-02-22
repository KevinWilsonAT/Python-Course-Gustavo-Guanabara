value = int(input('How much do you want to withdraw? R$'))
total = value
money_note = 200
total_m_n = 0

while True:
    if total >= money_note:
        total -= money_note
        total_m_n += 1
    else:
        if total_m_n > 0:
            print(f'You will withdraw {total_m_n} notes of R${money_note:.2f}')
        if money_note == 200:
            money_note = 100
        elif money_note == 100:
            money_note = 50
        if money_note == 50:
            money_note = 20
        elif money_note == 20:
            money_note = 10
        elif money_note == 10:
            money_note = 5
        elif money_note == 5:
            money_note = 2
        elif money_note == 2:
            money_note = 1
        total_m_n = 0
        if total == 0:
            break
print('PROCESS ENDED')
