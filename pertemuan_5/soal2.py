data_aktivitas = [("Diki", 88),("Aqul", 45),("Abid", 92),("Rehan", 70)]
for nama, poin in data_aktivitas:
    if poin > 80:
        print(f"{nama} mendapatkan predikat Gold")
    elif 50 <= poin <= 80:
        print(f"{nama} mendapatkan sertifikat vilver")
    else:
        print(f'{nama} mendapatkan predikat Bronze')        