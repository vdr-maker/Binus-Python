import math

r = float(input("Masukkan Jari-jari (meter) : "))

phi    = math.pi          
r_kubik = r ** 3          
volume  = (4 / 3) * phi * r_kubik

print(f"  Volume : {volume:,.6f} m³")