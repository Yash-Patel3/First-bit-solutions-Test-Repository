n=int(input("enter the range of number "))

sum=0

fact=1
for i in range(1,n+1):

    numerator=i
    denominator=fact*i

    sum+=numerator/denominator
    fact=denominator
print(sum)    