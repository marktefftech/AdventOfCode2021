# 309,347 -> 309,464
# 425,687 -> 300,687

# (309,347) (309, 464)
# found = (309, 347), (309, 348)....(309, 347)
# foundCount = (309, 347): 2

with open('./input.txt') as f:
    found = [[]]

    for line in f:
        
        coordinates = line.replace(' -> ', ',').strip('\n').split(',')
        #(309, 467, 309, 464)
        # 309 == 309
        if coordinates[0] == coordinates[2]:
            # found a vertical line
            verticalLineLength = int(coordinates[3]) - int(coordinates[1])
            # 464 = 347 = 87
            if verticalLineLength >= 0:
                while verticalLineLength >= 0:
                    found.append(list((int(coordinates[0]),(int(coordinates[1])+verticalLineLength))))
                    #found [(309,464), (309,463)]
                    verticalLineLength-= 1
            else:
                while verticalLineLength <= 0:
                    found.append(list((int(coordinates[0]),(int(coordinates[1])+verticalLineLength))))
                    #found [(309,464), (309,463)]
                    verticalLineLength+=1
        
        # 300,687, 425, 687
        if int(coordinates[1]) == int(coordinates[3]):
            # found a horiztontal line
            # 425 - 300 = 125
            horizontalLineLength = int(coordinates[2]) - int(coordinates[0])

            # increment 
            if horizontalLineLength >= 0:
                while horizontalLineLength >=0:
                    found.append(list(((int(coordinates[0])+horizontalLineLength), int(coordinates[1]))))
                    horizontalLineLength-=1

            else:
                while horizontalLineLength <= 0:
                    found.append(list(((int(coordinates[0])+horizontalLineLength), int(coordinates[1]))))
                    horizontalLineLength+=1

    ## found = (309, 347), (309, 348)....(309, 347)
    foundCount = {}
    
    for xy in found:
        xy = ''.join(str(xy))
        if xy not in foundCount:
            foundCount[xy] = 1
        else: 
            foundCount[xy] += 1

    hotspots = 0    

    for coord in foundCount:
        # print(foundCount[coord])
        if foundCount[coord] >1:
            hotspots+=1

    print('number of hotspots: %s' % (hotspots))
    


            
                


        
