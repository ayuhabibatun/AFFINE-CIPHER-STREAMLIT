from sympy import randprime
import random
import math

# Ambil dua bilangan prima secara acak
p = randprime(2, 10**2)
q = randprime(2, 10**2)
print("Bilangan prima pertama (p) = ",p)
print("Bilangan prima kedua (q) = ",q)

# Hitung nilai n
n = p * q
print("Nilai n = ",n)

# Hitung phi(n)
phi_n = (p - 1) * (q - 1)
print("Nilai phi(n):", phi_n)

# Cari kunci publik e (yang relatif prima dengan phi_n)
e = random.randint(2, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(2, phi_n - 1)
print("Kunci publik (e):", e)

# Hitung kunci privat d (invers dari e mod phi_n)
d = pow(e, -1, phi_n)
print("Kunci privat (d):", d)

# Minta input pesan dari user
pesan = input("\nMasukkan pesan yang ingin dienkripsi: ")

# Ubah setiap karakter dalam pesan jadi angka ASCII
pesan_ke_angka = [ord(karakter) for karakter in pesan]
print("Pesan dalam angka (ASCII):", pesan_ke_angka)

# Enkripsi setiap angka dengan rumus RSA: c = m^e mod n
pesan_terenkripsi = []
for angka in pesan_ke_angka:
    hasil = pow(angka, e, n)
    pesan_terenkripsi.append(hasil)
print("Pesan setelah dienkripsi:", pesan_terenkripsi)

# Dekripsi: m = c^d mod n
pesan_terdekripsi = []
for angka_enkripsi in pesan_terenkripsi:
    hasil = pow(angka_enkripsi, d, n)
    pesan_terdekripsi.append(hasil)

# Ubah kembali angka ASCII ke karakter
hasil_pesan = ''.join(chr(angka) for angka in pesan_terdekripsi)
print("Pesan setelah dekripsi:", hasil_pesan)