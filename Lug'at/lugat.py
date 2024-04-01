#otam={"ism":"qudrat","tyil":1981,"viloyat":"xorazm"}
#tyil=otam["tyil"]
#vil=otam["viloyat"]
#print(f"Otamning ismi {otam["ism"].upper()},{tyil}-yil,{vil.upper()}\
# viloyatida tug'ilgan.")




#taomlar = {
#    "ali": "osh",
#    "vali": "shashlik",
#    "hasan": "lag'mon",
##    "husan": "mastava",
 #   "olim": "somsa",
#}

#taom = taomlar["ali"]
#print(f"Alining sevimli taomi {taom}")

 

#izoh={'integer':'butun sonlar','float':'onlik sonlar','string':'matn','if':'IF bu shart bajaruvchi operator if(agar)','else':'aks holda'}
#print(izoh['integer'].upper())#



#kalit=input('kalit soz kiriting: ')
#print(izoh.get(kalit,'bunday soz mavjud emas'))


#kalit=input('kalit soz kiriting: ').lower()
#tarjima=izoh.get(kalit)

#if tarjima == None:
 #   print("bunday kalit soz yoq")

#else:
 #   print(f'{kalit.title()} sozi {tarjima} deb tarjima qilinadi')


#taomlar = {
#    "ali": "osh",
#   "vali": "shashlik",
#    "hasan": "lag'mon",
#    "husan": "mastava",
#    "olim": "somsa",
#}
#for k,q in taomlar.items():
#    print(f'{k.upper()} {q.title()}ni tanladi')
    
mahsulotlar={"uzum":1000,
             'apelsin':2000,
             'anor':3000
             }

#for mahsulot in mahsulotlar.keys():
 #   print(mahsulot)
    
 
    
bozorlik = ['anor','uzum','non','baliq']
for mahsulot in sorted(mahsulotlar):
     if mahsulot in bozorlik:
         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

for buyum in sorted(bozorlik):
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")
