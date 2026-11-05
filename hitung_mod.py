#input
angka1 = int(input("masukan angka pertama: "))
angka2 = int(input("masukan angka kedua: "))

#proses
if angka2 !=0:
    hasil = angka1 % angka2
    status_sukses = True
else:
    status_sukses = False

#output
if status_sukses:
    print(f"\nHasil dari {angka1} mod {angka2} adalah: {hasil}")
else:
    print("\nError: angka pembagi tidak boleh nol!")
