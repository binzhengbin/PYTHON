# 管理表数据

table = [['protein', 'ext1', 'ext2', 'ext3'],
         [0.16, 0.038, 0.044, 0.040],
         [0.33, 0.089, 0.095, 0.091],
         [0.66, 0.184, 0.191, 0.191],
         [1.00, 0.280, 0.292, 0.283],
         [1.32, 0.365, 0.367, 0.365],
         [1.66, 0.441, 0.443, 0.444]
        ]  # 嵌套列表
table = table[1:]  # 删除标签行
protein, ext1, ext2, ext3 = zip(*table)  # 创建四个元组，每个包含一列数据。
extinction = ext1 + ext2 + ext3
protein = protein * 3
table = zip(protein, extinction)
for prot, ext in table:
    print(prot, ext)

# 二维表
# 任何表可以被编码成含有列表的列表，也称为嵌套列表。
# 嵌套列表中，有一个单一的外列表（包含内部的行）和内列表（一行一个），外列表包含内列表。
# 二维阵列
square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
square2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# 1  2  3
# 4  5  6
# 7  8  9

# 访问行和单元格
# 将表格表示为嵌套列表后，可以通过索引访问各行，以同样的方式也可以访问任何列。
second_row = square[1]  # 访问第二行
print(second_row)
second_row_third_column = square[1][2]  # 访问第二行的第三列的单元
print(second_row_third_column)
square[1][2] = 11  # 修改第二行的第三列的单元
print(square)
for row in square2:
    print(row)

for row in square:  # 利用for双循环，可以依次访问各行的每个单元格。
    for cell in row:
        print(cell)

#  插入和删除行
table = [['protein', 'ext1', 'ext2', 'ext3'],
         [0.16, 0.038, 0.044, 0.040],
         [0.33, 0.089, 0.095, 0.091],
         [0.66, 0.184, 0.191, 0.191],
         [1.00, 0.280, 0.292, 0.283],
         [1.32, 0.365, 0.367, 0.365],
         [1.66, 0.441, 0.443, 0.444]
         ]
print(table)
# 删除行
table = table[1:]
# table.pop(0)
# 插入行
table.insert(2, [0.55, 0.123, 0.122, 0.145])  # 在给定位置插入新行
print(table)
table.append([0.55, 0.123, 0.122, 0.145])  # 在末尾添加一个新行
print(table)

# 访问列
# 嵌套列表的缺点是访问列不那么简单直接
protein = []
for row in table:
    protein.append(row[0])
print(protein)  # 可以在表上运行一个循环来收集一列的所有数据

# 如果想要用这种方法提取多列或访问相同的列多次，程序将变得很长，难以阅读。
protein, ext1, ext2, ext3 = zip(*table)  # zip(*table) 命令把每一列转换为单个元组变量，从而有效地将表旋转90度。
print(protein, ext1, ext2, ext3)

# 合并多列
# 加号（+）和乘号（*）运算符在python中可以分别应用于列表和元组的合并和乘法。
# 乘法通过复制来扩展列表。
protein = protein * 3
print(protein)
print([1, 2, 3] * 3)  # 类似于这种
# 加法可以将两个或者多个列表或元组连接为一个。
print([1, 2, 3] + [4, 5, 6])
# 其结果是包含所有数据项的一个列表或元组
extinction = ext1 + ext2 + ext3
print(extinction)


# zip()函数 python3.*
a = [1, 2, 3]
b = [4, 5, 6]
for each in zip(a, b):
    print(each)

