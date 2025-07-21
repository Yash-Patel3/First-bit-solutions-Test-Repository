num=input("enter three digit number :")

if len(num)==3:
    a=int(num[0])
    b=int(num[1])
    c=int(num[2])

    if a==b*2 and a==c*0.5:
        print("you have done it")
    else:
        print("please try it again")
else:
    print("enter a valid number")        