""" Program python sederhana - Calculator
----------------------------------------
"""
def addition ():
    print("Penambahan")
    n = float(input("Silahkan masukkan angka: "))
    t = 0
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Silahkan masukkan angka lain (masukkan 0 untuk menghitung): "))
    return [ans,t]
def subtraction ():
    print("Pengurangan")
    n = float(input("Silahkan masukkan angka: "))
    t = 0
    ans = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Silahkan masukkan angka lain (masukkan 0 untuk menghitung): "))
    return [ans,t]
def multiplication ():
    print("Perkalian")
    n = float(input("Silahkan masukkan angka: "))
    t = 0 #Total number enter
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Silahkan masukkan angka lain (masukkan 0 untuk menghitung): "))
    return [ans,t]
def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]
 
while True:
    list = []
    print(" Program Python pertamaku!")
    print(" Tulis 'a' untuk penambahan")
    print(" Tulis 's' untuk pengurangan")
    print(" Tulis 'm' untuk perkalian")
    print(" Tulis 'v' untuk average")
    print(" Tulis 'q' untuk keluar")
    c = input("seleksi: ")
    if c != 'q':
        if c == 'a':
            list = addition()
            print("Jawaban = ", list[0], " total inputs ",list[1])
        elif c == 's':
            list = subtraction()
            print("Jawaban = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Jawaban = ", list[0], " total inputs ",list[1])
        elif c == 'v':
            list = average()
            print("Jawaban = ", list[0], " total inputs ",list[1])
        else:
            print ("Maaf, karakter tidak valid")
    else:
        break