# Shohruh Mahmudov
# 2/2/2023
# 1-dars Hello World!

#print("hello")
#print(2**4)
#print(2/4)
#print('Assalomu alaykum')

# 2-dars Print() funksiyasi

#print('Salom hammaga')
#print("Bugun ajoyib kun")
#print('''Mening ismim Shohruh
#va men 20 yoshdaman''')
#print("Bugun Print funksiyasini o'rganamiz va \ntahlil qilamiz")     
#print("O\'zbekiston") 
#print('"Print" funksiyasining ayrim xususiyatlarini o\'rganib oldik') 

# 3-dars Arifmetik amallar

#print(2+5) #Qo'shish
#print(2*3) #Ko'paytirish
#print(56-32) #Ayirish
#print(2**4) #Darajaga ko'tarish
#print(6/5) #Bo'lish va kasrli son chiqarish
#print(6//5) #Bo'lish va butun qismini chiqarish
#print(7%3) #Qoldiq chiqarish
#print('To\'qqizning kvadrati',9**2,'ga teng')
#print('3x3=',3*3)

# 4-dars O'zgaruvchilar

#ism = 'Abdulloh'
#Ism = "Shohruh"
#yosh = '10'
#Yosh=20
#print(ism)
#print(Ism)
#print(yosh)
#print(Yosh)
#radius = 5
#pi = 3.14159
#aylana_yuzi = pi * radius**2
#print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

# 5-dars String

#ism = "Shohruh"
#familiya = 'Mahmudov'
#print(ism + familiya)
#print(f"{ism} {familiya}")
#print(ism + ' ' + familiya)
#ism_sharif = f"{ism} {familiya}"
#print(ism_sharif)
#print(f"Salom mening ismim {ism}, {ism_sharif}")

#print("Hello World!")
#print("Hello \tWorld!")
#print('Hello \nWorld!')

#ism = "Bobur"
#familya = "Olimov"
#ism_shariv = f"{ism} {familya}"
#print(ism_shariv.upper()) #Hamma hariflarni katta qiladi
#print(ism_shariv.lower()) #Hamma hariflarni kichik qiladi
#print(ism_shariv.title()) #Har bir so'zning bosh harfini kattalashtiradi
#print(ism_shariv.capitalize()) #Matndagi birinchi so'zning bosh harfini kattalashtiradi

#nom = "     olma    "
#print("Men "+nom.lstrip()+" yaxshi ko'raman") #Matnning chapdagi bo'shliqni o'chiradi 
#print("Men "+nom.rstrip()+" yaxshi ko'raman") #Matnning o'ngdagi bo'shliqni o'chiradi
#print("Men "+nom.strip()+" yaxshi ko'raman") #Marndagi chap va o'ng bo'shliqni o'chiradi
 
#matn = "       Salom hammaga odamlar        "
#print(matn.strip())

#Amaliyot

#ism = input("Ismingiz nima?\n")
#print("Assalomu alaykum "+ism.capitalize())

#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor" 
#viloyat="Samarqand"
#print(kocha+" ko'chasi, "+mahalla+" mahallasi, "+tuman+" tumani, "+viloyat+" viloyati")

#kocha = input("Qaysi ko'cha? ")
#mahalla = input("Qaysi mahalla? ")
#tuman = input("Qaysi tuman? ")
#viloyat = input("Qaysi viloyat? ")

#print("\n"+kocha.title()+" ko'chasi,\n"+mahalla.title()+" mahallasi,\n"+tuman.title()+" tumani,\n"+viloyat.title()+" viloyati")

# =============================================================================
# Shohruh Mahmudov
# 3/2/2023

# 6-dars Sonlar

#a=20
#b=-10
#print(a/b)

#a=10
#b=2.5
#print(a/b)
#c=a//b
#print(c)
#d=5.5
#e=5
#print(d/e)
#f=int(d//e)
#print(f)

#PI=3.14
#radius = 5
#print('Aylana yuzi ',PI*radius**2,' ga teng')
#print('Aylana yuzi '+str(PI*radius**2)+' ga teng')

#aholi = 7_594_234_532
#print("Yer yuzi aholisi",aholi,'ga teng')

#x,y,z=3,4,5
#print("Uchburchak uzunligi",x+y+z,'ga teng')

