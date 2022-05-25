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


