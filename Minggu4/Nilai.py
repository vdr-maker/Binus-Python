nilai = {
    "A": 4.00,
    "A-": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.00,
    "C-": 1.75,
    "D": 1.50,
    "E": 1.20
}

total = 0
jumlah = 0

while True:
    kategori = input(
        "Masukkan Kategori Nilai (Tekan Enter untuk Berhenti): "
    ).upper()

    if kategori == "":
        break

    if kategori in nilai:
        total += nilai[kategori]
        jumlah += 1
        print(f"// {nilai[kategori]:.2f}")
    else:
        print("Kategori nilai tidak valid!")

if jumlah > 0:
    rata_rata = total / jumlah

    if rata_rata >= 4.00:
        predikat = "A"
    elif rata_rata >= 3.75:
        predikat = "A-"
    elif rata_rata >= 3.50:
        predikat = "B+"
    elif rata_rata >= 3.00:
        predikat = "B"
    elif rata_rata >= 2.75:
        predikat = "B-"
    elif rata_rata >= 2.50:
        predikat = "C+"
    elif rata_rata >= 2.00:
        predikat = "C"
    elif rata_rata >= 1.75:
        predikat = "C-"
    elif rata_rata >= 1.50:
        predikat = "D"
    else:
        predikat = "E"

    print(f"Nilai rata-rata adalah {rata_rata:.2f} dengan predikat {predikat}")
else:
    print("Tidak ada nilai yang dimasukkan.")