#!/usr/bin/python3

counter = 0
def myprint(i, j):
    for item in range (j + 1):
        if i % 100 == 0:
            print()
        print(i,end='\t')
        i += 1
        global counter
        counter += 1
        if counter % 8 == 0:
            print()


for i in range(1, 256, 2):
    myprint(i, 0)

print()
print()
print()
print()

for i in range(2, 256, 4):
    myprint(i, 1)

print()
print()
print()
print()

for i in range(4, 256, 8):
    myprint(i, 3)

print()
print()
print()
print()

for i in range(8, 256, 16):
    myprint(i, 7)

print()
print()
print()
print()

for i in range(16, 256, 32):
    myprint(i, 15)

print()
print()
print()
print()

for i in range(32, 256, 64):
    myprint(i, 31)

print()
print()
print()
print()

for i in range(64, 256, 128):
    myprint(i, 63)

print()
print()
print()
print()

for i in range(128, 256, 256):
    myprint(i, 127)

print()
print()
print()
print()