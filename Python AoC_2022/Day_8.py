tab = []
tru = []

while(True):
    g = input()
    if g == "":
        break
    a = []
    for i in g:
        a.append(int(i))
    tab.append(a)

for i in range(len(tab)):
    a = []
    for j in range(len(tab[0])):
        a.append(False)
    tru.append(a)

#zacni gledat
for i in range(len(tab)):
    min = -1
    for j in range(len(tab[0])):
        if tab[i][j]>min:
            min=tab[i][j]
            tru[i][j]=True
    min = -1
    for j in range(len(tab[0])-1,-1,-1):
        if tab[i][j]>min:
            min=tab[i][j]
            tru[i][j]=True
#glej gor in dol
for i in range(len(tab[0])):
    min = -1
    for j in range(len(tab)):
        if tab[j][i]>min:
            min=tab[j][i]
            tru[j][i]=True
    min = -1
    for j in range(len(tab)-1,-1,-1):
        if tab[j][i]>min:
            min=tab[j][i]
            tru[j][i]=True

st_videnih = 0
for i in range(len(tru)):
    for j in range(len(tru[0])):
        if tru[i][j]:
            st_videnih+=1
print(st_videnih)
#part 2
score=[]
for i in range(len(tab)):
    a = []
    for j in range(len(tab[0])):
        a.append(0)
    score.append(a)

for i in range(1,len(tab)-1):
    for j in range(1,len(tab[0])-1):
        #sedaj se nahajam na mestu tab[i][j]
        gor,dol,levo,desno = 1,1,1,1
        #glej gor
        for k in range(i-1,0,-1):
            if tab[k][j]<tab[i][j]:
                gor+=1
            else:
                break
        # glej dol
        for k in range(i + 1, len(tab)-1):
            if tab[k][j] < tab[i][j]:
                dol += 1
            else:
                break
        #glej desno
        for k in range(j+1,len(tab[0])-1):
            if tab[i][k]<tab[i][j]:
                desno+=1
            else:
                break
        #glej levo
        for k in range(j-1,0,-1):
            if tab[i][k]<tab[i][j]:
                levo+=1
            else:
                break
        print(gor,dol,levo,desno, "indeks: ",i,j)
        score[i][j]=gor*dol*levo*desno

maks = 0
for i in range(len(score)):
    print(score[i])
    for j in range(len(score[0])):
        if score[i][j]>maks:
            maks = score[i][j]
print(maks)
