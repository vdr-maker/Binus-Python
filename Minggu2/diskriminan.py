import math

a = float(input("Masukkan Nilai A : "))
b = float(input("Masukkan Nilai B : "))
c = float(input("Masukkan Nilai C : "))

b_kuadrat  = b ** 2          
empat_ac   = 4 * a * c       
diskriminan = b_kuadrat - empat_ac

print(f"  Nilai D: {diskriminan}")