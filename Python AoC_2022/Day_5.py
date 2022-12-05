#preberi space in dodaj, 3 space character, 1 space naslednji
stack =[]
for _ in range(0,9):
    stack.append([])

while(True):
    g = input()
    if g=="-1":
        break
    if not g.startswith("move") and not g.startswith("1"):
        for j in range(0,len(g)):
            if j%4==0 and g[j]!= " ":
                stack[j//4].append(g[j+1])
    elif g.startswith("move"):
        stavek = g.split(" ")
        b = ""
        for i in range(0,int(stavek[1])):
            #part II, dodaj samo na zacetek vse hkrati
            a = stack[int(stavek[3]) - 1].pop(0)
            b+=a
            #Uncomment za part I
            #stack[int(stavek[5])-1].insert(0,a)
        #comment za part I
        for i in range(len(b),0,-1):
            stack[int(stavek[5]) - 1].insert(0, b[i-1])

odgovor=""
for k in range(0,9):
    odgovor+=stack[k][0]
print(stack)
print(odgovor)