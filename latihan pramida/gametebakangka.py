# Modul Random pada Python adalah modul yang berisi daftar fungsi
# yang digunakan untuk melakukan operasi-operasi yang berkaitan dengan bilangan acak/random.
import random

# Metode ini randint()mengembalikan elemen bilangan bulat yang dipilih dari rentang yang ditentukan.
# Catatan: Metode ini merupakan alias untuk randrange(start, stop+1).
angka_rahasia = random.randint(1, 100)
print('=' * 40)
print('Kami telah memiliki angka, silakan tebak!')
print('=' * 40)

# while true:print("ini adalah looping tak berhingga") Dalam contoh ini,
# kita menggunakan 'while True' untuk membuat perulangan yang akan terus berjalan tanpa henti.
while True:
    jawaban = int(input('\nMasukkan angka: '))

    if jawaban == angka_rahasia:
        print('Selamat, tebakanmu benar!')
        break # berhenti paksa
    else:
        print('Tebakanmu terlalu','kecil' if jawaban < angka_rahasia else 'besar' )
batas_percobaan = 5
for percobaan in range(batas_percobaan):
    jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukkan angka: '))
        
    if jawaban == angka_rahasia:
        print('Selamat, tebakanmu benar!')
        break
    else: 
        print('Tebakanmu terlalu','kecil' if jawaban < angka_rahasia else 'besar')
else:
        print(f'\nSayang sekali, kamu sudah salah menebak sebanyak {batas_percobaan}x!')