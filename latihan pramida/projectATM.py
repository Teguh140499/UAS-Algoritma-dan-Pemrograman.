# perintah import os ini akan menghasilkan sebuah perintah os.system('perintah')
import os

uang_saya = 0

# while true:print("ini adalah looping tak berhingga") Dalam contoh ini,
# kita menggunakan 'while True' untuk membuat perulangan yang akan terus berjalan tanpa henti.
while True:
    
    os.system('cls') #clear screen
# Perintah import os digunakan untuk bisa menggunakan perintah os.system('cls')
# yang akan digunakan sebagai pembuat efek clear screnn pada bahasa pemrograman python.
    
#print pada python adalah sebuah fungsi yang digunakan untuk memunculkan output yang ingin kita print pada console.         
    print('\nSELAMAT DATANG DI ATM')
    print('PILIH OPTION\n')
    print('1. Cek Uang Saya')
    print('2. Ambil Uang Saya')
    print('3. Tabung Uang Saya\n')

    
    # if else dalam Python adalah sebuah konsep dalam pemrograman
    # yang digunakan untuk pengambilan keputusan atau kontrol aliran program.
    option = int(input('Silahkan Pilih Option:'))
    if option == 1:
        print('Uang Kamu:', uang_saya)
    elif option == 2:
        print('Uang Kamu:', uang_saya)
        uang_ambil = int(input('Masukkan Jumlah Uang: '))
        if (uang_saya - uang_ambil) < 0:
            print('Tidak Cukup Uang!')
        else:
            uang_saya -= uang_ambil
            print('Berhasil Diambil:', uang_ambil)
            print('Uang Kamu Sekarang:', uang_saya)
    elif option == 3:
        print('Uang Kamu:', uang_saya)
        uang_tabung = int(input('Masukkan Jumlah Uang: '))
        uang_saya += uang_tabung
        print('Berhasil Ditabung:', uang_tabung)
        print('Uang Kamu Sekarang:', uang_saya)

    lanjut = input("Lanjut Bertransaksi? (YES/NO) : ")
    if lanjut == "NO":
        print("\nTerimakasih Telah Bertransaksi")
        print(int(input('Berikan Rating: ')))    