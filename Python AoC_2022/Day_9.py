from collections import defaultdict

grid = defaultdict(int)
#grid={} # na zacetku je empty, start je na 0,0
col_t,row_t,col_h,row_h = 0,0,0,0 #tail row in column
tail_list=[]
#part II vsak tail je head naslednjega torej [0,1,2,..,9] 0 je head 1, 1 je head 2 itd.
for i in range(0,10):
    tail_list.append([0,0])
#preberi komando in se iterativno premakni tja, zapolni dictionary s prištevanjem
grid["0,0"]=1
def premakni_tail(t_r,t_c,h_r,h_c):
    if abs(t_r-h_r)<=1 and abs(t_c-h_c)<=1:
        return "0"
    a = ""
    if t_r-h_r !=0 and t_c-h_c != 0: # ce je stran diagonalno
        if t_r < h_r: # ce se tail nahaja spodaj
            a+="U"
        else:
            a+="D"
        if t_c < h_c: # ce se tail nahaja levo
            a+="R"
        else:
            a+="L"
    else:
        if t_r-h_r<0: # ce se tail nahaja spodaj
            a="U"
        if t_r-h_r>0: # ce se tail nahaja zgoraj
            a="D"
        if t_c-h_c<0: # ce se tail nahaja levo
            a="R"
        if t_c-h_c>0: # ce se tail nahaja desno
            a="L"
    return a

while(True):
    g = input()
    if g=="":
        break
    g= g.split()
    for i in range(0,int(g[1])): # premakni head v primerno smer

        #print("tail:", row_t,col_t, "head: ",row_h,col_h)
        if g[0]=="R":
            col_h+=1
            tail_list[0][1]+=1
        elif g[0]=="L":
            col_h-=1
            tail_list[0][1] -= 1
        elif g[0]=="U":
            row_h+=1
            tail_list[0][0] += 1
        elif g[0]=="D":
            row_h-=1
            tail_list[0][0] -= 1
        pr = premakni_tail(row_t, col_t, row_h, col_h)

        for j in range(1,10):
            premik= premakni_tail(tail_list[j][0], tail_list[j][1], tail_list[j-1][0],tail_list[j-1][1])
            for k in premik:
                if k == "R":
                    tail_list[j][1] += 1
                if k == "U":
                    tail_list[j][0] += 1
                if k == "D":
                    tail_list[j][0] -= 1
                if k == "L":
                    tail_list[j][1] -= 1
            if j==9 and premik != "0":
                grid[",".join([str(tail_list[j][0]), str(tail_list[j][1])])] += 1
        # print(pr)
        for j in pr:
            if j == "R":
                col_t += 1
            if j == "U":
                row_t += 1
            if j == "D":
                row_t -= 1
            if j == "L":
                col_t -= 1
        #if pr[0]!="0":
        #    grid[",".join([str(row_t),str(col_t)])]+=1
sum=0
for k,v in grid.items():
    if v>0:
        sum+=1
print(sum)
