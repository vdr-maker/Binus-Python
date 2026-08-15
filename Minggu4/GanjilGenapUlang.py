while True:
    angka = int(input("Masukkan angka: "))

    if angka % 2 == 0:
        print(f"Angka {angka} adalah bilangan genap")
    else:
        print(f"Angka {angka} adalah bilangan ganjil")

    ulang = input("Apakah Anda ingin mengulang? ").upper()

    if ulang == "N":
        print("\nProgram Berhenti")
        print("Terima kasih telah menggunakan program saya ^^")
        break