#Q1:-
n=int(input("enter the number elements of the list"))
list=[]
for i in range(n):
    f=input()
    list.append(f)
print(list)


#Q2:-
list2=['google','apple','facebook','microsoft','tesla']
list.extend(list2)
print(list)

# another way to do this is using for loop
#for i in range(len(list2)):
#   f=list2[i]
#   list.append(f)

#Q3:-
#suppose we want to count the google in in the above list there are two methods
#first
d=list.count("google")
print(d)

#by using for loop
count=0
for i in list:
    if i=="google":
        count+=1
print(count)

#Q4:-
list1=[4,7,2,9,0]
list1.sort()
print(list1)

#Q5:-
m1=[1,2,3,4,5]
m2=[6,7,8,9,10]


arr=[]
i,j=0,0
n1=len(m1)
n2=len(m2)
while i < n1 and j < n2 :
    if m1[i] <= m2[j]:
        arr.append(m1[i])
        i += 1
    else:
        arr.append(m2[j])
        j += 1
while i < n1:
    arr.append(m1[i])
    i += 1
while j < n2:
    arr.append(m2[j])
    j += 1
print(arr)

#Q6:-iplementing satck and queues using list

stack=[1,2,3]
#push command to elments to the list "last in first out"
#we can use simple append
#pushing 4 in stack it will add at the end of the stack
stack.append(4)
print(stack)
# to delete we can use pop
stack.pop(0)
print(stack)

#Queues
que=[1,2,3,4,5,6]
# we can use insert function to add to the list
que.insert(0,9)
print(que)
#to delete
que.pop(0)
print(que)

#Q7:-
l=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even,odd)
#############################  complete    ####################################################################
























































