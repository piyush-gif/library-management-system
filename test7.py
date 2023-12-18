import random
arr=[]
n=100
c=0
for k in range(n):
    arr.append(random.randint(1,n))

for j in range(1,len(arr)):
    c+=1
    for i in range(len(arr)-1):
        if arr[i] > arr[j]:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            c+=1
#print(arr)
print(arr)
print(c)