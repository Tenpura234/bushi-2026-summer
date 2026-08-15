import re
from decimal import Decimal
from fractions import Fraction

menu_words={"0": "加算 A + B",
            "1": "減算 A - B",
            "2": "乗算 A * B",
            "3": "スカラー乗算 A * n",
            "4": "行列式",
            "5": "簡略化",
            "6": "逆行列",
            "7": "余因子行列"}

print("---行列計算メニュー---")
for i in menu_words:
    print(i, menu_words[i])
print("-------------------")

menu=input("\n計算方式を番号で入力:")

while not menu in menu_words:
    print("メニューにねーよボケ")
    menu = input("\n計算方式を番号で入力:")
print("\n"+menu_words[str(menu)]+"を選択")


def output(a):
    b = [[0 for j in range(len(a[0]))] for i in range(len(a))]
    for j in range(len(a[0])):
        for i in range(len(a)):
            b[i][j] = str(a[i][j])
    print(" ", *b, sep="\n")

def tableinput(a):
    name = a
    row = 0
    row_count =0
    i = 0
    j = 0
    pre = []
    print(f"行列 {name} を入力\n入力例:1 1.2 2/3 351\nendと入力して行入力終了")

    while row != "end":
        row = input(str(i+1)+ "行目:")
        if row == "end":
            break
        pre.insert(i, row)
        row_count = len(pre[0].split())

        if re.search(r"[^\d./ -]", row) and row != "end":
            print("数字と-./以外入れるなボケ")
            del pre[i]
            continue

        elif row_count != len(pre[int(i)].split()):
            print("列数がちげーよボケ")
            del pre[i]
            continue

        print(*pre, sep="\n")
        i = i + 1

    a = [[Fraction(x) for x in s.split()] for s in pre]

    print(f"\n行列{name}の入力終了")
    print(*a, sep="\n")
    return a


A = tableinput("A")
if 0 <= int(menu) <= 2:
    B = tableinput("B")
elif int(menu) == 3:
    while True:
        n = input("倍数n:")
        if re.search(r"[^\d./ -]", n):
            print("数字と./-以外入れるなボケ")
            continue
        break
A = [[2,0,0],[0,2,0],[0,0,2]]

print("\n-----演算結果-----")

if 0<= int(menu) <=2:
    print("行列A",*[str(f) for f in A]," ", "行列B", *[str(f) for f in B], sep="\n"  )
elif int(menu) == 3:
    print("行列A",*[str(f) for f in A], " ", "倍数n",Fraction(n), sep="\n")
else:
    print("行列A", *A, sep="\n" )

print("\n" + menu_words[menu])

i = 0
j = 0
k = 0
out = 0
if int(menu) ==0 and len(A) == len(B) and len(A[0]) == len(B[0]):
    C= [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for j in range(len(A[i])):
        for i in range(len(B)):
            C[i][j] = A[i][j] + B[i][j]
    out = 1

elif int(menu) ==1 and len(A) == len(B) and len(A[0]) == len(B[0]):
    C= [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for j in range(len(C[i])):
        for i in range(len(C)):
            C[i][j] = A[i][j] - B[i][j]
    out = 1

elif (int(menu) ==0 or int(menu) ==1) and (len(A) != len(B) or len(A[0]) != len(B[0])):
    print("サイズ違って計算できねーよボケ")
    print("Aのサイズ:", len(A[0]), "*", len(A) )
    print("Bのサイズ:", len(B[0]), "*", len(B) )

elif int(menu) ==2 and len(A[0]) == len(B):
    C = [[0 for j in range(len(A))] for i in range(len(B[0]))]
    print("Aの列数:",len(A[0]),"\nBの行数:",len(B))
    print("Cの行数:",len(C),"\nCの列数:",len(C[0]))
    for j in range(len(C[0])):
        for i in range(len(C)):
            for k in range(len(A[0])):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    out = 1

elif int(menu) ==2 and len(A[0]) != len(B):
    print("Aの列数とBの行数違って計算できねーよボケ")
    print("Aの列数:",len(A[0]),"\nBの行数:",len(B))

elif int(menu) ==3:
    C = [[0 for j in range(len(A[0]))] for i in range(len(A))]
    for j in range(len(C[0])):
        for i in range(len(C)):
            C[i][j] =  A[i][j]* Fraction(n)
    out = 1

elif int(menu) ==4 and len(A[0]) == len(A):
    l = 1
    m = 1
    zero = False
    for k in range(len(A)):
        output(A)
        if A[k][k] == 0:
            l = k
            if A[len(A)-1][len(A)-1] == 0:
                print("行列Aの非正則を検知")
                m = 0
                break
            while A[l][k] == 0:
                l = l + 1
                if l == len(A) - 1 and A[l][k] == 0:
                    break
            if l == len(A) - 1 and A[l][k] == 0:
                zero = True
                print("行列Aの非正則を検知")
                m = 0
                break
            tmp = A[k]
            A[k] = A[l]
            A[l] = tmp
            m = -m
            print("倍数m:", m)
            print(f"{k + 1}行目", "↔", f"{l + 1}行目")
            output(A)

        if zero == True:
            break

        n = A[k][k]
        m = m * A[k][k]
        for j in range(len(A[0])):
            A[k][j] = Fraction((A[k][j]), n)
        print(f"{k+1}行目 / {n}")
        output(A)
        print("倍数m:", m)
        for i in range(k + 1, len(A)):
            if A[i][k] != 0:
                tmp = A[i][k]
                for j in range(len(A[0])):
                    A[i][j] = A[i][j] - A[k][j] * tmp
                print(f"{i+1}行目 - {k+1}行目 × {tmp}")
                output(A)
    print("行列式の値:",m)

elif int(menu) ==4 and len(A[0]) != len(A):
    print("正方行列でないので計算できねーよボケ")
    print(f"行数:{len(A)},列数:{len(A[0])}")



if out == 1:
    i = 0
    j = 0
    for j in range(len(C[0])):
        for i in range(len(C)):
            C[i][j] = str(C[i][j])
    print(*C, sep="\n")


