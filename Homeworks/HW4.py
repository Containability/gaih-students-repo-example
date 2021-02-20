import random as rnd
class man():
    
    
    def play(self):
        words=["araba","elma","jaguar","şeftali","fil"]
        hak=10
        secret=words[rnd.randint(0,len(words)-1)]
    
        guesses=[]
        for _ in range(len(secret)):
            guesses.append("_")
        print(guesses[:])
    
        hak=10
        success=0
        succesful=[]
        indexes=[]
        indexes.append(0)
        
        while hak>0 and success<(len(secret)):
            counter=0
    
            print(guesses)
            guess=str(input(f'Kalan hakkınız:{hak} Lütfen tahmin harfinizi yazınız'))
            if(guess in succesful):
                print("Tekrar dene, bunu daha önce yazdın!")
                continue
            else:
                if(guess in secret):
                    for x in range(secret.count(guess)):
                    
                        if guess in secret and guess==secret[secret.index(guess,indexes[x],len(secret))]:
                            guesses.insert(secret.index(guess,indexes[x],len(secret)),guess)
                            del guesses[(secret.index(guess,secret.index(guess)+indexes[x],len(secret)))+1]
                            print("Harika! bir harf buldun")
                            success=success+1
                            succesful.append(guess)
                            indexes.append(secret.index(guess,indexes[x],len(secret))+1)
                            if secret.index(guess)==0 and counter==0:
                                indexes.pop()
                                indexes.append(1)
                                counter=counter+1
                else:
                    print("Üzgünüm yanlış harf :(")
                    hak=hak-1
                   
                     
                         
                            
                       
            
            
        if hak==0:      
            print(f'Kaybettin :( Kelimen : {"".join(secret[:])}')
        else:
            print(f'Tebrikler kazandın! Kelimen : {"".join(secret[:])} ') 
Man=man()
Man.play()
