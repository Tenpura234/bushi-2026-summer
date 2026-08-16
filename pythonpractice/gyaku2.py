import re
import random
from decimal import Decimal
from fractions import Fraction
from turtledemo.round_dance import stop

#線形代数講義[増補版]p40の手順に従う
#A = [[0,0,2,-3,1],[2,4,-8,8,-12],[1,2,-3,3,-4]]
#A = [[0,0,2,-3,1],[0,5,-8,8,-12],[0,1,-3,3,-4]]

A = [[random.randint(-9, 9) for j in range(3)] for i in range(3)]
#A = [[1,0,1],[0,0,1],[0,0,2]]
#A = [[2,0,0],[0,2,0],[0,0,2]]
def output(a):
    b = [[0 for j in range(len(a[0]))] for i in range(len(a))]
    for j in range(len(a[0])):
        for i in range(len(a)):
            b[i][j] = str(a[i][j])
    print(" ", *b, sep="\n")

output(A)

i = 0
j = 0
k = 0
process_row = 0
stop = False

gyoretsushiki = False
#ifなんとか:
#gyoretsushiki = True
m = 1

while process_row < len(A):
    i = process_row
    j= 0
#Step1
    while A[i][j] == 0:
        if i == len(A)-1 and A[i][j] == 0:
            i = process_row
            j = j + 1
            if j > len(A[0]) - 1:
                stop = True
                break
            continue
        if stop == True:
            break
        i = i + 1
    if j > len(A[0])-1:
        break
    print(f"A{i+1,j+1}に注目")
    tmp_i = i
    tmp_j = j
#Step2
    k = process_row
    while A[k][tmp_j] == 0:
        k = k + 1
    if process_row+1 != tmp_i+1:
        for j in range(len(A[0])):
            tmp = A[process_row][j]
            A[process_row][j] = A[tmp_i][j]
            A[tmp_i][j] = tmp
        print(f"{process_row+1}行目 ⇔ {tmp_i+1}行目")
        if gyoretsushiki == True:
            m = -m
            print(f"倍数m:{m}")
        tmp_i = process_row
        output(A)
#Step3
    if A[tmp_i][tmp_j] != 1:
        k = A[tmp_i][tmp_j]
        print(f"{tmp_i + 1}行目/ {k}")
        if gyoretsushiki == True:
            m = m * k
            print(f"倍数m:{m}")
        for j in range(len(A[0])):
            A[tmp_i][j] = Fraction(A[tmp_i][j] ,k)

    output(A)
#Step4
    for i in range(process_row if gyoretsushiki == True else 0, len(A)):
        if A[i][tmp_j] != 0 and i != tmp_i:
            k = A[i][tmp_j]
            for j in range(len(A[0])):
                A[i][j] = A[i][j] - A[tmp_i][j] * k
            print(f"{i + 1}行目 - {tmp_i + 1}行目 × {k}")

    output(A)
    process_row = process_row + 1
    print("row=",process_row)
    if gyoretsushiki == True:
        print(f"倍数m:{m}")