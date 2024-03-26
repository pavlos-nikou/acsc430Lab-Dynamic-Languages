TAX = 0.19

print("Enter the price of each item:")
total = 0

for i in range (5):
    total += float(input(f'  {i+1})'))

tax = total * TAX

print(f'\n\nTotal Amount(without TAX):{total:.2f}\nTax: {tax:0.2f}\nTotal With TAX: {total + tax:.2f}')