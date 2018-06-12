#question no 1
c = 1
while(c <= 10):
    var = int(input("enter the no: "))
    print(var)
    c = c+1


#question no 3
li = []
for i in range(10):   #ab 2 min yahi ruk jaiyo or batadiyo merko run kar isko 
 n = int(input())
 li.append(n)
lis = []
for i in li:
        f = i*i
        lis.append(f)
print(lis)
        


#question no 4
li = [1,2,3,4,'a','b','c','d',1.0,2.36,5.66]
I=[]
F=[]
S=[]
for i in range(len(li)):
    if type(li[i])==int:
            I.append(li[i])
            
    if type(li[i])==str:
            S.append(li[i])
            
    if type(li[i])==float:
            F.append(li[i])
print(I)
print(F)
print(S)

#question no 5
li = list(int(x) for x in range(1,101))
even = []
odd = []
for i in range(len(li)):
            if li[i] % 2 == 0:
             even.append(li[i])

            if li[i] % 2 != 0:
             odd.append(li[i])
print (even)
print (odd)
 



#question no 6
i = '*'
for j in range(1,5):
    print(i*j) 
    
#question no 7
dict = {}
n = int(input("enter the no of elements"))
for i in range(n):
    a,b = map(int,input("enter key nd value").split())
    dict[a] = b
print(dict)

#question no 8
li= []
for i in range(1):
    t = int(input())
    li.append(t)
print(li)
y = int(input("enter the element to search"))
for i in li:
    if y==i:
        li.remove(y)
print(li)
print("{} is deleted from the list".format(y))
              
#question no 2
while(1):
    print("infinite loop going on")
