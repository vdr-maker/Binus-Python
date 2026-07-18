import math

r = float(input("Masukkan Jari-jari (meter) : "))
t = float(input("Masukkan Tinggi    (meter) : "))

phi    = math.pi          
r_kuadrat = r ** 2        
volume    = phi * r_kuadrat * t

print(f"  Volume : {volume:,.6f} m³")
