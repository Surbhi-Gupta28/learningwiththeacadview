#how to find the length of tuple
tupleA=(1,5,7,9)
print(len(tupleA))

#to find max and min element in tuple
print(max(tupleA))
print(min(tupleA))

#to find the product of elements in a tuple
tupleB=(1,2,3,4)
def product(tupleB):
 prod=1
 for x in tupleB:
  prod=prod*x
  return prod

print(product(tupleB))

#sets
x  = input().split()
s = set()
for i in x:                                                                
   s.add(i)

y = input().split()
t = set()
for i in y:
	t.add(i)

print(s-t) #difference of sets
subsetA = s <= t
superA = s >= t
print(subsetA)                                 
print(superA)
print(s.intersection(y)) #intersection of two sets

#creating a dictionary by taking input from user
dic = {}
for i in range(10):
	key = input()
	value = int(input())
	dic[key]=value
print(dic)
#to sort the values in dictionary
print(sorted(dic.values()))

#last ques
str = "missisipi"
dict = {}
for i in str:
	count = 0
	if i not in dict:
		for j in str:
			if i==j:
				count+=1
				dict[i]=count
print(dict)
	
	
#                                                                              completed
