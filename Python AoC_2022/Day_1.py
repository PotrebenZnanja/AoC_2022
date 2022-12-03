elfi = [];

while(True):
    elf=[]
    g=input()
    while(g!="" and g!="-1"):
        elf.append(g)
        g=input()
    if g=="-1":
        break
    elfi.append(elf)

max_sum =0
sum_table=[]
for i in elfi:
    sum = 0

    for j in i:
        sum+=int(j)
    sum_table.append(sum)
    sum_table.sort()
    if max_sum<sum:
        max_sum=sum
print(sum_table[-3:])

print(sum_table[-1]+sum_table[-2]+sum_table[-3])

print(max_sum)
print(elfi)