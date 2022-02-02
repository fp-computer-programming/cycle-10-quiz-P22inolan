# Author: IBN (AMDG) 2/2/2022
prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip', 'half-zip']]

def item_costs(item, price):
    item_mod = item # set item_mod equal to item to wokr inside item list
    x = 0
    for lst in item: # for specific list in items array:
        for i,v in enumerate(lst): # enumerate items in list
            lst[i] = "{0} ${1}".format(v, price[x]) # format the item with the price next to it
            x += 1 # continue price count
            i += 1 # continue item count
    return item_mod

print(item_costs(items, prices) == [['tee-shirt $30', 'long-sleeved $40', 'tanktop $25'], ['quarter-zip $55', 'pullover $60', 'full-zip $80', 'half-zip $65']]) 
