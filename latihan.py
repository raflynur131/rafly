nama = "Rafly"
nim = "240441100056"
ipk = 4.00
mahasiswa = True

print("Nama saya adalah", nama)
#ini adalah format natural (tipe data sama)
print("Nim saya adalah", nim)
print("Impian ipk saya adalah", ipk)
print("saya merupakan mahasiswa", mahasiswa)

#ini adalah format string (tipe data bisa diubah menjadi string)
print(f'Nim saya adalah {nim}')

#program dinamis string
nama_panajang = str(input ("nama saya adalah:"))

#program dinamis integer
nilai_matematika = int(input ("Nilai saya adalah:"))

nilai_matematika = 89
nilai_biologi = 75
nilai_kimia = 90
nilai_fisika = 82

penjumlahan = nilai_matematika + nilai_kimia
perkalian = nilai_matematika * nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
pembagian = nilai_matematika / nilai_kimia

print(f'Hasil penjumlahan dari matematika dan kimia adalah:{penjumlahan}')
print(f'Hasil penjumlahan dari matematika dan kimia adalah:{perkalian}')
print(f'Hasil penjumlahan dari matematika dan kimia adalah:{pengurangan}')
print(f'Hasil penjumlahan dari matematika dan kimia adalah:{pembagian}')


usia_masuk_kuliah = int(input("Berapa usia anda?"))
lama_kuliah = int(input("Berapa lama kuliah anda?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f'Saya, bernama {nama} saya berumur {usia_saat_ini}')
print(f'Saya, bernama {nama} akan lulus pada tahun {tahun_lulus}')