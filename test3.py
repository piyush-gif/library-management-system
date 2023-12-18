arr=[1,2,3,4,5]
sum=0
min=0
max=0
for i in arr:
    sum+=i

    if i > max:
        max=i

    elif i < min:
        min=i

    
print((sum-max),(sum-min))
       
