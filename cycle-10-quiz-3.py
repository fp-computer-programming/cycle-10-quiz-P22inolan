# Author: IBN (AMDG) 2/2/2022
prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip', 'half-zip']]

def overfourty(lst):
    for i in range(len(lst)): # for each i in the list:
        if lst[i] > 40: # if the value is greater than 40:
            lst[i] -= 10 # subtract 10 from value
    return lst # return the list

print(overfourty(prices) == [30, 40, 25, 45, 50, 70, 55]) # test case