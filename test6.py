import random

arr = []
n=100
for i in range(n):
    arr.append(random.randint(0,n))

print(arr)
c=0
for j in range(len(arr)):
    c+=1
    for i in range(i+1,len(arr)):
        c+=1
        #print(i) # 0,1,2,3,4
        #print(arr[i])# 5,4,3,2,1  
        #print(c) #1,2,3,4,5
        if arr[i] > arr[j]: # 5 > 4,3,2,1
            #arr[c]=4
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            #print(swap) #4
print(arr)#[1,5,4,3,2]
print(c)
            # [5,4,3,2,1]
            # [4,5,3,2,1]
            # [3,5,4,2,1]
            # [2,5,4,3,1]
            # [1,5,4,3,2]

            # [1,4,5,3,2]
            # [1,3,5,4,2]
            # [1,2,5,4,3]

            # [1,2,4,5,3]
            # [1,2,3,5,4]

            # [1,2,3,4,5]