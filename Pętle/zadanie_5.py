print(1, 2, 3, 4, sep="-")


for i in range(5):
    print(i)

for i in range(5):
    print(i, end="-")

print()
for i in range(5):
    print(f"(i:5)", end="")

for i in range(5):
    for j in range(5):
        print(i*j)

