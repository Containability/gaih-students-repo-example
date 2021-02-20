#Explain your work

#Question 1
def primeFirst(val):
    count=0
    flag=True
    
    if val<=500: #500den küçükse
        for a in range(2,val):
            if(val%a==0):#kendisinden küçük herhangi bir sayıya bölünüyorsa
            
                flag=False#false
        if flag==True:#Eğer bölünmediyse true bu da asal sayı demek
            if val==499: #Prime second ile ayrımı olması için son asal sayıda new line
                print(val,end="\n")
            else:
                print(val,end=" ")

def primeSecond(val):		
		#Aynısının 500den büyük sayılara yapılan hali
    count=0
    flag=True
   
    if val>500 and val<1000:
        for a in range(2,val):
            if(val%a==0):
            
                flag=False
        if flag==True:
            print(val,end=" ")
            
for x in range(1000): #FOR DÖNGÜSÜ
    primeFirst(x)
    primeSecond(x)
