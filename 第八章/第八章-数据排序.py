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

