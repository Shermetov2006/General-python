# file = open ("pi.txt")
# PI= file.read()
# print(PI)
# file.close()

# with open('pi.txt') as file:
#     pi = file.read()

# print(pi)

# filename="pi.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)

# filename="pi.txt"
# with open(filename) as file:
#     talabalar=file.readlines()
# print(talabalar)

#YANGI *.TXT FAYLGA YOZAMIZ

# faylnomi="new.txt"
# ism = "maqsad rahimov"
# tyil=2007
# with open(faylnomi,"w") as file:
#     file.write(ism)
#     file.write(str(tyil))


# faylnomi="new.txt"
# ism = "maqsad"
# tyil = 2007
# with open(faylnomi, "w") as file:
#     file.write(ism + "\n")
#     file.write((str(tyil) + "\n"))


# faylnomi= "new.txt"
# age=17
# with open(faylnomi, "a") as file:
#     file.write("fgyutghhhf\n")
#     file.write((str(age)))


import pickle as p 
talaba= {'ism':'anvar','familya':'narzullayev', 'tyil':2007, "kursi":2}
talaba2={'ism':'ogabek','familya':'narzullayev', 'tyil':2003, "kursi":1}

with open("info.pkl", "wb") as file:
    p.dump(talaba, file)
    p.dump(talaba2, file)
    
    
import pickle as p  
with open("info.pkl", "rb") as file:
   talaba=p.load(file)
   talaba2=p.load(file)
   
print(talaba)
print(talaba2)
    