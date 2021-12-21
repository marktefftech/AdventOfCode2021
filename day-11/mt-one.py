# ['5723573158']
# ['3154748563']
# 4783514878
# 3848142375
# 3637724151
# 8583172484
# 7747444184
# 1613367882
# 6228614227
# 4732225334

G = [] 
for line in open('./input.txt', 'r'):
    G.append([int(i) for i in line.strip()])

rows = len(G)
cols = len(G[0])

ans = 0
def flash(r, c):
    global ans
    ans+=1
    # change the value to flashed
    G[r][c] = -1
    # for each of the surrounding values 
    for dr in [-1,0,1]:
        for dc in [-1, 0, 1]:
            # get the new coordinates
            rr = r+dr
            cc = c+dc
            # check against 0 not to go outside grid
            if 0<=rr<rows and 0<=cc<cols and G[rr][cc] != -1:
                G[rr][cc] += 1
                if G[rr][cc] >=10:# why do we check greater than 10 vals here?
                    flash(rr,cc)
t=0
while True:
    t+=1
    for r in range(rows):
        for c in range(cols):
            G[r][c] +=1
    
    for r in range(rows):
        for c in range(cols):
            if G[r][c] == 10:
                flash(r,c)

    done = True
    for r in range(rows):
        for c in range(cols):
            if G[r][c] == -1:
                G[r][c] = 0
            else:
                done = False
    
    if done:
        print(t)
        break

# steps = 0
# while True:
#     steps += 1
#     for r in range(rows):
#         for c in range(cols):
#             G[r][c] += 1
#     for r in range(rows):
#         for c in range(cols):
#             if G[r][c] == 10:
#                 flash(r,c)
#     done = True
#     for r in range(rows):
#         for c in range(cols):
#             if G[r][c] == -1:
#                 G[r][c] = 0
#             else:
#                 done = False
#     if steps == 100:
#         print(ans)
#         break
#     if done:
#         print(steps)
#         break