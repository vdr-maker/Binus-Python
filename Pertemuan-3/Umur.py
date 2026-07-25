umur = int(input("Masukkan umur: "))

if umur < 0:
    print("Umur tidak boleh negatif")
elif umur <= 1:
    print("Bayi")
elif umur <= 3:
    print("Balita")
elif umur <= 5:
    print("Pra-sekolah")
elif umur <= 12:
    print("Anak")
elif umur <= 17:
    print("Remaja")
elif umur <= 21:
    print("Dewasa Muda")
elif umur <= 30:
    print("Pra-dewasa")
elif umur <= 50:
    print("Dewasa")
elif umur <= 70:
    print("Pra-lansia")
else:
    print("Lansia")