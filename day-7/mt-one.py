values = [int(i) for i in open('./input.txt','r').readline().strip().split(',')]

costs = []

def get_cost(a, b):
    n = abs(a - b)
    return (n*(n+1))//2

for pos in range(min(values), max(values)+1):
    # costs.append(sum(abs(i - pos) for i in values))
    costs.append(sum(get_cost(i,pos) for i in values))

print(min(costs))