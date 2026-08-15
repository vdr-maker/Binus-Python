while True:
    sisi_a = int(input("Masukkan Sisi A: "))
    sisi_b = int(input("Masukkan Sisi B: "))
    sisi_c = int(input("Masukkan Sisi C: "))

    if sisi_a == sisi_b == sisi_c:
        print("\nIni adalah Segitiga Sama Sisi")
    elif sisi_a == sisi_b or sisi_a == sisi_c or sisi_b == sisi_c:
        print("\nIni adalah Segitiga Sama Kaki")
    else:
        print("\nIni adalah Segitiga Sembarang")

    ulang = input("\nApakah Anda ingin mengulang? ").upper()

    if ulang == "N":
        print("\nProgram Berhenti")
        print("Terima kasih telah menggunakan program saya ^^")
        break