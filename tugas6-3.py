baris = int(input("Masukkan Baris Segitiga Pascal = "))
print("Angka dari Baris ke", baris, "Adalah = ", end="")
pascal = 1
jumlah = 0
for i in range(1, baris + 1):
    print(pascal, end=" ")
    jumlah += pascal
    pascal = pascal * (baris - i) // i
print("\nDengan Total Penjumlahan-nya = ",jumlah)
