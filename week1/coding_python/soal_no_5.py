import math

def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari**2 * tinggi

# Menghitung volume tabung
jari_jari = 3
tinggi = 5
print(f"Volume tabung dengan jari-jari {jari_jari} dan tinggi {tinggi} adalah: {volume_tabung(jari_jari, tinggi):.2f}")
