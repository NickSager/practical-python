# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

print('Month Total_Paid Principal')
while principal > 0:
    if principal > payment:
        principal = principal * (1+ rate/12) - payment
        if month >= extra_payment_start_month and month <= extra_payment_end_month: 
            principal = principal - extra_payment
            total_paid = total_paid + extra_payment
        total_paid = total_paid + payment
    else:
        total_paid = total_paid + principal
        principal = 0
    month += 1
    # print(month, round(total_paid, 2), round(principal, 2))
    print(f'{month:3d} {total_paid:10.2f} {principal:10.2f}')
    
# print('Total paid:', round(total_paid, 2))
print(f'Total paid: ${total_paid:0.2f}')
# print('Months required:', month)
print(f'Months required: {month:0d}')
