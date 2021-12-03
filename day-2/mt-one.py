with open('./input.txt') as f:
    instructions = f.read().split('\n')
    x, y = 0, 0

    # ['forward 7', 'forward 9', 'down 1', 'up 6']
    for i in instructions:
        i = i.split(' ')
        # ['forward',  '7']
        direction, value = i[0], int(i[1])
        # ['up',  7]

        if direction == 'down':
            y+= value
        elif direction == 'up':
            y-= value
        else:
            x+= value
    
    # now we have final coords save as x, y 
    print('final coords are %s, %s' % (x, y))

    print('final position is %s' % (x*y))

    #def calculateCoordinates(x: int, y: int) -> coordinates:
