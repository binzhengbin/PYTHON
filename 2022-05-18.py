#### 第一部分  ####

import math  # this is an import operation
import random

ATP = -30.5
print(math.log(199))
print(ATP + 2)
x1, y1, z1 = 0.1, 0.0, -0.7
x2, y2, z2 = 0.5, -1.0, 2.7
dx = x1 - x2
dy = y1 - y2
dz = z1 - z2
dsquare = math.pow(dx, 2) + pow(dy, 2) + pow(dz, 2)
d = math.sqrt(dsquare)
print(d)

print('protein'[0])
# 中括号为索引，可以提取字符串的某些位置，默认第一个字符为位置0，-1为最后一个位置。
print('protein'[-1])
# 中括号中添加冒号，可以提取部分字符串
print('protein'[0:3])
print('protein'[0:])

print(len('protein'))
# len()确定字符串长度
print('protein'.count("r"))
# *.count() 为计数


# for循环 #
# for <index variable> in <sequence>:
#   <command1>
#   <command2>
#   ...
#   <command*>

# index variable 是变量名，在遍历sequence时提取元素的值。
# 特别重要的是for循环开头有一个冒号（：）。

for character in 'hemoglobin':
    print(character)

insulin = 'GlVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT'  # 先定义一下胰岛素insulin
for amino_acid in 'ACDEFGHIKLMNPQSTVWY':
    number = insulin.count(amino_acid)
    print(amino_acid, number)

for i in [1, 2, 3, 4, 5, 6]:
    print(i)

for number in range(10):
    print(number)

# 缩进用来标记某些代码块需要被一起执行。
# 代码块由冒号发起，后面紧跟缩进的该代码块的指令。
# 代码块的缩进长度至少为4个空格。


alphabet = 'AGCT'
sequence = ''
for i in range(10):
    index = random.randint(0, 3)
    sequence = sequence + alphabet[index]
    print(sequence)

seq = "PRQTEINSEQWENCE"
for i in range(len(seq) - 4):
    print(seq[i:i + 5])

# 自测题2.3
for i in range(len(insulin)):
    print(insulin[0:i])


###
### 第二部分 ###
###

# 字符串、列表和元组是对象的有序集合，字典和集合是对象的无序集合。

data = []
for line in open('neuron_data.txt'):
    length = float(line.strip())
    data.append(length)
n_items = len(data)
total = sum(data)
shortest = min(data)
longest = max(data)
data.sort()

output = open("result.txt","w")
output.write("number of dendritic lengths : %4i \n"%(n_items))
output.write("total dendritic length      : %6.1f \n"%(total))
output.write("shortest dendritic length   : %7.2f \n"%(shortest))
output.write("longest dendritic length    :%7.2f \n"%(longest))
output.close()
# 结果在result.txt文件内。

