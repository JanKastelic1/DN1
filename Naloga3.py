x = float(input("Vnesite prvo stevilo: "))
y = float(input("Vnesite drugo stevilo: "))
z = float(input("Vnesite tretje stevilo: "))
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
if y == x or z <= x:
    print(True)
else:
    print(False)