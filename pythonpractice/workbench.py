a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print(a + b + c)

C = [[0 for j in range(10)] for i in range(2)]
print(C)

matrix = [[1,0,0],[0,1,0],[0,0,1],[0, 0 ,114514]]
print(len(matrix))  ##行数
print(len(matrix[0])) ## 列数

##　行、列の順番
C = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(C)

C = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
print(C)
