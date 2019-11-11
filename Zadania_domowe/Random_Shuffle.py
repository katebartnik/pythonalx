
import random

osoby = ['marek', 'przemek', "michał", "kamila"]

osoby2 = ['marek', 'przemek', "michał", "kamila"]

random.shuffle(osoby)
random.shuffle(osoby2)

mapped = zip(osoby, osoby2)

for persons in mapped:
    print(persons[0] + ' kupuje prezent dla ' + persons[1])



