from collections import defaultdict, Counter

class School():
    def __init__(self):
        self.lifetime = 0

def main(values):
    school = School()
    print('initially there are %s fish' % (len(values)))

    values = Counter(values)
    print(values)
    # [0: 2355, 1: 1234, 2: 4325, 3: 2345]
    
    while school.lifetime < 256:
        fishDict = defaultdict(int)
        for v in values:
            if v > 0:
                fishDict[v-1]+= values[v]
            else:
                # fish counter is zero
                fishDict[6] += values[v]
                fishDict[8] += values[v]
        values = fishDict 
        school.lifetime+=1
        
        print('After day %s there are %s fish' % (school.lifetime, sum(values.values())))
        
   

values = [int(i) for i in open('./input.txt','r').read().strip().split(',')]

main(values.copy())

