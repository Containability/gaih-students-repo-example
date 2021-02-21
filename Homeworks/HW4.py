import random as rnd
class man():
    
    
    def play(self):
        words=["araba","elma","jaguar","şeftali","fil"]
        hak=10
        secret=words[rnd.randint(0,len(words)-1)]
    
        guesses=[]      #Bu liste tahtadaki boşlukları ve harfleri tutar. Yani oyun tahtasını
        for _ in range(len(secret)):
            guesses.append("_")             #Kelime boşluk şeklinde basılır kullanıcının kullandığı tahta oluşturulur
        print("Adam asmaca oyununa hoşgeldin! Hadi oynamaya başla ")
    
        hak=6               #Adam asmacada 6 yanlış yapma hakkı vardır.
        success=0           #Kaç kere bildiğini tutar
        succesful=[]            #Bildiklerini tutar
        indexes=[]               #Bilinenlerin indexlerinden sonraki index'e geçer(Daha iyi açıklaması aşağıda)
        indexes.append(0)           #İlk index 0 ile başlatılır (Çünkü aşağıdaki if(*****) için indexes[0] her koşulda 0 olmalı
        
        while hak>0 and success<(len(secret)):        #While başlar hak bitene veya kelime bilinene kadar devam eder.
            print(guesses)
            guess=str(input(f'Kalan hakkınız:{hak} Lütfen tahmin harfinizi yazınız'))    #input harf olarak alınır.
            if(guess in succesful):                                          #Eğer daha önce yazıldıysa while döngüsü başa döner
                print("Tekrar dene, bunu daha önce yazdın!")
                continue
            else:  
                if(guess in secret):        #Eğer tahmin edilen bilindiyse
                    for x in range(secret.count(guess)):    # Tahmin edilen harf kelimede kaç kere tekrarlıyorsa o kadar döngü olur, bu sayede aşağıdaki kod bulunan her konuma harf'i yerleştirir
                    
                        if(guess==secret[secret.index(guess,indexes[x],len(secret))]):  # ****** Burdaki koşulumuz tahminin (guess) gizli kelime (secret) ın içinde ise bulunması ve tekrar etme durumu için index metodu ile indexes[] listemi kullanarak her birinin konumunu ayrı ayrı bulmasını sağlamak
                            guesses.insert(secret.index(guess,indexes[x],len(secret)),guess)  #Burada bulmaya çalıştığımız kelimedeki harfin bulunduğu index'e koyar, indexes[] ise aynı yere değil her seferinde son bulunan indexten sonraki harfler içinde o harfin bulunmasını sağlar(Eğer bunu yapmazsam her seferinde ilk bulduğu harfe gider ve eğer bir kelimede 1 den fazla kere tekrar ediyorsa tekrar tekrar aynı yere harfi koyar.
                            del guesses[(secret.index(guess,secret.index(guess)+indexes[x],len(secret)))+1] # olan boşluk her seferinde bir sonraki indexe kayacağından o boşluk silinir
                            if (x==(secret.count(guess)-1)):print(f"Harika! {x+1} harf buldun")
                            success=success+1   
                            succesful.append(guess)
                            indexes.append(secret.index(guess,indexes[x],len(secret))+1)    #Burada da bulunan harfin index'inden sonraki index indexes[] a koyulur. Bu sayede for döngüsü dönerken bir hafıza oluşturulur ve her tekrarlayan harf durumunda son bulunandan sonraki harflerde arama yapılır. Örnek araba'da 0 indexestedir sonra indexes'a 1 eklenir: indexes[0,1], sonra for döngüsündeki iterasyon 1 dir indexes[1] de 1 vardır ve araba kelimesinde r ve sonrasındaki harflerdeki ilk a aranır.Aynısı bir iterasyon daha tekrarlanır indexes[0,1,3] olur ve harfler yerleşmiş olur
                            
                else:
                    print("Üzgünüm yanlış harf :(")
                    hak=hak-1
       
        if hak==0:      
            print(f'Kaybettin :( Kelimen : {"".join(secret[:])}')
        else:
            print(f'Tebrikler kazandın! Kelimen : {"".join(secret[:])} ') 
Man=man()
Man.play()
