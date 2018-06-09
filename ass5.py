#question no 1
i = int(input("enter the year"))
if i%4==0:
    print("The entered yr is a LEAP YEAR")
else:
    print("you have not entered a leap yr")

#question no 2
l = int(input("enter the value of length"))
breadth = int(input("enter the value of breadth")) 
if l == breadth:                                   
        print("the given figure is square")
else:
        print("the given figure is rectangle")

#question no 3
a = int(input("enter the age of first person"))
b = int(input("enter the age of second person"))
c = int(input("enter the age of third person"))
if a >= c and a >= b:
        print("a is elderest")
elif b >= c and b >= a:
        print("b is elderest")
else:
        print("c is elderest")

#question no 4
point = int(input("enter the points you have scored")) 
if point >= 181 and point <= 200: 
            print("chocolates")
elif point >= 1 and point <= 50:
            print("no prize")
elif point >= 51 and point <= 150:
            print("wooden dog")
elif point >= 151 and point <= 180:
            print("book")
else:
            print("sorry! no prize this time")

#question no 5
quantity = int(input("enter the quantity of items"))
cost = quantity * 100
if cost >= 1000:
    discount = (10 * cost)/100
    total_cost = cost - discount
    print("the total cost with discount is :{} " .format(total_cost)) 
else:
    print(cost)
    print("sorry no discount as total cost in less than 1000")
               
               
            
            
    
        
        
    
