#Przypomnienie
# int, float, complex, str, str,
# list [], tuple ()
# dict {}

print(dict())
x = dict()
print(type(x))

pol_ang = {
    # "klucz" : "wartość"
    "klucz" : "key",
    "wartość" : "value",
    "pies" : "dog",
}

print(pol_ang)
print(pol_ang["pies"])
print("dog" in pol_ang)

if "dog" in pol_ang:
    print(pol_ang["dog"])

print(dir(pol_ang))

print(pol_ang.get("dog", "Brak takiego hasła"))
print(pol_ang.get("pies", "Brak takiego hasła"))

pol_ang['kot'] = "cat"
print(pol_ang)

print({1:"a", 2: "b"})
print({1.1:"a", 2.1: "b"})


x = "2123123"
y = [1,2,3]

print(pol_ang.pop("pies"))
print(pol_ang)

print(pol_ang.popitem())
print(pol_ang)

# set {}

zbior = {1, 2, 3, 4}
print(zbior, type(zbior))
print(dir(zbior))

zbior2 = {1, "a", 2, "b", "c", "z", 3}
print(zbior2)
zbior2.add(9)
print(zbior2)
zbior2.add("a")
print(zbior2)

lista = [1, 1, 1, 2, 4, 4,]
print(set(lista))

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Suma zbiorów: ", A | B, A.union(B))
print("Różnica zbiorów: ", A - B, A.difference(B))
print("Część wspólna, przeciecie: ", A & B, A.intersection(B))
print("Różnica symetryczna", A ^ B, A.symmetric_difference(B))
print("Podzbiór", A.issubset(C))
print("Podzbiór", A.issubset(A))

