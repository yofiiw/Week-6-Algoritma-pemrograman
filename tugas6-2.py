tinggi = int(input("Masukkan Tinggi Segitiga Pascal = "))
for i in range(tinggi):
  pascal = 1
  print(" " * (tinggi - i), end="")
  for j in range(i + 1):
    print(pascal, end=" ")
    pascal = pascal * (i - j) // (j + 1)
  print()
