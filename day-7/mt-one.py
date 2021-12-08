from collections import defaultdict

values = [int(i) for i in open('./input.txt','r').readline().strip().split(',')]

spent = defaultdict(int)

for value in values:
    # already calculated the cost to get to that spot
    if value in spent:
        continue

    totalFuelUsed = 0
    runner = 0
    
    while runner < len(values)-1:
        totalFuelUsed+= abs(value - values[runner])
        runner+=1
    spent[value] = totalFuelUsed
    
print('spent: %s, valuesLength: %s' % (len(spent), len(values)))
leastFuelUsed = min(spent, key=spent.get)
print('least fuel used is %s' % spent[leastFuelUsed] )
print('checked %s spots' % len(spent))


