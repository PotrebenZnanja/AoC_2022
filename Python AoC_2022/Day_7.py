from collections import defaultdict
path=[]
dic = defaultdict(int)
while(True):
    g = input()
    if g=="":
        break
    stavek = g.strip().split()
    if stavek[1] == "cd":
        if stavek[2] == "..":
            path.pop()
        else:
            path.append(stavek[2])
    elif stavek[1] == "ls":
        continue
    else:
        try:
            val = int(stavek[0])
            #print(path,val)
            for i in range(1,len(path)+1):
                print(i)
                dic['/'.join(path[:i])] +=val
            print(dic)
        except:
            pass
a = 0
meja = 40000000
za_spraznit = dic["/"]-meja
p2 = 1e9
print("Za spraznit je: ",za_spraznit)
for k,v in dic.items():
    if v<=100000:
        a+=int(v)
    if v>= za_spraznit:
        p2 = min(p2,v)
print(a)
print(p2)


