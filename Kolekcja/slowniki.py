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
print({[1,2 ]: "pierwsza"})




