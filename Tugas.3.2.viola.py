def main():
    while True:
        try:
            # Mengambil input dari pengguna
            sisi1 = float(input("Masukkan sisi 1: "))
            sisi2 = float(input("Masukkan sisi 2: "))
            sisi3 = float(input("Masukkan sisi 3: "))
            
            # Memeriksa bahwa semua sisi adalah positif
            if sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0:
                print("Panjang sisi segitiga harus positif. Silakan coba lagi.")
                continue

            # Menentukan jumlah sisi yang sama
            if sisi1 == sisi2 == sisi3:
                print("3 sisi sama")
            elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
                print("2 sisi sama")
            else:
                print("Tidak ada yang sama")
            
            break  # keluar dari loop jika input valid
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

if __name__ == "__main__":
    main()
