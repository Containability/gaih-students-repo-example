#Explain your work
#I am taking random variables from random library. And then i will check them if they are prime. 
#If they are prime i will append them to my 3x3 2-D array.If not they will pop

#Question 1
import random
import time
random.seed()
primes=[]
randoms=[]
count=0
i=0

while i<9:
    flag=False
    randoms.append(random.randint(0,1000))
    for a in range(2,randoms[i]):
        if((randoms[i]%a)==0):
            count=count+1
            flag=True
            
        
        
    i=i+1
    if(flag):
        i=i-1
        print(count,randoms[i],a,"Not Found")
        randoms.pop()
for x in randoms:
    print(x,end=" ")
    
