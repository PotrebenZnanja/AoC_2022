sum =0
sum2=0
while(True):
    g = input()
    if g=="":
        break
    h = g.split(",")
    par = []
    for k in h:
        a = k.split("-")
        for j in a:
            par.append(int(j))
    if (par[0]<=par[2] and par[1]>=par[3]) or (par[0]>=par[2]and par[1]<=par[3]):
        sum+=1

    #part II
    if not( par[0]>par[3] and par[1]>par[2] or par[0]<par[3] and par[1]<par[2]):
        print(par)
        sum2+=1

print(sum, sum2)