# NESTED IF

kelas = 5
score = 40

if kelas > 1:
    if score >= 85:
        print('Predikat A/Memuaskan')
    elif score >= 75:
        print('Predikat B/Bagus')
    else:
        print('Tidak Lulus')
else:
    if score >= 80:
        print('Predikat A/Bagus')
    else:
        print('Tidak Lulus')