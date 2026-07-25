print("=== Konversi Suhu ===")
print("1. Celsius ke Fahrenheit")
print("2. Celsius ke Kelvin")
print("3. Fahrenheit ke Celsius")
print("4. Fahrenheit ke Kelvin")
print("5. Kelvin ke Celsius")
print("6. Kelvin ke Fahrenheit")

pilihan = int(input("Pilih menu (1-6): "))
suhu = float(input("Masukkan suhu: "))

if pilihan == 1:
    hasil = (suhu * 9/5) + 32
    print("Hasil:", hasil, "°F")

elif pilihan == 2:
    hasil = suhu + 273.15
    print("Hasil:", hasil, "K")

elif pilihan == 3:
    hasil = (suhu - 32) * 5/9
    print("Hasil:", hasil, "°C")

elif pilihan == 4:
    hasil = (suhu - 32) * 5/9 + 273.15
    print("Hasil:", hasil, "K")

elif pilihan == 5:
    hasil = suhu - 273.15
    print("Hasil:", hasil, "°C")

elif pilihan == 6:
    hasil = (suhu - 273.15) * 9/5 + 32
    print("Hasil:", hasil, "°F")

else:
    print("Pilihan tidak valid")