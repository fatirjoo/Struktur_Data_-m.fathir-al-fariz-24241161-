# FINAL PROJECT UAS

def meet1():
    print("\n=== MEET 1: Tabel Kebenaran Perbandingan Boolean ===")
    a = 24
    b = 53
    print("a < b:", a < b)
    print("a > b:", a > b)
    print("a <= b:", a <= b)
    print("a != b:", a != b)
    print("a not b:", "a not b") 

def meet2():
    print("\n=== MEET 2: Operasi Logika ===")
    x = True
    z = not x
    print("Nilai dari z =", z)

    print("\n********** AND ***********")
    kombinasi = [(True, True), (True, False), (False, True), (False, False)]
    for x, y in kombinasi:
        z = x and y
        print(f"{x} and {y} = {z}")

def meet3_dan_4():
    print("\n=== MEET 3 dan 4: Luas dan Gambar Segitiga ===")
    alas = int(input("Masukkan alas segitiga: "))
    tinggi = int(input("Masukkan tinggi segitiga: "))

    if alas > 0 and tinggi > 0:
        luas = 0.5 * alas * tinggi
        print(f"\nLuas segitiga adalah: {luas:.2f}\n")
        print("Gambar segitiga:")
        for i in range(1, tinggi + 1):
            print(' ' * (tinggi - i) + '*' * (2 * i - 1))
    else:
        print("Alas dan tinggi harus lebih dari 0!")

def meet5():
    print("\n=== MEET 5: Kalkulator Sederhana ===")
    print("Masukkan dua angka dan pilih operasi (+, -, *):")
    operasi = input("Operasi: ")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if operasi == "+":
        print("Hasil =", angka1 + angka2)
    elif operasi == "-":
        print("Hasil =", angka1 - angka2)
    elif operasi == "*":
        print("Hasil =", angka1 * angka2)
    else:
        if angka2 != 0:
            print("Hasil =", angka1 / angka2)
        else:
            print("Tidak bisa membagi dengan nol")

def meet6():
    print("\n=== MEET 6: Pengecekan Hak Akses ===")
    hak_akses = input("Masukkan hak akses Anda: ").lower()
    print("Full akses" if hak_akses == "admin" else "Akses denied")

def meet7():
    print("\n=== MEET 7: Pengecekan Panjang Password ===")
    password = input("Masukkan password: ")
    if len(password) < 8:
        print("Karakter kurang")
    else:
        print("Karakter cukup")
    
    if len(password) > 8:
        print("Karakter kurang")
    else:
        print("Karakter cukup")

def meet8():
    print("\n=== MEET 8: String Angka ===")
    number = "1234567890"
    print("a. Data terakhir:", number[-1])
    print("b. Data pertama:", number[0])
    print("c. Data ke-3 sampai ke-6:", number[2:6])

def meet9_10():
    print("\n=== MEET 9 dan 10: Pemisahan Domain ===")
    domain = input("Masukkan nama domain anda (contoh: adel.com): ")
    if "." in domain:
        nama, ekstensi = domain.split(".")
        print("Nama domain anda adalah =", nama)
        print("Nama yang anda gunakan adalah =", ekstensi)
    else:
        print("Format domain tidak valid!")

# HEADER
print("##### Kelompok #####")
print("M.ADEL FITRAH (24241153)")
print("M.FATHIR AL FARIZ (24241161)")
print("###################")

# MENU UTAMA
while True:
    print("\nDaftar program")
    print("1. MEET 1 (Perbandingan Boolean)")
    print("2. MEET 2 (Operasi Logika)")
    print("3. MEET 3 dan 4 (Segitiga dan Gambar)")
    print("4. MEET 5 (Kalkulator Sederhana)")
    print("5. MEET 6 (Hak Akses)")
    print("6. MEET 7 (Cek Password)")
    print("7. MEET 8 (Manipulasi String Angka)")
    print("8. MEET 9 dan 10 (Pemisahan Domain)")
    print("0. Keluar")

    pilihan = input("Masukkan nomor program yang ingin dijalankan: ")

    if pilihan == "1":
        meet1()
    elif pilihan == "2":
        meet2()
    elif pilihan == "3":
        meet3_dan_4()
    elif pilihan == "4":
        meet5()
    elif pilihan == "5":
        meet6()
    elif pilihan == "6":
        meet7()
    elif pilihan == "7":
        meet8()
    elif pilihan == "8":
        meet9_10()
    elif pilihan == "0":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")