#ism = 'Anvar'
#yosh = 36
#print(type(ism))
#print(type(yosh))
#matn = ism + ' ' + str(yosh) + " da"
#print(matn)

#t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#yosh = 2023 - t_yil
#print('Siz',yosh,'dasiz')

#Amaliyot

#son = int(input('Son kiriting: '))
#print(son,'ning kvadrati',son**2,'ga teng')
#print(son,'ning kubi',son**3,'ga teng')

#son1 = int(input("Birinchi sonni kiriting: "))
#son2 = int(input("Ikkinchi sonni kiriting: "))
#print(son1,'+',son2,'=',son1+son2)
#print(son1,'-',son2,'=',son1-son2)
#print(son1,'*',son2,'=',son1*son2)
#print(son1,'/',son2,'=',son1/son2)

# 7-dars List

#mevalar = ['olma','shaftoli','uzum','olcha']
#sonlar = [1,2,3,4,5]
#print(mevalar)
#print(sonlar)
#son_soz = ['salom',4,'hayr',9]
#print(son_soz)
#bosh = []
#print(bosh)
#print('Birinchi meva:',mevalar[0])
#print('Meva nomi:',mevalar[-1].title())
#print(sonlar[0]+sonlar[1])
#print(sonlar[-1]*sonlar[-3])
#narhlar = [12000,15000,20000,22000]
#narhlar[0] = narhlar[0] + 5000
#print(narhlar)

#mevalar.append('tarvuz') #append('value') funksiyasida listni oxiriga yangi element qo'shiladi
#print(mevalar)
#sonlar.append(7)
#print(sonlar)

#mevalar.insert(0, "gilos") #insert(index,"value") funksiyasida listni istalgan joyiga qo'shiladi
#print(mevalar)
#sonlar.insert(-2, 4.2)
#print(sonlar)

#del mevalar[1] #del funksiyasida aniq bir elementni o'chirsa bo'ladi
#print(mevalar)
#del sonlar[-2]
#print(sonlar)

#mevalar.remove("uzum") #remove(value) funksiyasida element raqamini bilmagan holda nomi orqali o'chirish
#print(mevalar)
#sonlar.remove(3)
#print(sonlar)

#bozorlik = ['kartoshka','sabzi','yo\'g\'','olma']
#mahsulot = bozorlik.pop(1) #pop(index) funksiyasi aniq bir elementni ajratib oladi
#print("Men",mahsulot+'ni oldim','\n'+'Qolgan mahsulotlar:',bozorlik)

#Amaliyot

#ismlar = ['Umid','O\'tkir','Bekzod']
#print(ismlar[0]+', bugun choyxonaga boramizmi?')
#print(ismlar[1]+', bugun darslaring bormi?')
#print(ismlar[-1]+', endi qachon kelasan?')

#sonlar = [3,2,-2,-5,4.5,2.6]
#print(sonlar[0]+sonlar[-1])
#print(sonlar[1]-sonlar[2])
#sonlar[0]=sonlar[0]+2
#sonlar[-3]=sonlar[-3]*2
#print(sonlar[0]*sonlar[-3])

#t_shaxslar = ['Amir Temur','Zahriddin Bobur','Alisher Navoi']
#z_shaxslar = ['Stiv Jobs','Bill Gates','Ronaldo']
#print('Men tarixiy shaxslardan',t_shaxslar.pop(2),'bilan\nZamonaviy shaxslardan esa',z_shaxslar.pop(-2),'bilan suhbatlashgan bo\'lar edim')

#friends = []
#print(friends)
#friends.append('Azim')
#friends.append('Bekzod')
#friends.append('O\'tkir')
#friends.append('Humoyun')
#friends.append('Xondamir')
#print(friends)
#friends.remove('Xondamir')
#friends.remove('Humoyun')
#print(friends)
#friends.insert(0, 'Umid')
#friends.insert(2,'Anvar')
#friends.insert(-1,'Rasul')
#print(friends)

#mehmonlar = []
#f1 = friends.pop(0)
#f2 = friends.pop(-1)
#f3 = friends.pop(3)
#mehmonlar.append(f1)
#mehmonlar.append(f2)
#mehmonlar.append(f3)
#print(mehmonlar)
#f4 = friends.pop(0)
#f5 = friends.pop(0)
#mehmonlar.append(f4)
#print(mehmonlar)

