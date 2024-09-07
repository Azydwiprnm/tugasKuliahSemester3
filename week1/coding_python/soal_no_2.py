def tukar_buah():
    piring1 = "Manggis"
    piring2 = "Pisang"
    piring3 = ""

    # Proses pertukaran
    piring3 = piring1   # Manggis dipindah ke Piring 3
    piring1 = piring2   # Pisang dipindah ke Piring 1
    piring2 = piring3   # Manggis dipindah ke Piring 2

    print(f"Piring 1 berisi: {piring1}")
    print(f"Piring 2 berisi: {piring2}")

# Menukar buah pada dua piring
tukar_buah()
