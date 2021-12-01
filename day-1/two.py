with open('./input.txt', 'r') as f:
    values = f.read().split('\n')
    comparisonArr = (0,0)
    cursor = 0
    increases = 0

    while cursor < len(values) - 2:
        try:
            value1 = int(values[cursor])
            value2 = int(values[cursor+1])
            value3 = int(values[cursor+2])
            value4 = int(values[cursor+3])
            threeSum1 = value1 + value2 + value3
            threeSum2 = value2 + value3 + value4
            if threeSum2 - threeSum1 > 0:
                increases+=1
            cursor+=1
        except:
            print('except')
            break
    print(increases)

    




# 1
# 4
# 6
# 1
# 5
# 4
# 2

# 11
# 11
# 12
# 10
# 11

# (1,4,6,1,5)
#      ^ ^ ^
# (11,12)

# if nex - cur > 0 