# =============================================================================
#Shohruh Mahmudov
#4/2/2023

# 8-dars Ro'yxatlar bilan ishlash

#cars = ['bmw','lacetti','nexia','audi','bugatti','damas']
#cars.sort() #sort() funksiyasi listni tartiblaydi
#print(cars)
#sonlar = [23,123,32.5,32.3,11,5,-2,-52,0]
#sonlar.sort()
#print(sonlar)
#cars.sort(reverse = True)  #reverse teskari qiladi
#print(cars)
#sonlar.sort(reverse=True)
#print(sonlar)
#cars2 = ['Bmw', 'LaCeTti','12','audi','damaS','Nexia']
#cars2.sort()
#print(cars2)
#mehmonlar = ['Aziz','Azim','Bekzod','Abdulla']
#print('Tartiblangan ro\'yxat:',sorted(mehmonlar)) #sorted() listga tegmagan holda tartiblaydi
#print('Asil ro\'yxat:',mehmonlar)
#print(sorted(mehmonlar, reverse=True))
#print(sorted(sonlar,reverse=True))

#cars.reverse()
#print(cars)

#print("Ikki to'plamdagi elementlar soni:",len(cars),'va',len(sonlar)) #len() funksiyasi listning uzunligini aniqlaydi

#sonlar2 = list(range(0,12)) #range(a,b) a dan b gacha sonlarni yaratadi list() ularni ro'yxatga aylantiradi
#print(sonlar2) #range() dagi sonlar b-1 da to'xtaydi

#juft_sonlar = list(range(0,20,2)) #range(a,b,c) dagi c harfi sonlar orasidagi farqni ko'rsatadi
#toq_sonlar = list(range(1,20,2))
#print('Juft sonlar:',juft_sonlar)
#print('Toq sonlar:',toq_sonlar)

#sonlar3 = list(range(20)) #range(b) holatda list 0 dan boshlanadi
#print(sonlar3)

#arzon = min(sonlar) #min() listdagi minimal qiymatni topadi
#qimmat = max(sonlar) #max() listdagi maximal qiymatni topadi
#hammasi = sum(sonlar) #sum() listdagi elementlar yi'g'indisini topadi(faqat sonlar uchun ishlaydi)
#print('Minimal son:',arzon)
#print('Maximal son:',qimmat)
#print('Yi\'g\'indi:',hammasi)
#kichik = min(cars)
#print(kichik)
#katta=max(cars)
#print(katta)
#little = min(cars2)
#big = max(cars2)
#print(little,big)
#low = min(mehmonlar)
#high = max(mehmonlar)
#print(low,high)

#my_cars = cars[1:3] #[a:b] listning a dan b gacha qiymatlarini oladi
#print(my_cars)
#print(cars)
#my_cars2 = cars[2:5]
#print(cars)
#print(my_cars2)
#my_sonlar = sonlar[:5] #[,b] listda 0 dan b gacha qiymatlarni oladi
#print(sonlar)
#print(my_sonlar)
#my_sonlar2 = sonlar[2:] #[a:] listda a dan oxirigacha qiymatlarni oladi
#print(sonlar)
#print(my_sonlar2)
#my_sonlar3 = sonlar[:] #[:] listni to'liq oladi
#print(my_sonlar3)

#toys = ('bear','teddy','kitty','car','doll') #tuple list ustida amallar bajara olasiz lekin o'zgartirish 
#print(sorted(toys))                          #kirita olmaysiz const list bo'lgani uchun
#print(toys[0:3])

#toys = list(toys)  #list() funksiyasi yordamida tuple listni oddiy listga aylantirish mumkin
#toys.append('bobby')
#print(toys)
#toys = tuple(toys) #tuple() funksiyasi yordamida oddiy listni tuple listga aylantirish mumkin
#print(toys)

#Amaliyot

#davlatlar = ['Uzbekistan','Turkmanistan','Kazakistan','England','America']
#print(davlatlar)
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar,reverse=True))
#print(davlatlar)
#davlatlar.reverse()
#print(davlatlar)
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)

#sonlar = list(range(120,1200,2))
#print(sonlar)
#natija = sum(sonlar)
#print('120 dan 1200 gacha bo\'lgan sonlar yig\'indisi:',natija)
#print('Eng katta va eng kichik sonlar ayirmasi:',max(sonlar)-min(sonlar))
#print('Ro\'yxatdagi elementlar soni:',len(sonlar))
#print('Boshidagi 20 ta son:',sonlar[:20])
#print('O\'rtasidagi 20 ta son:',sonlar[100:120])
#print('Oxiridagi 20 ta son:',sonlar[520:])

