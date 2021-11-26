#String Insert

ka= input("Masukkan sebuah kata/kalimat : ")
sip= input("Masukkan karakter yang ingin disisipkan : ")
kap= ka.upper()
#sisipHuruf
print((" "+sip+" ").join(kap))
print(ka.replace(" "," "+sip+" "))

