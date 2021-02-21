class yemek():
    
    def __init__(self):
        self.i=0
        self.tarif={}
    def karıştır(self):
        self.i+=1
        self.tarif={k: v for k, v in self.tarif.items() if v!="tuz"}
    def kaynat(self):
        if("su" in self.tarif.values()):
            self.i+=1
            self.tarif={k: v for k, v in self.tarif.items() if v!="su"}
            if("pirinç" in self.tarif.values()):
                self.tarif.update({1:"Pilav"})
                self.tarif={k: v for k, v in self.tarif.items() if v=="Pilav"}
        else:
            print("Su yok yemek yandı çöp oldu. ")
            self.tarif={"ÇÖP"}
        
    def tuzEkle(self):
        self.i+=1
        self.tarif.update({str(self.i):"tuz"})
    def salçaEkle(self):
        self.i+=1
        self.tarif.update({str(self.i):"salça"})
    def fasulyeEkle(self):
        self.i+=1
        self.tarif.update({str(self.i):"fasulye"})
    def soğanEkle(self):
        self.i+=1
        self.tarif.update({str(self.i):"soğan"})
    def yağEkle(self):
        self.i+=1
        self.tarif.update({str(self.i):"yağ"})
    def suEkle(self):
        self.i+=1
        self.tarif.update({str(self.i):"su"})
    def kızart(self):
        if("yağ" in self.tarif.values()):
            self.i+=1
            self.tarif={k: v for k, v in self.tarif.items() if v!="yağ"}
            if("tavuk" in self.tarif.values()):
                self.tarif.update({1:"Kızarmış Tavuk"})
                self.tarif={k: v for k, v in self.tarif.items() if v=="Kızarmış Tavuk"}
        else:
            print("Yemeğinde yağ yok yemek yandı çöp oldu")
            self.tarif={"ÇÖP"}
    def show(self):
        print(self.tarif)
            
    def tavukEkle(self):
        self.i+=1
        self.tarif.update({str(self.i):"tavuk"})
    def pirinçEkle(self):
        self.i+=1
        self.tarif.update({str(self.i):"pirinç"})
class fasulye(yemek):
    yemekadı="fasulye"
    
    def __init__(self):
        super().__init__()
        self.istenenyemek={"1":"soğan","4":"fasulye","5":"salça"}
    def tarifi(self):
        print ({"1":"soğan","2":"yağ","3":"kızart","4":"fasulye","5":"salça","6":"su","7":"tuz","8":"karıştır","9":"kaynat"})
        
    def hazır(self):
        self.i+=1
        if self.istenenyemek==self.tarif:
            self.tarif={"Fasulye"}
            print("Tebrikler yemeğin hazır")
        else:
            print("Tarife uyamadın hazırladığın yemek yanlış  ",end=" ")
        
class KızarmışTavuk(yemek):
    yemekadı="Kızarmış Tavuk"
    def __init__(self):
        super().__init__()
        self.istenenyemek={1:"Kızarmış Tavuk"}
    def tarifi(self):
        return {"1":"tavuk","2":"yağ","3":"kızart"} 
    def hazır(self):
        self.i+=1
        if self.istenenyemek==self.tarif:
            print("Tebrikler yemeğin hazır")
            self.tarif={self.yemekadı}
        else:
            print(f"Tarife uyamadın hazırladığın {self.yemekadı} yanlış  ",end=" ")
class Pilav(yemek):
    yemekadı="Pilav"
    def __init__(self):
        super().__init__()
        self.istenenyemek={1:"Pilav"} 
    def tarifi(self):
        return {"1":"pirinç","2":"su","3":"kaynat"} 
    def hazır(self):
        self.i+=1
        if self.istenenyemek==self.tarif:
            print("Tebrikler yemeğin hazır")
            self.tarif={self.yemekadı}
        else:
            print(f"Tarife uyamadın hazırladığın {self.yemekadı} yanlış  ",end=" ")
  # Örnek deneme için:
hadi=fasulye()
hadi.tarifi() #Olması gereken sıralı tarifi gösterir
hadi.soğanEkle()
hadi.yağEkle()
hadi.kızart()
hadi.fasulyeEkle()
hadi.salçaEkle()
hadi.suEkle()
hadi.tuzEkle()
hadi.karıştır()
hadi.kaynat()
hadi.hazır() #Hazır kontrol eder
hadi.show() #Hazırlanan yemeği gösterir
tavuğum=KızarmışTavuk()
tavuğum.tavukEkle()
tavuğum.kızart()
tavuğum.hazır()
tavuğum.show()
pilavım=Pilav()
pilavım.pirinçEkle()
pilavım.suEkle()
pilavım.kaynat()
pilavım.hazır()
pilavım.show()
