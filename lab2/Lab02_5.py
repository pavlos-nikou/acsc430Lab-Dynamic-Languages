totalCost = float(input("Enter the total ammount: "))
tip = totalCost * 0.1
salesTax = totalCost * 0.05

print(f'tip: {tip:^7.2f}\tsales tax: {salesTax}\tafter Tax:{totalCost+tip+salesTax:^10.2f}')