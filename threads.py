#question no 
import threading
def mylogg():
   print("hlo")
   threading.Timer(5.0,mylogg).start()
mylogg()

#question no 2
import threading
def numb():
   for i in range(1,11):
    print(i)
    threading.Timer(1.0,numb)
numb()

#question no 3
from threading import Thread
def slp(i,B):
   time.sleep(B)
   print("thread %i." %(i))
   a = [0,6,8,9]
   B = 2
   for i in a:
      th  = Thread(target = slp , args = (i,B))
      th.start()
      B+=2
      print(i)

#question no 4
def factor(n):
   fact = 1
   for i in range(n,0,-1):
      fact = fact*i
   print(threading.currentThread().getName(),fact)

n = int(input("enter no : "))
t = threading.Thread(name = "factorial is ",target = factor,args=(n,))
t.start()
