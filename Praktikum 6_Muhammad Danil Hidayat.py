# -*- coding: utf-8 -*-
"""
@Hari/Tanggal : 20210111
@Judul : Praktikum 6
@author: Muhammad Danil Hidayat
@NIM : 065002100032
"""

def nilai_siswa ():
    skor = 0    
    ulang = 1
    nomor = 0
    while ulang == 1:
        nomor += 1
        x = str(input('tekan ENTER untuk mencari rata-rata!\nNilai siswa: '))
        if x == '': 
            nomor -= 1
            ulang = 0
        else:
            if x == 'A': 
                skor += float(4)
                a = '4'
            elif x == 'A-':
                skor += float(3.75)
                a = '3,75'
            elif x == 'B+':
                skor += float(3.50)
                a = '3,5'
            elif x == 'B':
                skor += float(3.00)
                a = '3'
            elif x == 'B-':
                skor += float(2.75)
                a = '2,75'
            elif x == 'C+':
                skor += float(2.50)
                a = '2,5'
            elif x == 'C':
                skor += float(2.00)
                a = '2'
            elif x == 'C-':
                skor += float(1.75)
                a = '1,75'
            else:
                print('data infalid')
                nomor -= 1
                a = 'TAK TERDEFINISI'
            print(f"nilai ke-{nomor} = {a}")
    rata2 = skor / nomor
    return rata2

print("rata rata nilai adalah", nilai_siswa())