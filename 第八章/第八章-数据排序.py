# 8.2.2
from operator import itemgetter
table = []
for line in open('random_distribution.tsv'):
    columns = line.split()
    columns = [float(x) for x in columns]
    table.append(columns)
column = 1 # 按照第二列进行排序
table_sorted = sorted(table, key = itemgetter(column))
for row in table_sorted:
    row = [str(x) for x in row]
    print('\t'.join(row))

# 在python中有两种排列方法：
# 对列表进行排序的sort()方法和对任何可迭代数据排序的内置函数sorted()
# sort()默认是按照升序进行排序
data = [1, 5, 7, 8, 9, 2, 3, 6, 6, 10]
new_data = data.sort()
print(data)
# 因为sort()函数是就地修改列表，所以不会产生新列表，这也是为什么print(new_data)会返回一个None。
# 如果想要按照降序排序，可以先按照升序然后再把列表倒过来
data.reverse()
print(data)

# 比较函数cmp(a，b)对两个参数a和b进行比较，并根据结果返回一个整数。
# 如果a<b则返回负值；如果a=b则返回0；如果a>b则返回正值。
# sort()函数其实隐式的使用了cmp()函数来确定元素大小。
import functools  # python3中启用了cmp函数（compare）
def my_cmp(a, b):
    if a > b:
        return -1
    if a == b:
        return 0
    if a < b:
        return 1
L = [1, 2, 3, 4, 5, 6, 8, 8, 9, 9, 30]
L_sort = sorted(L, key = functools.cmp_to_key(my_cmp))
print(L_sort)

# 如果按第一列对表格进行排序，接着依次按照第二列、第三列进行排序，则可以读取表格将其放入列表的列表中，然后利用sort函数和自定义函数对其排序。
x = 0
def my_cmp(a, b):  # 这是定义的新函数
    if a[x] < b[x]:
        return 1
    if a[x] == b[x]:
        if a[x + 1] < b[x + 1]:
            return 1
        if a[x + 1] == b[x + 1]:
            if a[x + 2] < b[x + 2]:
                return 1
            if a[x + 2] == b[x + 2]:
                return 0
            if a[x + 2] < b[x + 2]:
                return -1
        if a[x + 1] < b[x + 1]:
            return -1
    if a[x] < b[x]:
        return -1

# 8.3.2内置函数sorted()
# sort()函数只适用于列表，而soretd()函数可以对列表、元组、字典等多种数据进行排序。
L = [1, 2, 3, 7, 5, 6, 4, 8, 9, 100, 30]
newdata = sorted(L)
print(newdata)

# 8.3.3 使用itemgetter排序
# 内置函数sorted()可以通过自定义函数（如表中给定列的值）进行排序，使用operator模块中的itemgetter函数可以达到该目标。
from operator import itemgetter
data = ['ACCTGGCCA', 'ACTG', 'TACGGCAGGAGACG', 'TTGGATC']
a = itemgetter(1)(data)
print(a)
b = itemgetter(1, -1)(data)
print(b)
# itemgetter(i)(T) 返回Td的第i个元素，T可以是字符串、列表、元组或字典。
# 如果想先按第二列，然后再按其它列（比如第四列）对table进行排序
new_table = sorted(table, key=itemgetter(1, 3))

# 8.3.4
# 按照降序排序时，附加参数reverse = True可以传递至sorted()函数中
new_data2 = sorted(data, reverse=True)
print(new_data2)

# 8.3.5 数据结构排序
# 对字典进行排序时，可以将所有键提取出来到列表中，对元组进行排序
data = {1: 'a', 2: 'b',  4: 'd', 3: 'c', 5: 't', 6: 'm', 36: 'z'}
keys = list(data)
print(keys)
keys.sort()
for key in keys:
    print(key, data[key])

# 使用内置函数sorted()对字典排序
for key in sorted(data):
    print(key, data[key])

# 对传递至列表的元组进行排序
# 元组是不可变的，因此自身不能排序。
data = (1, 4, 5, 3, 8, 9, 2, 6, 8, 9, 40)
list_data = list(data)
list_data.sort()
new_tup = tuple(list_data)
print(new_tup)

# 使用内置函数sorted()对元组排序
# sorted(iterable, key=None, reverse=False)
# iterable 是指可迭代对象
# key 主要是用来比较的元素，只有一个参数，具体的函数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse 是指排序规则，False代表升序（默认），反之则为降序。
data = (1, 4, 5, 3, 8, 9, 2, 6, 8, 9, 40)
new_tup = tuple(sorted(data))
print(new_tup)

# 8.3.6 按长度对字符串排序
# lambda函数又称为匿名函数，定义函数
data = ['ACCTGGCCA', 'ACTG', 'TACGGCAGGAGACG', 'TTGGATC']
bylength = sorted(data, key=lambda x: len(x))  # 通过lambda定义，变量x取列表元素值data的值。
print(bylength)













