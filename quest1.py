#write a programme to take user input and check the year is leap year or not

year=int(input("enter the year"))
if (1000<=year<=9999):
    """ if(year%4==0 and year%100!=0) or year%400==0:
        print("the year is leap year")
    else:
        print("year is not a leap year")"""
    
    if (year%4==0):
        if(year%100!=0):
            print("it is a leap year")
    else:
        print("It is not a leap year")    
    if (year%400==0):
        print("its a leap year ")
    else:
        print("its not a leap year")
       
else:
    print("please enter a valid year")        
    