#taomlar = ['osh','sho\'rva','dimlama','moshxo\'rda','mastava']
#nonushta = taomlar[:]
#print(taomlar)
#print(nonushta)
#nonushta.remove('osh')
#nonushta.remove('dimlama')
#nonushta.append('choy')
#nonushta.append('non')
#print(nonushta)
#nonushta = tuple(nonushta)
#print(nonushta)

# 9-dars For-loop operatori

#mehmonlar = ['Aziz','Bekzod','Anvar','Humoyun','Shohruh']
#for mehmon in mehmonlar:
#    print('Salom',mehmon)
    
#for mehmon in mehmonlar:
#    print(f"{mehmon},sizni to'yga chaqiramiz")

#sonlar = [2,5,14,-2,-5,0]
#for a in sonlar:
#    print(f'{a} ning kvadrati',a**2)

#sonlar = list(range(1,11))
#for a in sonlar:
#    print(f"{a} ning kubi:",a**3)
    
#sonlar = list(range(11))
#son_ildizi = []
#for a in sonlar:
#    son_ildizi.append(a**(1/2))
    
#print(sonlar)
#print(son_ildizi)

#dostlar=[]
#print("Eng yaqin 5 ta do'stingizni kiriting:")
#for a in range(5):  # 0 dan 4 gacha qiymatlar oladi
#    dostlar.append(input(f"{a+1} do'stingizning ismi: "))
#print(dostlar)

#cars = []
#print("Eng yoqtirgan 3 ta mashinangiz nomini yozing:")
#for car in range(3):
#    cars.append(input(f"{car+1}chi mashina: "))
#print("Sizga yoqadigan mashinalar ro'yxati:",cars)    

#kvadratlar = []
#print("5 ta son kiriting: ")
#for son in range(5):
#    a=int(input(f'{son+1}chi son: '))
#    kvadratlar.append(a**2)
#print(kvadratlar)

#Amaliyot

#ismlar = ['Ali','VaLi','sali','Azim','shohRuh']
#a=0
#for ism in ismlar:
#    print(f'{ism.title()}, qalaysan?')
#    a=a+1
#print("Kod",a,"marta takrorlandi")

#toq_sonlar = list(range(11,100,2))
#print(toq_sonlar)
#for son in toq_sonlar:
#    print(son**3)

#kinolar=[]
#print("Sizga yoqqan 5 ta kino nomini yozing")
#for kino in range(5):
#    kinolar.append(input(f"{kino+1}chi kino nomi: ").title())
    
#print("Sizga yoqqan kinolar:",kinolar)

# odamlar = input(f"necha kishi bilan suhbatlashdingiz? ")
# u_odamlar = []
# for odam in range(int(odamlar)):
#     u_odamlar.append(input(f"{odam+1}chi uchrashgan odamingizning ismi: ").title())
# print("Siz uchrashgan odamlar:",u_odamlar)

# =============================================================================
#Shohruh Mahmudov
#5/2/2023

# 9-dars If-Else operatori

# avtolar = ['bmw','kia','hyundai','mercedez','bugatti']
# for avto in avtolar:
#     if avto == 'bmw':     
#         print(avto.upper())
#     else:
#         print(avto.title())

# ism = input('Ismingiz nima? ')
# if ism.lower() != 'shohruh':
#     print(f'Uzr {ism.title()}, biz Shohruhni taklif etgan edik')
# else:
#     print('Xush kelibsiz,',ism.title())

# javob = int(input('12x6 nechiga teng?: '))
# if javob != 72:
#     print('Javob xato')

# yosh = int(input('Yoshingiz nechida?: '))
# if yosh <= 18:
#     print('Kirish mumkin emas')
# else:
#     print('Xush kelibsiz')

# login = input("Yangi login kiriting: ")
# if len(login) <= 5:
#     print('Login 5 ta harfdan ko\'p bo\'lishi kerak ')
    
# yosh = int(input('Tug\'ilgan yilingizni kiriting: '))
# if 2023-yosh <=18:
#     print(f'Siz {2023-yosh}da ekansiz\nSizga ruxsat etilmadi')
# else:
#     print('Xush kelibsiz')

# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2023-yil>65: print('Sizning COVIDga moyilligiz bor ekan')

# x,y=25,50
# print("x<y") if x<y else print("x>y")

# yil1 = int(input("Siz tug'ilgan yilingizni kiriting: "))
# yil2 = int(input("Do'stingiz tug'ilgan yilini kiritsin: "))
# print(f'Siz {yil2-yil1} yoshga katta ekansiz') if yil1<yil2 else print(f"Do'stingiz {yil1-yil2} yoshga katta ekan")

# Amaliyot

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# ism = input('Login kiriting: ')
# if ism.lower() == 'admin':
#     print("Xush kelibsiz,",ism.title(),'foydalanuvchilar ro\'yxatini ko\'rasizmi?')
# else:
#     print(f'Xush kelibsiz {ism.title()}')

# print('Ikkita son kiriting:')
# son1 = int(input('Birinchi son: '))
# son2 = int(input('Ikkinchi son: '))
# if son1 == son2:
#     print('Sonlar teng')
# else:
#     print('Sonlar teng emas')
    
# son = int(input('Son kiriting: '))
# if son <0:
#     print('Son manfiy')
# else:
#     print('Son musbat')

# son = int(input('Son kiriting: '))
# print(son**(1/2)) if son > 0 else print('Musbat son kiriting')
    
# 10-dars If-elif-else ketma-ketligi

# yosh = int(input("Yoshingiz nechida? "))  #if-elif-else da to'gri javob topilganda tekshiruv to'xtaydi
# if yosh <=4: 
#     print('Sizga kirish bepul')
# elif yosh <=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10ming so\'m')
    
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# else:
#     price = 10000
# print(f"Sizga kirish {price} so'm")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# elif yosh <= 20:
#     price = 8000
# else:
#     price = 10000
# print(f"Sizga kirish {price} so'm")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# elif yosh >= 20:
#     price = 8000

# print(f"Sizga kirish {price} so'm")

# kun = input('Bugun qanday kun? ')
# if kun.lower() == 'shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Ish kuni')

# kun = input('Bugun qanday kun? ')
# harorat = int(input('Havo harorati qanday? '))
# if (kun.lower() == 'shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print('Bugun dam olish kuni va cho\'milishga boramiz')
# elif (kun.lower() == 'shanba' or kun.lower()=='yakshanba') and harorat<=30:
#     print('Bugun uyda dam olamiz')
# else:
#     print('Ish kuni')

# narx = 15000 #mijoz 15000 so'mga taom oldi
# choy = True #choy oldi
# salat = False #salat olmadi
# if choy and salat: # choy va salat olsa 10ming
#     narx = narx + 10000
# elif choy or salat: # choy yoki salat olsa 5ming
#     narx = narx + 5000
# print(f'Jami {narx} so\'m') # Umumiy narx

# narx = 15000
# choy = True #olingan
# salat = False #olinmagan
# non = True #olingan 
# kampot = True #olingan
# assorti = False #olinmagan
# if choy:     # Faqat if operatori ishlatilgan bo'lsa shart har birini tekshiradi
#     print('Mijoz choy oldi')
#     narx = narx + 5000
# if salat:
#     print('Mijoz salat oldi')
#     narx = narx + 10000
# if non:
#     print('Mijoz non oldi')
#     narx = narx + 2000
# if kampot:
#     print('Mijoz kampot oldi')
#     narx = narx + 6000
# if assorti:
#     print('Mijoz assorti oldi')
#     narx = narx + 15000
# print(f'Jami {narx} so\'m')

# menu = ['somsa','honim','osh','sho\'rva']
# 'manti' in menu  #menu da manti bormi?

# menu = ['somsa','honim','osh','sho\'rva']
# buyurtma = input('Nima ovqat yeysiz? ')
# if buyurtma.lower() in menu:
#     print('Buyurtma qabul qilindi')
# else:
#     print(f'{buyurtma} menuda mavjud emas')

# menu = ['somsa','honim','osh','sho\'rva']
# buyurtma = input('Nima ovqat yeysiz? ')
# if buyurtma.lower() not in menu:
#     print(f'{buyurtma} menuda mavjud emas')
# else:
#     print('Buyurtma qabul qilindi')

