grades = [85, 92, 78, 65, 88, 90, 72]

A = B = C = below_70 = 0

for g in grades:
    if g >= 90:
        A += 1
    elif g >= 80:
        B += 1
    elif g >= 70:
        C += 1
    else:
        below_70 += 1

print("A:", A)
print("B:", B)
print("C:", C)
print("Below 70:", below_70)
