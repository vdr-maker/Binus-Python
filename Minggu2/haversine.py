import math

RADIUS_BUMI = 6371.0

print("\n  [ TITIK A ]")
lon_a = float(input("  Longitude Titik A (°E) : "))
lat_a = float(input("  Latitude  Titik A (°S) : "))

print("\n  [ TITIK B ]")
lon_b = float(input("  Longitude Titik B (°E) : "))
lat_b = float(input("  Latitude  Titik B (°S) : "))

lat1  = math.radians(lat_a)
lat2  = math.radians(lat_b)
lon1  = math.radians(lon_a)
lon2  = math.radians(lon_b)

delta_lat = lat2 - lat1
delta_lon = lon2 - lon1

sin2_dlat = math.sin(delta_lat / 2) ** 2
sin2_dlon = math.sin(delta_lon / 2) ** 2
cos_lat1  = math.cos(lat1)
cos_lat2  = math.cos(lat2)

a = sin2_dlat + (cos_lat1 * cos_lat2 * sin2_dlon)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
d = RADIUS_BUMI * c

print(f"  Titik A : Lat {lat_a}°, Lon {lon_a}°")
print(f"  Titik B : Lat {lat_b}°, Lon {lon_b}°")
print(f"  a       : {a:.8f}")
print(f"  c       : {c:.8f} rad")
print("-" * 44)
print(f"  Jarak   : {d:,.4f} km")
print(f"          : {d * 1000:,.2f} meter")
