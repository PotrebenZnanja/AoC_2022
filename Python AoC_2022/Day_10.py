val = 1

cikel = 0
signal=[]
CRT = ""
while(True):
    g = input()
    cik_prej=cikel
    if g=="":
        break
    g = g.split()
    #Insert code kle za part II
    if val-cikel%40>=-1 and val-cikel%40<=1:
        CRT+="#"
    else:
        CRT+="."
    #---
    if g[0]=="noop":
        cikel+=1
    elif g[0]=="addx":
        cikel+=1
        if val - cikel%40 >= -1 and val - cikel%40<= 1:
            CRT += "#"
        else:
            CRT += "."
        cikel+=1
    #part I
    if cikel%40==20:
        signal.append(cikel*val)
    elif g[0]=="addx" and cikel%40==21:
        signal.append((cikel-1)*(val))
    if g[0]=="addx":
        val += int(g[1])

for i in range(40,len(CRT)+1,40):
    print(CRT[i-40:i])
print(signal)
print(sum(signal))