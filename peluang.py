def menghitungPeluang():
    Start = True
    while Start:
        awal = 0
        user_input = input(
            "Selamat datang, pilih peluang yang ingin dihitung (koin / dadu ) : ")
        if user_input == 'koin':
            print("=== Program menghitung peluang koin v0.1 ===")
            user_input2 = input("Menghitung peluang ( gambar / angka ) ? : ")
            if user_input2 == 'gambar':
                sampel = int(input("Berapa banyak sampel yang di hitung ? : "))
                gambar = int(input("Berapa banyak gambar yang muncul ? : "))
                print("Lagi menghitung ....")
                peluang = 0
                peluang = gambar / sampel
                print("Peluang gambar yang muncul dalam 1 kejadian adalah ", peluang)
                user_input3 = input(
                    "Masih ingin melanjutkan menghitung? (y/n) : ")
                if user_input3 == 'y':
                    Start = True
                elif user_input3 == 'n':
                    print("Program Akan berhenti.")
                    Start = False
                else:
                    print("Perintah tidak diketahui, program otomatis keluar.")
                    Start = False
            elif user_input2 == 'angka':
                print("Masih dalam tahap pengembangan.")
                Start = False
        elif user_input == 'dadu':
            print("=== Program menghitung peluang mata dadu v.01 ===")
            print("Maaf, masih dalam tahap pengembangan ..")
        else:
            print("Pilihan Program tidak ditemukan")
            print("Program Akan Berhenti.")
            Start = False


menghitungPeluang()
