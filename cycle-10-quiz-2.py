# Author: IBN (AMDG) 2/2/2022
prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip', 'half-zip']]

def price_cutter(price):
    for i in range(len(price)): # for each i in the list:
        price[i] -= 5 # subtract 5 from value
    return price # return list

print(price_cutter(prices) == [25, 35, 20, 50, 55, 75, 60]) # Test case
