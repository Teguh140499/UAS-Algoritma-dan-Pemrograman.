#PROJECT REKAP NILAI
#Deklarasi Fungsi
def fungsi_total_nilai(var_harian, var_uts, var_uas) :
    var_harian = int(var_harian) * 0.3
    var_uts = int(var_uts) * 0.3
    var_uas = int(var_uas) * 0.4

    var_total = var_harian + var_uts + var_uas
    return var_total
#Deklarasi Fungsi Perulangan
def fungsi_perulangan():
    var_hasil_perulangan = 0
    for i in range(1,7): 
    # FOR merupakan sebuah pernyataan mengulang suatu proses yang telah diketahui jumlah perulangannya.
    # Range di Python adalah fungsi bawaan yang berguna untuk menghasilkan deret angka sesuai dengan pola tertentu.    
        print("--------Nilai Ke ",i,"--------")
        var_harian = input("Nilai Harian : ")
        var_uts = input("Nilai UTS : ")
        var_uas = input("Nilai UAS : ")

        #Pemanggilan fungsi Penjumlahan
        var_hasil_perulangan +=(int(fungsi_total_nilai(var_harian, var_uts, var_uas)))

    return var_hasil_perulangan /i
#Deklarasi Fungsi Operator
def fungsi_total_nilai(var_harian, var_uts, var_uas) :
    var_harian = int(var_harian) * 0.3
    var_uts = int(var_uts) * 0.3
    var_uas = int(var_uas) * 0.4

    var_total = var_harian + var_uts + var_uas
    return var_total

#Deklarasi Fungsi Percabangan
def fungsi_percabangan (var_nilai) :
    var_huruf = ""
    if (var_nilai >= 0 and var_nilai < 20) :
        var_huruf = "E"
    elif (var_nilai >= 20 and var_nilai < 40) :
        var_huruf = "D"
    elif (var_nilai >= 40 and var_nilai < 60) :
        var_huruf = "C"
    elif (var_nilai >= 60 and var_nilai < 80) :
        var_huruf = "B"
    elif (var_nilai >= 80 and var_nilai < 100) :
        var_huruf = "A"
    return var_huruf
     # if else dalam Python adalah sebuah konsep dalam pemrograman
     # yang digunakan untuk pengambilan keputusan atau kontrol aliran program.
     # Dalam Python, fungsi bisa mengembalikan nilai menggunakan kata kunci return.
     # Nilai yang dikembalikan ini bisa berupa hasil operasi dalam fungsi, nilai variabel, atau struktur data lainnya.

#Deklarasi Fungsi Perulangan
def fungsi_perulangan():
    var_hasil_perulangan = 0
    for i in range(1,7):
        print("--------Nilai Ke ",i,"--------")
        var_harian = input("Nilai Harian : ")
        var_uts = input("Nilai UTS : ")
        var_uas = input("Nilai UAS : ")

        #Pemanggilan fungsi Penjumlahan
        var_hasil_perulangan +=(int(fungsi_total_nilai(var_harian, var_uts, var_uas)))

    return var_hasil_perulangan /i


#Pemanggilan fungsi perulangan
var_total = fungsi_perulangan()

print("--------Total Nilai --------")
print("Total nilai yang didapat : ",var_total)

#Pemanggilan Fungsi Percabangan
print("Total Nilai Dalam Huruf : ", fungsi_percabangan(var_total))