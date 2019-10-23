my_list = [1, "a", "ala", "kot", 121]
print(my_list)
print(my_list[0])

my_list2 = [1, 2, 3, my_list]
print(my_list2[3][1])
print(dir(my_list))

my_list.append(10) #dodaje elementy do listy
print(my_list)

my_list.pop() #zabiera z listy elementy
print(my_list)
print(my_list.index(1))
print(my_list.index("a"))
print(my_list.count("a"))

a = [1, 2, 3]
b = [3, 4, a]

print(a)
print(b)
a.append(10) #10 doda się i do listy a i listy b

print(1 in x) #Sprawdzanie czy cos sie w czyms zawiera



