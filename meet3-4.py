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
