dna = input("masukan sekuens DNA: ").upper()

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

print("_"*50)
print("jumlah A:", a)
print("jumlah T:", t)
print("jumlah G:", g)
print("jumlah C:", c)

total = a + t + g + c
gc =(g + c) / total * 100


print("GC Content adalah:", gc, "%")

if gc >= 60:
    print("predikat DNA = GC tinggi")
elif gc >= 40:
    print("predikat DNA = GC sedang")
else:
    print("predikat DNA = GC rendah")
