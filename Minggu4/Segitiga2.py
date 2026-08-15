max_value = int(input("Input Max Value: "))

# Bagian turun
for i in range(max_value, 0, -1):
    print(str(i) * i)

# Bagian naik
for i in range(2, max_value + 1):
    print(str(i) * i)