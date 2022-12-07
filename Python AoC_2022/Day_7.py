from collections import defaultdict
path=[]
dic = defaultdict(int)
dicl = {}
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
            for i in range(len(path)+1):
                print('/'.join(path[:i]))
                if '/'.join(path[:i]) not in dicl:
                    dicl['/'.join(path[:i])] = val
                else:
                    dicl['/'.join(path[:i])] += val
                dic['/'.join(path[:i])] +=val
        except:
            pass
a = 0
meja = 40000000
za_spraznit = dic["/"]-meja
p1 = 0
p2 = 1e9
print("Za spraznit je: ",za_spraznit)
for k,v in dic.items():
    if v<=100000:
        a+=int(v)
    if v>= za_spraznit:
        p2 = min(p2,v)
print(a)
print(p1)
print(p2)
