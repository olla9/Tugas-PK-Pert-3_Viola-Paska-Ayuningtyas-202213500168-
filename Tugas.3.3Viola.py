def main():
    # Jumlah hari dalam bulan untuk tahun 2020
    hari_per_bulan = {
        1: 31,  # Januari
        2: 29,  # Februari (tahun kabisat)
        3: 31,  # Maret
        4: 30,  # April
        5: 31,  # Mei
        6: 30,  # Juni
        7: 31,  # Juli
        8: 31,  # Agustus
        9: 30,  # September
        10: 31, # Oktober
        11: 30, # November
        12: 31  # Desember
    }

    while True:
        try:
            bulan = int(input("Masukkan bulan (1-12): "))
            
            if bulan < 1 or bulan > 12:
                print("Bulan yang diinputkan tidak valid. Silakan masukkan bulan antara 1 dan 12.")
                continue
            
            jumlah_hari = hari_per_bulan[bulan]
            print(f"Jumlah hari: {jumlah_hari}")
            break  # keluar dari loop jika input valid
            
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

if __name__ == "__main__":
    main()
