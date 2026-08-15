# 空の辞書を用意する
lists = {}

A = [[1,2,3],[9,8,7],[11,21,0]]
# |A| = 310
# ループなどで動的に名前（キー）を変えてリストを作る
i = 0

for i in range(len(A)):
    list_name = f"list_{i}"
    lists[list_name] = []  # 新しい空のリストを生成

# データの追加
i = 0
for i in range(len(A)):
    lists[f"list_{i}"].append(A[i])

for i in range(len(lists)):



print(lists)  # 出力: ['データA']