#Explain your work
#I am taking random variables from random library. And then i will check them if they are prime. 
#If they are prime i will append them to my 3x3 2-D array.If not they will pop

#Question 1
import random
import time
random.seed()
randoms=[]
count=0
i=0
#This while keeps going until it finds 9 random prime numbers.

while i<9:
    flag=False #This flag is false every iteration
    randoms.append(random.randint(0,100))
    for a in range(2,randoms[i]):
        if((randoms[i]%a)==0):
            count=count+1
            flag=True #Becomes true if this number can be divided to some number below it
            
            
        
        
    i=i+1
    if(flag):
        i=i-1
       # print(count,randoms[i],a,"Not Found") #For checking the iteration.
        randoms.pop() #If flag is true then the last element is not a prime number so this code removes it.
cntr=1
for x in randoms:
    print(x,end=" ")#elements
    if(cntr%3==0):
        print("\n")#In every 3 iteration this will print out the elements to the next line
    cntr=cntr+1
    
