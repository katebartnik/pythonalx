f = open("test")
for line in f:
    print(line) # print f.read wyplucie całego pliku / dla małych pliczków

f.close()


#Drugi przykład

f = open("test")
for _ in f:
    print(_)

f.close()

# Trzeci przykład - TAK PRACUJEMY Z PLIKAMI!!!!!!!!
# Manager kontekstu

with open("test", encoding='utf-8') as f:
    for l in f:
        print(l.upper())
