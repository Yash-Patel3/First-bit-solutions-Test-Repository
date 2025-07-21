num=int(input("enter the number"))

for i in range(2,num+1):
    count=0
    for j in range(2,i):
        if i%j==0 :
         count+=1
         break
    if count==0:
       print(i)
         