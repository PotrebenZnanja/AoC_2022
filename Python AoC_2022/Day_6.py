g = input()
ind=0

arr=[]
br = False
for i in g:
    arr.append(i)
    ind+=1
    br=False
    if len(arr)==14:
        for j in range(0,len(arr)-1):
            for k in range(j+1,len(arr)):
                if arr[j]==arr[k]:
                    br=True
                    break
                if br:
                    break
            if br:
                break
        if br:
            arr.pop(0)
        else:
            break
print(ind)