def kpk(a, b):
    temp_a = a
    temp_b = b
    while temp_a != temp_b:
        if temp_a < temp_b:
            temp_a += a
        else:
            temp_b += b
    return temp_a

# Menghitung KPK dari 3 dan 4
a = 3
b = 4
print(f"KPK dari {a} dan {b} adalah: {kpk(a, b)}")
