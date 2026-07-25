import math

a = float(input("Masukkan nilai A: "))
b = float(input("Masukkan nilai B: "))
c = float(input("Masukkan nilai C: "))

if a == 0:
    print("Ini bukan persamaan kuadrat")
else:
    d = b**2 - 4*a*c

    print(f"Persamaan: {a}x² + {b}x + {c} = 0")
    print("Diskriminan =", d)

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)

        print("Memiliki akar yang berbeda")
        print("x1 =", x1)
        print("x2 =", x2)

    elif d == 0:
        x = -b / (2*a)

        print("Memiliki akar ganda")
        print("x =", x)

    else:
        print("Memiliki akar imajiner")
        print("x1 = (-b + √(b² - 4ac)) / (2a)")
        print("x2 = (-b - √(b² - 4ac)) / (2a)")