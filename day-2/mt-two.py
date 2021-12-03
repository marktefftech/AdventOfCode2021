with open('./input.txt') as f:
    instructions = f.read().split('\n')
    x, y, aim = 0, 0, 0

    # ['forward 7', 'forward 9', 'down 1', 'up 6']
    for i in instructions:
        #'forward 7'
        i = i.split(' ')
        #['forward'  '7']
        direction, value = i[0], int(i[1])

        if direction == 'forward':
            x+= value
            y+= value * aim

        elif direction == 'down':
            aim+= value

        else:
            aim-= value

    # now we have final coords save as x, y 
    print('final coords are %s, %s' % (x, y))
    print('final position is %s' % (x*y))