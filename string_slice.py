#
#array slicing
#

s = "Hello"
print(s[0:5]) #od indeksu 0 do 4 włącznie
print(s[-3]) #3ci znak od końca

s = "Ruda tańczy jak szalona"
arr = s.split(" ")
print(arr[0]) # pierwszy element listy
print(s[0:16:2]) #co drugi znak od indeksu 0 do 15 włącznie
print(s[::3]) #cały string co 3 znak

#reverse w Pythonie
print(s[::-1]) #który język zrobi to krócej :P

print("Hello"+"World")

a = "Hello"
b = "alx"

print(f"{a} {b} {1+2}")
print("{} {} {}".format(a, b, 1+6))

x = input("Podaj wartość x")
print(x, type(x))

x = int(x, type(x))








