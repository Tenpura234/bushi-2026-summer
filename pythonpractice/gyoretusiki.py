l = 1
m = 1
zero = False
for k in range(len(A)):
    output(A)
    if A[k][k] == 0:
        l = k
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