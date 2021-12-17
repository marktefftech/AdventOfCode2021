# Time O(n) Space 0(1)
from collections import defaultdict

def analyze(digits, digitCounter):
        # ['bf', 'defbag', 'efadgbc', 'bfgeda']
        tmp = 0
        print(digitCounter)
        for i in digits:
            # 'bf' 2
            runningSum = 0
            for chunk in i:
                check = ''.join(sorted(chunk))
                if check in digitCounter.values():
                    numberFound = list(digitCounter.keys())[list(digitCounter.values()).index(check)]
                    runningSum = runningSum*10 + numberFound
                    # digitCounter[numberFound]+=1 
                    # print(runningSum)
            tmp+= runningSum
        return tmp

def main():
    # SEGMENT_VALUES = {2: 1, 4: 4, 3: 7, 7:8}
    unsortedVals = {8: 'acedgfb', 5: 'cdfbe',  2: 'gcdfa', 3: 'fbcad', 7: 'dab', 9: 'cefabd', 6: 'cdfgeb', 4: 'eafb', 0: 'cagedb', 1: 'ab'}

    c=0
    digitCounterDict = defaultdict(int)
    while c < len(unsortedVals):
        tmpStr = ''.join(sorted(unsortedVals[c]))
        digitCounterDict[c] = tmpStr    
        c+=1
        # {1: bf, 2: aaddff  ... }
    
    print(digitCounterDict)
    outputDigits = []
    with open('/Users/mteffeteller/AoC2021/day-8/input.txt', 'r') as f:
        for line in f:
            data = line.strip().split('|')
            outData = data[1].strip().split()
            outputDigits.append(outData)

    # part1 = analyze(outputDigits, digitCounterDict, SEGMENT_VALUES)
    # print('digits 1, 4, 7, or 8 appear %s times' % (part1))
    part2 = analyze(outputDigits, digitCounterDict)
    print('add up all of the output values: %s' % (part2))
        
main()

