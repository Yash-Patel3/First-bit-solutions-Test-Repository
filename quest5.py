# a man goes for shopping display the price of five product bill after adding 18% gst

product1=int(input("enter the price of product one"))
product2=int(input("enter the price of product two"))
product3=int(input("enter the price of product three"))
product4=int(input("enter the price of product four"))
product5=int(input("enter the price of product five"))

bill=product1+product2+product3+product4+product5
total_bill_with_gst=bill+(bill*0.18)

print("toatal bill is : ",total_bill_with_gst)