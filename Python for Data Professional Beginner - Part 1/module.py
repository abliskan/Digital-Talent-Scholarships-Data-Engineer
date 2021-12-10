#Chapter1 - Mari mengenal python
"""
##Program pertama: "Hello World"
print("Hello World!")

##Program Pertamaku
print("Riset Bahasa Python")

##Struktur Program Python - Part 1
### Statement
print("Belajar Python menyenangkan") 
print("Halo Dunia")
print("Hello World!")
### Variables & Literals
bilangan1 = 5
bilangan2 = 10
kalimat1 = "Belajar Bahasa Python"
### Operators
print(bilangan1 + bilangan2)

## Tugas Praktek - 1
bilangan1 = 20
bilangan2 = 10
print(bilangan1 - bilangan2)

## Tugas Praktek - 2
harga_asli = 20000
potongan = 2000
harga_setelah_potongan = harga_asli - potongan
harga_final = harga_setelah_potongan * 1.1
print(harga_final)

## Quiz 1

## Quiz 2

#Chapter2 - Mari mengenal python

## Quiz 1

## Quiz 2

## Tipe data dasar: Null, Boolean, Numeric, dan Text

## Quiz 1

## Quiz 2

## Sequence type - 1
contoh_list = [1, 'dua', 3, 4.0, 5]
print(contoh_list[0])
print(contoh_list[3])
contoh_list = [1, 'dua', 3, 4.0, 5]
contoh_list[3] = 'empat'
print(contoh_list[3])

## Sequence type - 2
contoh_tuple = ('Juni', 'Juli', 'Agustus', 'September')
print(contoh_tuple[0])

## Set Type
contoh_list = ['Dewi', 'Budi', 'Cici', 'Linda', 'Cici'] 
print(contoh_list)
contoh_set = {'Dewi', 'Budi', 'Cici', 'Linda', 'Cici'}
print(contoh_set)
contoh_frozen_set = ({'Dewi', 'Budi', 'Cici', 'Linda', 'Cici'}	)
print(contoh_frozen_set)

## Mapping Type
person = {'nama': 'John Doe', 'pekerjaan': 'Programmer'}
print(person['nama'])
print(person['pekerjaan'])

## Tugas Praktek - 1
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000 }
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000 }
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000 }

## Tugas Praktek - 2
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000} 
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000} 
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000} 
daftar_belanja = [sepatu, baju, celana]

## Tugas Praktek - 3
### Data yang dinyatakan ke dalam dictionary
sepatu = {"nama": "Sepatu Niko", "harga": 150000, "diskon": 30000} 
baju = {"nama": "Baju Unikloh", "harga": 80000, "diskon": 8000} 
celana = {"nama": "Celana Lepis", "harga": 200000, "diskon": 60000}
### Hitunglah harga masing-masing data setelah dikurangi diskon
harga_sepatu = sepatu["harga"] - sepatu["diskon"] 
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
### Hitung harga total
total_harga = harga_sepatu + harga_baju + harga_celana
### Hitung harga kena pajak
total_pajak = total_harga * 0.1
### Cetak total_harga + total_pajak
print(total_harga+total_pajak)
"""
#Chapter3 - Pythons Conditioning & Looping
## Python conditioning for decision - part 1

## Python conditioning for decision - part 2
# Statement if
x = 4
if x % 2 == 0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua") # statemen aksi lebih menjorok ke dalam
# Statement if ... elif ... else
x = 7
if x % 2 == 0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua")
elif x % 3 == 0: # jika sisa bagi x dengan 3 sama dengan 0
    print("x habis dibagi tiga")
elif x % 5 == 0: # jika sisa bagi x dengan 5 sama dengan 0
    print("x habis dibagi lima")
else:
    print("x tidak habis dibagi dua, tiga ataupun lima")
 