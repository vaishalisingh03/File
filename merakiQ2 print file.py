xyz=open("people3.txt","w")
xyz.write("abhishek-gurgaon\nranveer-delhi")
xyz.close()
a=["abv","opy"]
i=0
list=[]
while i<len(a):
    j=1
    sum=""
    while j<len(a[i])+1:
        sum+=a[i][-j]
        j+=1
    list.append(sum)
    i+=1
print(list)


