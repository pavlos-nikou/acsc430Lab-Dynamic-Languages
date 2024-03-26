stocks= 1000
stock_price_on_purchase = 32.87 * stocks
stock_price_on_sale = 33.92 * stocks
commition = 0.02

print(f'Purchase Amount: {stock_price_on_purchase:>26.2f}')
print(f'Sold Amount: {stock_price_on_sale:>30.2f}')
commition_amount_purchase = stock_price_on_purchase * commition
print(f'Commitions Amount(purchase): {commition_amount_purchase:>14.2f}')
commition_amount_sale = stock_price_on_sale * commition
print(f'Commitions Amount(sale): { commition_amount_sale:>18.2f}')

returnAmount = (stock_price_on_sale - commition_amount_sale) - (stock_price_on_purchase - commition_amount_purchase)
if returnAmount >= 0:
    returns = "Gained"
else:
    returns = "Lost  "
print(f'Total Amount {returns}: {returnAmount:>22.2f}')