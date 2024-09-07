def volume_kerucut(diameter, tinggi):
    jari_jari = diameter / 2
    return (1/3) * math.pi * jari_jari**2 * tinggi

# Menghitung volume kerucut
diameter = 5
tinggi = 4
print(f"Volume kerucut dengan diameter {diameter} dan tinggi {tinggi} adalah: {volume_kerucut(diameter, tinggi):.2f}")
