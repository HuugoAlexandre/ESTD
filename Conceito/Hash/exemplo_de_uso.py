from main import *

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H._slots)
print(H._valores)
print(H[17])
print(H.__len__())
H[20]='duck'
print(H.__len__())
H[66]='fly'
print(H.__len__())
print(H[20])
print(H._valores)
print(H[99])
print(H.__contains__(77))