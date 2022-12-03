sum=0
stavki=[]
while(True):
    g=input()
    stavki.append(g)
    if(g==""):
        break
    vrni=False
    for i in range(len(g)//2):
        for j in range(len(g)//2,len(g)):
            if g[i]==g[j]:
                crka=ord(g[i])-96
                if crka < 0:
                    crka=ord(g[i])-65+27
                sum+=crka
                vrni=True
                break
        if vrni:
            break
print(sum)
#part II
sum2=0
vrni=False
for i in range(0,len(stavki),3):
    vrni=False
    for j in stavki[i]:
        if j in stavki[i+1] and j in stavki[i+2]:
            crka = ord(j) - 96
            if crka < 0:
                crka = ord(j) - 65 + 27
            sum2 += crka
            break

print(sum2)