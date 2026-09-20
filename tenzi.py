import re
from decimal import Decimal
from fractions import Fraction



# def tableinput(a):
#     name = a
#     row = 0
#     i = 0
#     pre = []
#     print(f"行列 {name} を入力\n入力例:1 1.2 2/3 351\nendと入力して行入力終了")
#     while row != "end":
#         row = input(str(i+1)+ "行目:")
#         if row == "end":
#             breal
#         pre.insert(i, row)
#         row_count = len(pre[0].split())
#         if re.search(r"[^\d./ -]", row) and row != "end":
#             print("数字と-./以外入れるなボケ")
#             del pre[i]
#             continue
#         elif row_count != len(pre[int(i)].split()):
#             print("列数がちげーよボケ")
#             del pre[i]
#             continue
#         print(*pre, sep="\n")
#         i = i + 1
#         
#     a = [[Fraction(x) for x in s.split()] for s in pre]
#     print(f"\n行列{name}の入力終了")
#     print(*a, sep="\n")
#     return a

A = [[1,2,-1,2],[2,-1,3,9],[3,1,1,8]]
import random

#A = [[random.randint(-9, 9) for j in range(8)] for i in range(3)]
#A = [[0,0,0,0],[0,-0,0,9],[3,1,1,8]]
def simplify(a):
    #Step1
    k = 0
    while k < len(a):
        i = k
        j = 0
        while j < len(a[0]) and a[i][j] == 0:
            if i == len(a)-1:
                i = k
                j = j + 1
            else:
                i = i + 1
        if j >= len(a[0]):
            break
        print(f"a{i+1,j+1}に注目")
        tmp_i = i
        tmp_j = j
    #Step2
        l = k
        while a[l][tmp_j] == 0:
            l = l + 1
        if k+1 != tmp_i+1:
            for j in range(len(a[0])):
                tmp = a[k][j]
                a[k][j] = a[tmp_i][j]
                a[tmp_i][j] = tmp
            print(f"{k+1}行目 ⇔ {tmp_i+1}行目")
            tmp_i = k
            output(a)
    #Step3
        if a[tmp_i][tmp_j] != 1:
            l = a[tmp_i][tmp_j]
            print(f"{tmp_i + 1}行目/ {l}")
            for j in range(len(a[0])):
                a[tmp_i][j] = Fraction(a[tmp_i][j] ,l)
        output(a)
    #Step4
        for i in range(0, len(a)):
            if a[i][tmp_j] != 0 and i != tmp_i:
                l = a[i][tmp_j]
                for j in range(len(a[0])):
                    a[i][j] = a[i][j] - a[tmp_i][j] * l
                print(f"{i + 1}行目 - {tmp_i + 1}行目 × {l}")
        output(a)
        k = k + 1
        print("row=",k)
    return a

def output(a):
    for i in a: print([str(x) for x in i])
        


print("計算結果:")
output(simplify(A))