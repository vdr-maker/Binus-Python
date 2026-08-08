def identitas():
    print("Nama  : Vito")
    print("Asal   : Bintaro")
    print("-" * 40)


def penjumlahan(a=0, b=0):
    return a + b

def pengurangan(a=0, b=0):
    return a - b

def pembagian(a=0, b=1):
    return a / b

def perkalian(a=0, b=0):
    return a * b

def modulus(a=0, b=1):
    return a % b


identitas()

while True:
    menu = input("Masukkan Menu (+|-|/|*|%|stop): ")

    if menu.lower() == "stop":
        print("Program berhenti. Terima kasih telah menggunakan program saya.")
        break

    if menu not in ["+", "-", "/", "*", "%"]:
        print("Menu tidak valid. Silakan pilih +, -, /, *, %, atau stop.\n")
        continue

    nilai1 = float(input("Masukkan Nilai 1: "))
    nilai2 = float(input("Masukkan Nilai 2: "))

    if menu == "+":
        hasil = penjumlahan(nilai1, nilai2)
        print(f"Hasil dari penambahan {nilai1:g} + {nilai2:g} adalah {hasil:g}")

    elif menu == "-":
        hasil = pengurangan(nilai1, nilai2)
        print(f"Hasil dari pengurangan {nilai1:g} - {nilai2:g} adalah {hasil:g}")

    elif menu == "*":
        hasil = perkalian(nilai1, nilai2)
        print(f"Hasil dari perkalian {nilai1:g} * {nilai2:g} adalah {hasil:g}")

    elif menu == "/":
        if nilai2 == 0:
            print("Error: Nilai 2 tidak boleh 0 untuk pembagian.")
        else:
            hasil = pembagian(nilai1, nilai2)
            print(f"Hasil dari pembagian {nilai1:g} / {nilai2:g} adalah {hasil:g}")

    elif menu == "%":
        if nilai2 == 0:
            print("Error: Nilai 2 tidak boleh 0 untuk modulus.")
        else:
            hasil = modulus(nilai1, nilai2)
            print(f"Hasil dari modulus {nilai1:g} % {nilai2:g} adalah {hasil:g}")

    print()