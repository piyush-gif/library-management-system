n=25
#range(2)=[0,1]
#range(1)=[0]
#range(0)=[]
for i in range(n):
    c=''
    for k in range(n-i):
        c+=' '

    for j in range(i):
        c+= '..'
    
    c+='.'
    print(c)
n=n+1
for i in range(n):
    c=''
    for j in range(i):
        c+=' '
    for k in range(n-i-1):
        c+='..'
    c+='.'
    print(c)
