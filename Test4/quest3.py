
def factorial(fact,n):
    if n==0 or n==1:
        return 1
    
    else:
        return fact*n * factorial(fact,n-1)



start=int(input("enter a start number of range : "))
n=int(input("enter a number end : "))
fact=1

for num in range(start,n+1):
   result=factorial(fact,num)

   print(f"{num}={result}")
