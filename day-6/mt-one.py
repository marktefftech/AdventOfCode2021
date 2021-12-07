class School():
    def __init__(self):
        self.lifetime = 0

    def reproduceDaily(self, fishies: list) -> list:
        zeroCounter = 0 
        tempFish = []
        for fish in fishies:
            if fish == 0:
                tempFish.append(6)
                zeroCounter+=1
                continue
            else:
                tempFish.append(fish-1)
        
        while zeroCounter > 0:
            tempFish.append(8)
            zeroCounter-=1

        return tempFish

def main(values):
    school = School()
    print('initially there are %s fish' % (len(values)))
    while school.lifetime < 80:
        # be sure to call the method on the class object
        school.lifetime+=1
        values = school.reproduceDaily(values)
        print('After day %s there are %s fish' % (school.lifetime, len(values)))
        
   
with open('./input.txt', 'r') as f:
        values = f.read().split(',')
        values = list(map(int, values))

main(values)

