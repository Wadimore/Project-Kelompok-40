from kelompok import *

kelompok = no_kelshift.kelshift(40,6)

anggota1 = 'Abdul Fattah Rahmadiansyah'
anggota2 = 'Muhammad Affan Pasha'
anggota3 = 'Vicky Setyo Haryadi'
anggota4 = 'Syafiq Naufal Musyaffa'

nim1 = 21120122120028 
nim2 = 21120122140090
nim3 = 21120122130066
nim4 = 21120122140107

print(anggota1, nim1)
print(anggota2, nim2)
print(anggota3, nim3)
print(anggota4, nim4)

def judul():
        return print('\n===== Program Konversi Basis Desimal ======')

def menu():
        print('| Konversi Ke:                      |')
        print('| 1. Biner                          |')
        print('| 2. Oktal                          |')
        print('| 3. Hexadecimal                    |')
        print('| 4. keluar                         |')
        print('=====================================')
        opsi = input('Pilih Menu : ')
        if opsi == '1':
            biner()
        elif opsi == '2':
            oktal()
        elif opsi == '3':
            hexadecimal()
        elif opsi == '4':
            keluar()
        else:
            print ('')
            print ('Angka yang Anda masukkan salah!')
            print ('')
            menu()

def biner():
        tampil = ''
        cetak = []
        desimal = int (input('Masukan angka desimal:'))
        print ('')
        while desimal != 0:
            hasil = desimal % 2 
            cetak.insert(0, str(hasil)) 
            desimal = desimal//2 
            if desimal == 0:
                for i in range (len(cetak)): 
                    tampil +=  cetak[i]
        print ('Hasilnya adalah : ', tampil)
        print ('')
        kembali = input('Ulangi Konversi? [y/t]')
        if kembali == "y" or kembali == "Y":
            biner()
        else:
            print ('')
            menu()

def oktal():
        tampil = ''
        cetak = []
        desimal = int (input('Masukan angka desimal :'))
        print ('')
        while desimal != 0:
            hasil = desimal % 8 
            cetak.insert(0, str(hasil)) 
            desimal = desimal//8  
            if desimal == 0:
                for i in range (len(cetak)): 
                    tampil +=  cetak[i]
        print ('Hasilnya adalah : ', tampil)
        print ('')
        kembali = input('Ulangi Konversi? [y/t]')
        if kembali == "y" or kembali == "Y":
            oktal()
        else:
            print ('')
            menu()

def hexadecimal():
        tampil = ''
        cetak = []
        desimal = int (input('Masukan angka desimal :'))
        print ('')
        while desimal != 0:
            hasil = desimal % 16 
            if hasil == 10:
                hasil = 'A'
            if hasil == 11:
                hasil = 'B'
            if hasil == 12:
                hasil = 'C'
            if hasil == 13:
                hasil = 'D'
            if hasil == 14:
                hasil = 'E'
            if hasil == 15:
                hasil = 'F'
            cetak.insert(0, str(hasil))
            desimal = desimal//16 
            if desimal == 0:
                for i in range (len(cetak)): 
                    tampil +=  cetak[i]
        print ('Hasilnya adalah : ',tampil)
        print ('')
        kembali = input('Ulangi Konversi? [y/t]')
        if kembali == "y" or kembali == "Y":
            hexadecimal()
        else:
            print ('')
            menu()

def keluar():
    exit()

judul()
menu()
