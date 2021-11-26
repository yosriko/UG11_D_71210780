#generatesoal

tipe= input("Masukkan tipe yang ingin and coba : ")
import random
import string
punct= ("==","<",">")
x1= random.randrange(1,20)
x2= random.randrange(1,20)
x3= random.randrange(1,20)
x4= random.randrange(1,20)
z= random.choice(punct)

if "pengurangan" in tipe:
    print("(benar/salah) jika ", x1,"-",x2,z,x3,"-",x4)
    answ= input("Masukkan Jawaban Anda : ")
    if "benar" in answ:
        f1= x1-x2
        f2= x3-x4
        if "==" in z:
            if f1==f2:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
        elif ">" in z:
            if f1>f2:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
        elif "<" in z:
            if f1<f2:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
    elif "salah" in answ:
        f1= x1-x2
        f2= x3-x4
        if "==" in z:
            if f1==f2:
                print("Jawaban Anda Masih Salah!")
            else:
                print("Jawaban Anda Benar !")
        elif ">" in z:
            if f1>f2:
                print("Jawaban Anda Masih Salah!")
            else:
                print("Jawaban Anda Benar !")
        elif "<" in z:
            if f1<f2:
                print("Jawaban Anda Masih Salah!")
            else:
                print("Jawaban Anda Benar !")
    else:
        print("Pilihannya cuma benar/salah")
elif "penjumlahan" in tipe:
    print("(benar/salah) jika ", x1,"+",x2,z,x3,"+",x4)
    answ= input("Masukkan Jawaban Anda : ")
    if "benar" in answ:
        f1= x1+x2
        f2= x3+x4
        if "==" in z:
            if f1==f2:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
        elif ">" in z:
            if f1>f2:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
        elif "<" in z:
            if f1<f2:
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
    elif "salah" in answ:
        f1= x1+x2
        f2= x3+x4
        if "==" in z:
            if f1==f2:
                print("Jawaban Anda Masih Salah!")
            else:
                print("Jawaban Anda Benar !")
        elif ">" in z:
            if f1>f2:
                print("Jawaban Anda Masih Salah!")
            else:
                print("Jawaban Anda Benar !")
        elif "<" in z:
            if f1<f2:
                print("Jawaban Anda Masih Salah!")
            else:
                print("Jawaban Anda Benar !")
    else:
        print("Pilihannya cuma benar/salah")
else:
    print("Maap tapi disoal disuruh cuma pengurangan dan penjumlahan")
    
                
