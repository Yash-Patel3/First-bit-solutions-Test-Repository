
def factorial(fact,n):
    if n==1:
        return fact 
    
    
    return fact*n * factorial(fact,n-1)



n=int(input("enter a number : "))
fact=1
result=factorial(fact,n)
print(result)