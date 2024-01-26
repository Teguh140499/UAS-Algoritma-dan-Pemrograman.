#PROJECT STRUK BELANJA
print ("=============== WARKOP ABANG TEGUH ===============")
pembeli = input("Masukkan nama Pembeli : ")
alamat = input("Masukkan alamat Pembeli: ")
no_hp = int(input("Masukkan no. HP Pembeli: "))
import time
hari_ini = time.asctime(time.localtime(time.time()))
data = pembeli + "di" + alamat + "dengan no HP:"
print("===================================================")
print("Pesanan Atas Nama :",pembeli)


# "def" dalam Python, tujuannya adalah untuk mendefinisikan fungsi
# dan memberikan kode yang akan dijalankan ketika fungsi tersebut dipanggil.
def fungsimakanan():
    global totalmkn
    global porsi
    global mkn
    #print pada python adalah sebuah fungsi yang digunakan untuk memunculkan output yang ingin kita print pada console
    print("\n============ Daftar Menu ============")
    print("1. Mie goreng - Rp 12000")
    print("2. Mie Kuah - Rp 12000")
    print("3. Seblak Bakso - Rp 15000")
    print("4. Seblak Tulang - Rp 12000")
    print("5. Seblak Polos - Rp 8000")
    nomor=int(input("Masukkan Pilihan: "))
    porsi= int(input("Berapa Porsi:"))

    
    # if else dalam Python adalah sebuah konsep dalam pemrograman
    # yang digunakan untuk pengambilan keputusan atau kontrol aliran program.
    if nomor==1:
        totalmkn=porsi*12000
        print (porsi," porsi Mie Goreng = Rp", totalmkn)
        mkn=("Mie Goreng")
    elif nomor==2:
        totalmkn=porsi*12000
        print (porsi," porsi Mie Kuah = Rp", totalmkn)
        mkn=("Mie Kuah")
    elif nomor==3:
        totalmkn=porsi*15000
        print (porsi," porsi Seblak Bakso = Rp", totalmkn)
        mkn=("Seblak Bakso")
    elif nomor==4:
        totalmkn=porsi*12000
        print (porsi," porsi Seblak Tulang = Rp", totalmkn)
        mkn=("Seblak Tulang")
    elif nomor==5:
        totalmkn=porsi*8000
        print (porsi," porsi Seblak Polos = Rp", totalmkn)
        mkn=("Seblak Polos")
    else:
        print("Piliahan tidak ada, selahkan masukan lagi!!!")
        fungsimakanan()

def funsiminuman():
    global totalmnm
    global mnm
    global gelas
    print("\n=============== Aneka Minuman ===============")
    print("1. Kopi Susu - Rp 4000")
    print("2. Jus Sirsak - Rp 8000")
    print("3. Jus Alpukad - Rp 10000")
    print("4. Fanta Susu - Rp 6000")
    print("5. Susu Coklat - Rp 5000")
    nomor=int(input("Masukan Pilihan: "))
    gelas= int(input("Berapa Gelas: "))

    if nomor==1:
        totalmnm=gelas*4000
        print (gelas,"gelas Kopi Susu = Rp", totalmnm)
        mnm=("Kopi Susu")
    elif nomor==2:
        totalmnm=gelas*8000
        print (gelas,"gelas Jus Sirsak = Rp", totalmnm)
        mnm=("Jus Sirsak")
    elif nomor==3:
        totalmnm=gelas*10000
        print (gelas,"gelas Jus Alpukad = Rp", totalmnm)
        mnm=("Jus Alpukad")
    elif nomor==4:
        totalmnm=gelas*6000
        print (gelas,"gelas Fanta Susu = Rp", totalmnm)
        mnm=("Fanta Susu")
    elif nomor==5:
        totalmnm=gelas*5000
        print (gelas,"gelas Susu Coklat = Rp", totalmnm)
        mnm=("Susu Coklat")
    else:
        print("Pilihan tidak ada, silahkan masukan lagi!!!")
        funsiminuman()

fungsimakanan()
funsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp", totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp"))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==============================")
print("======= S T R U K   B E L A N J A =======")
print("================================")
print("Nama\t\t\t:",pembeli)
print("Alamat\t\t\t:",alamat)
print("Nomor HP\t\t:", "+62", no_hp)
print("Beli\t\t\t:",porsi,mkn,"(Rp", totalmkn,")")
print("\t\t\t:",gelas,mnm,"( Rp",totalmnm,")")
print("Total\t\t\t: Rp", totalsemua)
print("Dibayar\t\t\t: Rp",uang)
print("Kembalian\t\t: Rp",kembalian)
print("Tanggal pembelian\t:", hari_ini)
print("==============================")
print("==============================")