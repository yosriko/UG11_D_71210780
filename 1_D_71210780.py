#cek string

stng= input("Masukkan string :")

if stng.isdigit():
    x= int(stng)
    if x%2==0:
        print(int(x/2))
    else:
        print(int((x+5)/2))
elif "." in stng:
    y= float(stng)
    z= round(y)
    a= (z+5)/2
    print(int(a))

else:
    rstng= stng[::-1]
    print(rstng)
        
    
