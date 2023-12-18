grades=[4, 73, 67, 67, 38, 33, 60, 57, 58, 99]
for i in range(len(grades)):
    #print(i) # 0-9
    for j in range(1,21):
        mul=j*5
        if grades[i] > 42 and mul > grades[i]:
        #print(i) # 73 67 67
            if  abs(mul - grades[i]) < 3:
               # print(mul)
                grades[i]=mul
print(grades)

                
