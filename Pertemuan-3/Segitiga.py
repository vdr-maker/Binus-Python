a = float(input("Masukkan sisi A: "))
b = float(input("Masukkan sisi B: "))
c = float(input("Masukkan sisi C: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Bukan Segitiga")
else:
    sisi = sorted([a, b, c])
    x, y, z = sisi

    if x**2 + y**2 == z**2:
        print("Segitiga Siku-siku")
    elif a == b == c:
        print("Segitiga Sama Sisi")
    elif a == b or a == c or b == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")