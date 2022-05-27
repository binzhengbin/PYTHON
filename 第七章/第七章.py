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
# zip()命令可以将两个或多个列表中的元素一个接一个的相结合。
c = [7, 8, 9]
for each in zip(a, b, c):
    print(each)
# 每个输入列表中的第一个元素配对在一起，然后是第二个元素，以此类推。
# zip()函数的参数必须是可迭代的（列表，元组和字符串）。
# 它返回的结果是一个包含数个元组的列表。
# zip(*table) 这个星号表示告诉zip函数使用嵌套列表中的所有列表作为参数。
# zip(*table) 可以将表旋转90度


# 插入和删除列
# 插入列
table = [['protein', 'ext1', 'ext2', 'ext3'],
         [0.16, 0.038, 0.044, 0.040],
         [0.33, 0.089, 0.095, 0.091],
         [0.66, 0.184, 0.191, 0.191],
         [1.00, 0.280, 0.292, 0.283],
         [1.32, 0.365, 0.367, 0.365],
         [1.66, 0.441, 0.443, 0.444]
         ]   # 还是这个列表
table = zip(*table)  # 先旋转90度
table2 = list(table)  # 使用list函数转化为列表
table2.append(['ext4', 0, 0, 0, 0, 0, 0])
table2.pop(2)  # 删除某列
print(table2)
table2 = zip(*table2)  # 转置回去
table3 = list(table2)
print(table3)

# zip函数将列表转变成了元组，而元组是不可变的，这意味着使用zip函数后不能在对单个单元格进行操作，需要将行再次转换为列表。
table3[1] = list(table3[1])
table3[1][2] = 1111
print(table3)

row = [0] * 6  # 创建一维0列表
print(row)
table0 = []
for i in range(6):   # 通过重复循环创建多行
    table0.append([0] * 6)
print(table0)

table4 = [[0] * 6 for i in range(6)]  # 列表推导式
print(table4)


# 用字典表示表格数据
table = [
    {'protein': 0.16, 'ext1': 0.038, 'ext2': 0.044, 'ext3': 0.040},
    {'protein': 0.33, 'ext1': 0.089, 'ext2': 0.095, 'ext3': 0.091},
    {'protein': 0.66, 'ext1': 0.184, 'ext2': 0.191, 'ext3': 0.191},
    {'protein': 1.00, 'ext1': 0.280, 'ext2': 0.292, 'ext3': 0.283},
    {'protein': 1.32, 'ext1': 0.365, 'ext2': 0.367, 'ext3': 0.365},
    {'protein': 1.66, 'ext1': 0.441, 'ext2': 0.443, 'ext3': 0.444}
]
cell = table[1]['ext2']
print(cell)

# 字典中嵌套字典
table = {
    'row1': {'protein': 0.16, 'ext1': 0.038, 'ext2': 0.044, 'ext3': 0.040},
    'row2': {'protein': 0.33, 'ext1': 0.089, 'ext2': 0.095, 'ext3': 0.091},
    'row3': {'protein': 0.66, 'ext1': 0.184, 'ext2': 0.191, 'ext3': 0.191},
    'row4': {'protein': 1.00, 'ext1': 0.280, 'ext2': 0.292, 'ext3': 0.283},
    'row5': {'protein': 1.32, 'ext1': 0.365, 'ext2': 0.367, 'ext3': 0.365},
    'row6': {'protein': 1.66, 'ext1': 0.441, 'ext2': 0.443, 'ext3': 0.444}
}
cell = table['row1']['ext2']
print(cell)
# 这样查找特定的单元格会更加快捷简单
######## 用来加速程序进行的搜索字典被称为'索引'。#######

# 7.3 如何转换表的表现形式
# 用于储存表的所有方法：嵌套列表、嵌套字典和二者混合
# 每种形式都有其优缺点，因此实际运用中可能需要将表的一种表现形式转化为另一种。
# 嵌套列表转换为嵌套字典
table = [
         ['protein', 'ext1', 'ext2', 'ext3'],
         [0.16, 0.038, 0.044, 0.040],
         [0.33, 0.089, 0.095, 0.091],
         [0.66, 0.184, 0.191, 0.191],
         [1.00, 0.280, 0.292, 0.283],
         [1.32, 0.365, 0.367, 0.365],
         [1.66, 0.441, 0.443, 0.444],
         [1.66, 0.441, 0.443, 0.444]
         ]
nested_dict = {}
n = 0
key = table[0]
for row in table[1:]:
    n = n + 1
    entry = {key[0]: row[0], key[1]: row[1], key[2]: row[2], key[3]: row[3]}
    nested_dict['row' + str(n)] = entry  # 左边是字典的键 右边是字典的值
print(nested_dict)

# 嵌套字典转换为嵌套列表
nested_list = []
for entry in nested_dict:
    key = nested_dict[entry]
    nested_list.append([key['protein'], key['ext1'], key['ext2'], key['ext3']])
print(nested_list)
# 认真看能看懂


