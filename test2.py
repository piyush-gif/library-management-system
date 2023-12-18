arr=[[1,2,3],
     [4,5,6],
     [9,8,10]]
ls=0
position=0
for i in range(len(arr)):
    position=len(arr)-i-1
    
    #print(position)
    rs=arr[i][position]
    print(arr[i])
    ls+=arr[i][i]
#print(ls)
    #i=arr[i]+1
    # print()
   # ls=ls+arr[i][0]
    #i = 0,1,2
    #arr[i] = [11, 22, 33]
    # for j in range(len(arr[i])):
    #     if i == j:
    #         #print(arr[i][j])
    #         ls += arr[i][j]
# print(ls)
# rs=0
# for i in range(len(arr)):
#     #i = 0,1,2
#     #arr[i] = [11,22,33]
#     for k in range(len(arr[i])):
#         #j=len(arr[i])-k-1
#         sum=i+k
#         if sum == len(arr)-1:
#             rs=rs+arr[i][k]
# print(rs)
# print(abs(ls-rs))
    

        
#print(arr[0][0],arr[1][1],arr[2][2])






# a=[11,22,33,44]
# for i in range(len(a)):
#    # print(a[i])
#     i=i+1
#     print(i)