# Author: IBN (AMDG) 2/2/2022
prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip', 'half-zip']]

def average():
    x = 0 # create counter for prices
    average = 0 # blank number for adding prices
    for num in prices:
        average += float(prices[x]) # adding each price to average
        x += 1 # increasing count
    average /= float(len(prices)) # average = average / the length of the list
    return average
print(average() == (30+40+25+55+60+80+65) / 7) # test case
