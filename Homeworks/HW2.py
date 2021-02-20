#Explain your work

student_names=[]
grades=[]
isim=["isim","soyisim"]
def get_key(val,dicto):
    for key, value in dicto.items():
         if val == value:
             return key
 
    print ("key doesn't exist")
for a in range(5):
    student_names.append(list(str(input(f'Lütfen {a+1}. {y} giriniz: ')) for y in isim)) #Öğrenci isim ve soyisimleri girilir
    
students={x[0]: list(int(input(f'Lütfen {x[0]} notlarını giriniz: ')) for _ in range(3)) for x in student_names} #Notları girilir girilirken isimlerle aynı dict e koyulur

cntr=0
for k,val in students.items():
    grades.append(round((val[0]+val[1]+val[2])/3)) #Ortalamalar hesaplanır ve bir listeye konur
    students[k]=grades[cntr]#Listeden students a ortalamaları şeklinde tekrar notları değişir
    cntr+=1
sorted_students={get_key(v,students):v for v in sorted(grades)} #Sorted ile düşükten yükseğe ortalamalara göre öğrenciler sıralanır
best=reversed(sorted_students.items()) #Ters çevrilir
print(f'Congratulations {get_key(sorted(grades)[-1],sorted_students)} ') #Print edilir
