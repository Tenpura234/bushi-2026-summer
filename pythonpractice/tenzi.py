import re
from decimal import Decimal
from fractions import Fraction

class Input_matrix:

    def tableinput(self,a):
        name = a
        row = 0
        i = 0
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


class Tablecalculate:
    def __init__(self):
        self.A = [[0]]
        self.B = [[0]]
        self.C = [[0]]
        self.n = 0
        
    def simplify(self,a):
        process_row = 0
        stop = False

        gyoretsushiki = False
        m = 1

        while process_row < len(a):
            i = process_row
            j= 0
        #Step1
            while a[i][j] == 0:
                if i == len(a)-1 and a[i][j] == 0:
                    i = process_row
                    j = j + 1
                    if j > len(a[0]) - 1:
                        stop = True
                        break
                    continue
                if stop == True:
                    break
                i = i + 1
            if j > len(a[0])-1:
                break
            print(f"a{i+1,j+1}に注目")
            tmp_i = i
            tmp_j = j
        #Step2
            k = process_row
            while a[k][tmp_j] == 0:
                k = k + 1
            if process_row+1 != tmp_i+1:
                for j in range(len(a[0])):
                    tmp = a[process_row][j]
                    a[process_row][j] = a[tmp_i][j]
                    a[tmp_i][j] = tmp
                print(f"{process_row+1}行目 ⇔ {tmp_i+1}行目")
                if gyoretsushiki == True:
                    m = -m
                    print(f"倍数m:{m}")
                tmp_i = process_row
                self.output(a)
        #Step3
            if a[tmp_i][tmp_j] != 1:
                k = a[tmp_i][tmp_j]
                print(f"{tmp_i + 1}行目/ {k}")
                if gyoretsushiki == True:
                    m = m * k
                    print(f"倍数m:{m}")
                for j in range(len(a[0])):
                    a[tmp_i][j] = Fraction(a[tmp_i][j] ,k)

            self.output(a)
        #Step4
            for i in range(process_row if gyoretsushiki == True else 0, len(a)):
                if a[i][tmp_j] != 0 and i != tmp_i:
                    k = a[i][tmp_j]
                    for j in range(len(a[0])):
                        a[i][j] = a[i][j] - a[tmp_i][j] * k
                    print(f"{i + 1}行目 - {tmp_i + 1}行目 × {k}")

            self.output(a)
            process_row = process_row + 1
            print("row=",process_row)
            if gyoretsushiki == True:
                print(f"倍数m:{m}")
        return a

    def output(self,a):
        b = [[0 for j in range(len(a[0]))] for i in range(len(a))]
        for j in range(len(a[0])):
            for i in range(len(a)):
                b[i][j] = str(a[i][j])
        print(" ", *b, sep="\n")
        

InputMatrix = Input_matrix()

A = InputMatrix.tableinput("A")
TableCalculate = Tablecalculate()
result = TableCalculate.simplify(A)
print("計算結果:")
TableCalculate.output(result)