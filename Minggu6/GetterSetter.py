class Student:
    def __init__(self):
        self.__nama = None
        self.__skor = None

    def get_nama(self):
        if self.__nama is None:
            return "Tidak Ada"
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_skor(self):
        if self.__skor is None:
            return "Tidak Ada"
        return self.__skor

    def set_skor(self, skor):
        self.__skor = skor

    def hapus_data(self):
        self.__nama = None
        self.__skor = None


siswa = Student()

while True:
    print("\n===== Program OOP =====")
    print("1. Deklarasikan Objek")
    print("2. Tampilkan Objek")
    print("3. Ubah Nilai Objek")
    print("4. Hapus Objek")
    print("5. Keluar dari Program")

    pilihan = input("Masukkan Pilihan Anda (1/2/3/4/5): ")

    if pilihan == "1":
        nama = input("Masukkan Nama Anda: ")
        skor = int(input("Masukkan Skor Anda: "))

        siswa.set_nama(nama)
        siswa.set_skor(skor)

        print("Data Berhasil Ditambahkan")

    elif pilihan == "2":
        print("\nNama:", siswa.get_nama())
        print("Skor:", siswa.get_skor())

    elif pilihan == "3":
        ubah = input("Apa yang ingin Anda ubah (Nama/Skor): ")

        if ubah.lower() == "nama":
            nama_baru = input("Masukkan Nama Baru: ")
            siswa.set_nama(nama_baru)
            print("Data Nama Berhasil Diubah")

        elif ubah.lower() == "skor":
            skor_baru = int(input("Masukkan Skor Baru: "))
            siswa.set_skor(skor_baru)
            print("Data Skor Berhasil Diubah")

        else:
            print("Pilihan tidak tersedia")

    elif pilihan == "4":
        siswa.hapus_data()
        print("Data Berhasil Dihapus")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan program saya.")
        break

    else:
        print("Pilihan tidak tersedia. Silakan pilih 1-5.")