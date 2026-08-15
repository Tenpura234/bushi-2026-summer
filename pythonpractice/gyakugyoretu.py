import re
from decimal import Decimal
from fractions import Fraction

#A = [[0,0,2,-3,1],[2,4,-8,8,-12],[1,2,-3,3,-4]]
A = [[0,0,2,-3,1],[2,4,-8,8,-12],[0,2,-3,3,-4]]

def output(a):
    b = [[0 for j in range(len(a[0]))] for i in range(len(a))]
    for j in range(len(a[0])):
        for i in range(len(a)):
            b[i][j] = str(a[i][j])
    print(" ", *b, sep="\n")

i = 0
j = 0
k = 0
processed_row = -1
l = 1
m = 0
tmp_i = 0
tmp_j = 0


output(A)
while A[i][j] == 0:
    i = i + 1
    if i == len(A)-1 and A[i][j] == 0:
        i = 0
        j = j + 1
print(f"({i+1}行目,{j+1}列目)を選択")
tmp_i = i
tmp_j = j
tmp = A[i][j]
for j in range(len(A[0])):
    A[i][j] =Fraction(str(A[i][j]/tmp))
print(f"{i+1}行目 / {tmp}")
output(A)

i = 0
j = 0
for i in range(len(A)):
    if A[i][tmp_j] != 0 and i != tmp_i:
        print("繰り返し　i=", i)
        print(f"{i + 1}行目 - {tmp_i + 1}行目　× {A[i][tmp_j]}")
        k = A[i][tmp_j]
        for j in range(len(A[0])):
            A[i][j] = A[i][j] - A[tmp_i][j] * k
        output(A)
        print(f"i={i},j={j}")
i = tmp_i
j = tmp_j



