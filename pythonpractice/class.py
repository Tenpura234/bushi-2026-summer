import re
from decimal import Decimal
from fractions import Fraction


class Select_menu:
    def __init__(self):
        self.menu_words={
            "0": "加算 A + B",
            "1": "減算 A - B",
            "2": "乗算 A * B",
            "3": "スカラー乗算 A * n",
            "4": "行列式",
            "5": "簡略化",
            "6": "逆行列",
            "7": "余因子行列"}
    
    def display_menu(self):
        print("---行列計算メニュー---")
        for i in self.menu_words:
            print(i, self.menu_words[i])
        print("---------------------")

    def menu_input(self):
        menu = input("\n計算方式を番号で入力:")
        while not menu in self.menu_words:
            print("メニューにねーよボケ")
            menu = input("\n計算方式を番号で入力:")
        print("\n"+self.menu_words[str(menu)]+"を選択")
        self.menu = menu

class Input_matrix:
    def __init__(self):
        self.A = [[0]]
        self.B = [[0]]
        self.C = [[0]]
        self.n = 0


    def tableinput(self,a):
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

    def numberinput(self,n):
        while True:
            n = input("倍数n:")
            if re.search(r"[^\d./ -]", n):
                print("数字と./-以外入れるなボケ")
                continue
            break
        return n


class Tablecalculate:
    def __init__(self):
        self.A = [[0]]
        self.B = [[0]]
        self.C = [[0]]
        self.n = 0
        

    def plus(self,a,b):
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            c= [[0 for j in range(len(b[0]))] for i in range(len(a))]
            for j in range(len(a[0])):
                for i in range((len(b[0]))):
                    c[i][j] = a[i][j] + b[i][j]
        return c

    def minus(self,a,b):
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            c = [[0 for j in range(len(b[0]))] for i in range(len(a))]
            for j in range(len(a[0])):
                for i in range((len(b[0]))):
                    c[i][j] = a[i][j] - b[i][j]
        return c

    def multi(self,a,b):
        if len(a[0]) == len(b):
            c = [[0 for j in range(len(a))] for i in range(len(a[0]))]
            for j in range(len(c[0])):
                 for i in range(len(c)):
                    for k in range(len(A[0])):
                        c[i][j] = c[i][j] + a[i][k] * b[k][j]
        return c

    def scalarmulti(self,a,n):
        c = [[0 for j in range(len(a[0]))] for i in range(len(a))]
        for j in range(len(c[0])):
            for i in range(len(c)):
                c[i][j] =  a[i][j]* Fraction(n)
        return c

    def determinant(self,a):
        if len(a[0]) == len(a):
            l = 1
            m = 1
            zero = False
            for k in range(len(a)):
                self.output(a)
                if a[k][k] == 0:
                    l = k
                    if a[len(a)-1][len(a)-1] == 0:
                        print("行列aの非正則を検知")
                        m = 0
                        break
                    while a[l][k] == 0:
                        l = l + 1
                        if l == len(a) - 1 and a[l][k] == 0:
                            break
                    if l == len(a) - 1 and a[l][k] == 0:
                        zero = True
                        print("行列aの非正則を検知")
                        m = 0
                        break
                    tmp = a[k]
                    a[k] = a[l]
                    a[l] = tmp
                    m = -m
                    print("倍数m:", m)
                    print(f"{k + 1}行目", "↔", f"{l + 1}行目")
                    self.output(a)

                if zero == True:
                    break

                n = a[k][k]
                m = m * a[k][k]
                for j in range(len(a[0])):
                    a[k][j] = Fraction((a[k][j]), n)
                print(f"{k+1}行目 / {n}")
                self.output(a)
                print("倍数m:", m)
                for i in range(k + 1, len(a)):
                    if a[i][k] != 0:
                        tmp = a[i][k]
                        for j in range(len(a[0])):
                            a[i][j] = a[i][j] - a[k][j] * tmp
                        print(f"{i+1}行目 - {k+1}行目 × {tmp}")
                        self.output(a)
        return m

    def simplify(self,a):
        i = 0
        j = 0
        k = 0
        process_row = 0
        stop = False

        gyoretsushiki = False
        #ifなんとか:
        #gyoretsushiki = True
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
        

    




menu_manager = Select_menu()
menu_manager.display_menu()
menu_manager.menu_input()
print(menu_manager.menu)

InputMatrix = Input_matrix()



if menu_manager.menu == "0":
    A = InputMatrix.tableinput("A")
    B = InputMatrix.tableinput("B")
    TableCalculate = Tablecalculate()
    result = TableCalculate.plus(A, B)
    print("計算結果:")
    print(*result, sep="\n")

if menu_manager.menu == "1":
    A = InputMatrix.tableinput("A")
    B = InputMatrix.tableinput("B")
    TableCalculate = Tablecalculate()
    result = TableCalculate.minus(A, B)
    print("計算結果:")
    print(*result, sep="\n")

if menu_manager.menu == "2":
    A = InputMatrix.tableinput("A")
    B = InputMatrix.tableinput("B")
    TableCalculate = Tablecalculate()
    result = TableCalculate.multi(A, B)
    print("計算結果:")
    print(*result, sep="\n")

if menu_manager.menu == "3":
    A = InputMatrix.tableinput("A")
    n = InputMatrix.numberinput("n")
    TableCalculate = Tablecalculate()
    result = TableCalculate.scalarmulti(A, n)
    print("計算結果:")
    print(*result, sep="\n")

if menu_manager.menu == "4":
    A = InputMatrix.tableinput("A")
    TableCalculate = Tablecalculate()
    result = TableCalculate.determinant(A)
    print("計算結果:")
    print(result)

if menu_manager.menu == "5":
    A = InputMatrix.tableinput("A")
    TableCalculate = Tablecalculate()
    result = TableCalculate.simplify(A)
    print("計算結果:")
    print(*result, sep="\n")