# menu = ['somsa','honim','osh','sho\'rva','mastava','shashlik']
# buyurtma =['somsa','kola','shashlik','choy']
# for taom in buyurtma:
#     if taom in menu:
#         print(f'{taom} menuda mavjud')
#     else:
#         print(f'{taom} menuda mavjud emas')

# menu = ['somsa','honim','osh','sho\'rva','mastava','shashlik']
# buyurtma =['somsa','kola','shashlik','choy']
# if buyurtma:    # bu holatda buyurtma listi bo'sh yoki bo'shmasligi tekshrilmoqda
#     for taom in buyurtma:
#         if taom in menu:
#             print(f'{taom} menuda mavjud')
#         else:
#             print(f'{taom} menuda mavjud emas')
# else:     # agar buyurtma = [] bo'lganda bu holat ishlaydi
#     print('Savatchangiz bo\'sh')

# Restorant dasturi

# menu=[]
# buyurtma=[]
# buyurtma2 = []
# print('Menuga 5 ta ovqatlar ro\'yxatini kiriting: ')
# for taom in range(5):
#     menu.append(input(f'{taom+1}chi taom nomi: '))
# print('Menudagi taomlar:',menu)
# print('Endi 3 xil buyurtma bering: ')
# for bill in range(3):
#     buyurtma.append(input(f'{bill+1}chi buyurtma nomi: '))
# print('Buyurtmadagi taomlar:',buyurtma)
# for food in buyurtma:
#     if food in menu:
#         print(f'{food} menuda bor')
#         buyurtma2.append(food)
#     else:
#          print(f'{food} menuda mavjud emas')
# if buyurtma2:
#     print('Buyurtmangiz qabul qilindi va siz',buyurtma2,'ni tanladingiz')
# else:
#     print('Siz bergan buyurtmadagi ovqatlar menuda yo\'q\nIltimos boshqa buyurtma bering')

# Amaliyot

# son = int(input("Juft son kiriting: "))
# if son%2 == 0:
#     print('Rahmat')
# else:
#     print('Bu juft son emas boshqa son kiriting')

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<4 or yosh>60:
#     print('Bepul')
# elif yosh<18:
#     print('Chipta narxi 10000 so\'m')
# else:
#     print('Chipta narxi 20000 so\'m')

# son1 = int(input('Birinchi sonni kiriting: '))
# son2 = int(input('Ikkinchi sonni kiriting: '))
# if son1<son2:
#     print(f'{son1}<{son2}')
# elif son1>son2:
#     print(f'{son1}>{son2}')
# else:
#     print(f'{son1}={son2}')

# mahsulotlar = ['olma','nok','anor','kartoshka','piyoz','sabzi','non','shkolad','picheniya','kola']
# savat=[]
# print('5 ta olmoqchi bo\'lgan narsalaringizni ayting: ')
# for food in range(5):
#     savat.append(input(f'{food+1}chi narsa: '))
# for taom in savat:
#     if taom in mahsulotlar:
#         print(f'Do\'konimizda {taom} bor')
#     else:
#         print(f'Do\'konimizda {taom} yo\'q')

# mahsulotlar = ['olma','nok','anor','kartoshka','piyoz','sabzi','non','shkolad','picheniya','kola']
# savat=[]
# bor_mahsulotlar=[]
# mavjud_emas=[]
# print('5 ta olmoqchi bo\'lgan narsalaringizni ayting: ')
# for food in range(5):
#     savat.append(input(f'{food+1}chi narsa: '))
# for taom in savat:
#     if taom in mahsulotlar:
#         bor_mahsulotlar.append(taom)
#     else:
#         mavjud_emas.append(taom)
# if mavjud_emas==[]:
#     print('Siz so\'ragan mahsulotlar hammasi bor')
# else:
#     print(f'{mavjud_emas} shu mahsulotlar do\'konimizda yo\'q')

# foydalanuvchilar = ['Anvar','Azim','Bekzod','Shohruh','Humoyun']
# login = input("Yangi login kiriting: ").title()
# if login not in foydalanuvchilar:
#     print("Xush kelibsiz!")
# else:
#     print("Login band, yangi login kiriting")

son = int(input("Son kiriting:"))
for a in range(2,11):
    if son%a==0:
        print(f'{son} soni {a}ga qoldiqsiz bo\'linadi')









