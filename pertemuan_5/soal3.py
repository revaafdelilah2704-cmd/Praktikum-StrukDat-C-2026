ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

hanya_coding = ukm_coding - ukm_robotik
ukm_coding.union(ukm_robotik)
cek_andi = "Andi" in ukm_robotik

print("Hanya coding:", hanya_coding)
print("ukm coding:", ukm_coding)
print("Apakah Andi di robotik?", cek_andi)