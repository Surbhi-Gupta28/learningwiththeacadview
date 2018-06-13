#question no 1
def area(r):
    areaa = (3.14 * r * r)
    print(areaa)
    

rad = int(input("enter the radius of circle: "))
area(rad)




#question no 2
def perfect(n):
  sum = 0
  for i in range(1,n):
    if n%i == 0:
      sum = sum + i
  if sum == n:
    return True
  else:
    return False
for i in range(1,1001):
  if perfect(i):
    print (i)

    
#question no 3
def table(n,i):   
  print (n*i)       
  i=i+1
  if i<=10:
    table(n,i)    
table(12,1)


#question no 4
def power(a,b):
    if b == 1:
     return a
    else:
       return a * power(a,b-1)

c = int(input("enter the base no: "))
d = int(input("enter the exponent no: "))      
print (power(c,d))


#question no 5
def fact(n):
    if n>= 1:
        return n * fact(n-1)
    else:
        return 1

num = int(input("enter the number: "))
print(fact(num))

        
