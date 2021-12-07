with open('./input.txt', 'r') as f:
    values = f.read().split('\n');
    #['101000101000', '010101110101', '011100011100']
    comparator = len(values) / 2

    # this can be done dynamically
    columnCounter = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

    #['101000101000']
    for i in values:
        nums = list(i)
        index = 1
        #['1','0','1','0']
        for n in nums:
            if int(n) == 1:
                columnCounter[index]+=1
            index+=1

    gamma = ''
    epsilon = ''
    
    # columnCounter = {1:124, 2:535, 5:355}
    idx=1
    for k in columnCounter:
        if columnCounter[idx] > comparator:
            gamma+= str(0)
        else:
            gamma+= str(1)
        idx+=1

    for n in gamma:
        if n == '0':
            epsilon+= str(1)
        else:
            epsilon+= str(0)

    print(columnCounter)
    print('final gamma is %s, or %s' % (gamma, int(gamma,2)))
    print('final epsilon is %s, or %s' % (epsilon,int(epsilon,2)))
    final = int(gamma,2) * int(epsilon,2)
    print('final power is %s' % final )

    

