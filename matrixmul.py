#!/usr/bin/env python3
n = int(input("Enter values of row:"))
print("Enter values for the matrix A:")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the matrix B:")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multiplication:")
print("-"* 7* n)
for x in c:
    for y in x:
        print(str(y).rjust(5),end = " ")
    print()
print("-"* 7* n)

