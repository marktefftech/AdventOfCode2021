
with open('./input.txt', 'r') as f:
    increase = 0
    values = f.read().split('\n');

    cursor = 0

    for i in values:
        cur = int(values[cursor])

        try:
            nex = int(values[cursor+1])
        except:
            break

        if (nex - cur) > 0:
            increase+=1
        cursor+=1
    
    print(increase)
    