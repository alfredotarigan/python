x = [10, 20, 30, 40, 50, 60]
y = [10, 40, 60, 80, 100]

koin1 = ['Depan', 'Belakang', 'Belakang', 'Depan']


def hitungRata(x):
    Start = True
    jumlah = 0
    rata = 0
    while Start:
        print("=== Program menghitung rata rata Python v0.1 ===")
        for i in x:
            jumlah = jumlah + i
            rata = jumlah / len(x)
        print("Nilai rata rata nya adalah ", rata)
        Start = False
        print("Program berhenti, silahkan masukkan kembali nilai yang ingin dihitung.")


hitungRata(x)
