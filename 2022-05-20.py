###
### 第二部分 ###
###

# 字符串、列表和元组是对象的有序集合，字典和集合是对象的无序集合。

data = []  # 创建一个空的（文件列表）。
for line in open('neuron_data.txt'):
    length = float(line.strip())  # strip()函数会删除一行开头或者结尾处的空字符（如果存在的话），包括该行末尾的换行符。
    data.append(length)  # length数据添加到data中。

n_items = len(data)
total = sum(data)
shortest = min(data)
longest = max(data)
data.sort()

output = open("result.txt", "w")  # 'w' 表示write 写入的意思，只能用于写入。
output.write("number of dendritic lengths : %4i \n"%(n_items))
output.write("total dendritic length      : %6.1f \n"%(total))
output.write("shortest dendritic length   : %7.2f \n"%(shortest))
output.write("longest dendritic length    :%7.2f \n"%(longest))
output.close()
# 结果在result.txt文件内。

output_file = open('count.txt', 'w')
output_file.write('number of neuron lengths : 7\n')  # \n 表示为换行符，因为write()不能自动换行。
output_file.close()

text_file = open('neuron_data.txt')  # 打开文件
lines = text_file.readlines()  # 从文件中读取长度数值 readlines()函数只是读取文件中的所有内容，按照分隔符逐行储存这些字符串，最后会返回一个字符串列表。
text_file.close()  # 关闭文本文件

# for line in open('filename'):  # 很多程序从文本文件读取数据时都包含与以下两行相似的命令。
#    line = line.strip()

f = open('count.txt', 'w')
f.write('this is just a dummy test')
f.close()
g = open('count.txt')
g.read()



