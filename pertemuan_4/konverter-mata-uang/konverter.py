# konverter.py
from kurs import kurs

def konversi(dari, ke, jumlah):
    if dari == "IDR":
        return jumlah / kurs[ke]
    elif ke == "IDR":
        return jumlah * kurs[dari]
    else:
        # konversi antar mata uang asing
        ke_idr = jumlah * kurs[dari]
        return ke_idr / kurs[ke]

        