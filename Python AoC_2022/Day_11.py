class Monkey:

    inspect = 0
    def __init__(self,id,items,op,test,true,false):
        self.id =  id
        self.items = items
        self.operation = op
        self.test = test
        self.true = true
        self.false = false

    def pop_item(self,item):
        return self.items.pop(item)

    def dodaj(self,item):
        self.items.append(item)
    def oper(self,item): #inspect
        izraz = self.operation
        self.inspect+=1
        new = self.items[item]
        if izraz[3]=="+":
            new+= self.items[item] if izraz[4]=="old" else int(izraz[4])
        if izraz[3] == "*":
            new *= self.items[item] if izraz[4] == "old" else int(izraz[4])
        self.items[item] = new
    def attr(self):
        att= vars(self)
        return ", ".join("%s: %s"% item for item in att.items())

monkeys=[]
items = []
cur_monkey=0
oper=""
zmnozek=1
while(True):
    g = input()
    if g=="":
        monkeys.append(Monkey(cur_monkey,items,oper,test,tru,fal))
        items=[]
        continue
    if g=="-1":
        break

    g= g.strip().split()
    if g[0]=="Monkey":
        cur_monkey=g[1][:-1]
    elif g[0]=="Starting":
        items = [int(x) for x in "".join(g[2:]).split(",")]
    elif g[0]=="Operation:":
        oper = g[1:]
    elif g[0]=="Test:":
        test = int(g[-1])
        zmnozek*=test
    elif g[1]=="true:":
        tru = g[-1]
    elif g[1]=="false:":
        fal = g[-1]

#zacni s premetavanjem
for i in range(0,10000):
    print("run: ",i+1)
    for j in monkeys:
        for k in range(0,len(j.items)):
            j.oper(k) # inspect item
            #Uncomment za part I j.items[k]//=3
            #j.items[k]//=3
            j.items[k]%=zmnozek
            if j.items[k]%j.test == 0:
                monkeys[int(j.true)].items.append(j.items[k])
            else:
                monkeys[int(j.false)].items.append(j.items[k])
        j.items=[]
        #print(j.attr())

inspect_list = []
for i in monkeys:
    print("%s , Monkey %s inspected %s"%(i.items,i.id,i.inspect))
    inspect_list.append(i.inspect)
inspect_list.sort(reverse=True)
print(inspect_list[0]*inspect_list[1])