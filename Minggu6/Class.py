class Student:
    def __init__(self, nama, umur, kelas, alamat):
        self.nama = nama
        self.umur = umur
        self.kelas = kelas
        self.alamat = alamat

    def tampilkan_biodata(self):
        print("\n=== BIODATA SISWA ===")
        print(f"Nama   : {self.nama}")
        print(f"Umur   : {self.umur} tahun")
        print(f"Kelas  : {self.kelas}")
        print(f"Alamat : {self.alamat}")


nama = input("Masukkan nama: ")
umur = input("Masukkan umur: ")
kelas = input("Masukkan kelas: ")
alamat = input("Masukkan alamat: ")

siswa = Student(nama, umur, kelas, alamat)

siswa.tampilkan_biodata()