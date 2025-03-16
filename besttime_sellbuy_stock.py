price=[7,1,5,3,6,4]

min_price=price[0]
max_profit=0

for i in price:
    if i<min_price:
        min_price=i
    potential_profit=i-min_price
    if potential_profit>max_profit:
        max_profit=potential_profit

print(max_profit)            

