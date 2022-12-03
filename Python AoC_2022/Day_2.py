
# A = ROCK = X = 1
# B = PAPER = Y = 2
# C = SCISSORS = Z = 3
sum=0
sum_2 = 0
# X = LOSE
# Y = DRAW
# Z = WIN
while(True):
    g=input()

    if g=="":
        break
    if(g[0]=="A"):
        if g[2]== "Y":
            sum+=8
            sum_2+=4 # draw+1 = 3+1
        elif g[2]=="X":
            sum+=4
            sum_2+=3 # lose+3 = 0+3
        else:
            sum+=3
            sum_2+=8 # win +2 = 6+2
    if g[0]=="B":
        if g[2]== "Y":
            sum+=5
            sum_2+=5# draw+2 = 3+2
        elif g[2]=="X":
            sum+=1
            sum_2+=1#lose + 1 = 0+1
        else:
            sum+=9
            sum_2+=9 # win +3 = 6+3
    if g[0]=="C":
        if g[2]== "Y":
            sum+=2
            sum_2+=6# draw+3 = 3+3
        elif g[2]=="X":
            sum+=7
            sum_2+=2 # lose+2 = 0+2
        else:
            sum+=6
            sum_2+=7 # win+1 = 6+1

print(sum)
print(sum_2)
