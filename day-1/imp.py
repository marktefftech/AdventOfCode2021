
# Put values into a list
# Be sure to explicitly state list()    
values = list(int(a) for a in open('./input.txt').readlines())

print(sum((a < b) for a, b in zip(values, values[1:])))

# woah i actually wrote and understand this. good job so far :) 
# don't give up