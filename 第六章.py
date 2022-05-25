# 集合
# 集合是唯一对象的无序组合。这意味着它并不是列表之类的顺序的对象，不能包含相同的元素。
# 集合不支持索引和切片操作。
# 创建集合 set(x) x是一个类序列的对象，即字符串、元组或列表。
a = set('MGSNKSKPKDASQ')
print(a)
b = {1, 2, 3, 4}
print(b)

# 由于集合是唯一元素的组合，创建集合时多余的元素会被自动删除。
id_list = ['P04637', 'P02340', 'P10361', 'Q29537', 'P04637', 'P10361', 'P10361']
id_set = set(id_list)
print(id_set)
# 这是非常简洁的寻找唯一标识符的方式。

# 集合的方法
# 方法add()可用于将一个元素添加到集合中，如果该元素已经存在那么就不起作用。
# 方法update()用于将几个元素添加到集合中。
# pop() remove()和discard()可以将元素从集合中去除。
s1 = {1, 2, 3, 4, 5}
s1.add(10)
print(s1)
s1.update(['a', 'b', 'c'])
print(s1)
if 5 in s1:
    print(True)
s2 = {10, 4, 5}
print(s1.issubset(s2))  # 集合s1是否是s2的子集。
print(s1.issuperset(s2))  # 集合s1是否是s2的超集。也就是s2是不是s1的子集。

# 使用集合来确定数据重叠/差异
s3 = {'a', 'b', 'c'}
s4 = {'c', 'd', 'e'}
union = s3.union(s4)
print(union)  # 并集
intersection = s3.intersection(s4)
print(intersection)  # 交集
symmetric_difference = s3.symmetric_difference(s4)
print(symmetric_difference)  # 对称差，创建了一个包含只在s1或只在s2，即不同时存在于两者中的元素的新集合。
difference = s3.difference(s4)
print(difference)  # 两个集合的差，创建了一个包含s3不在s4中的元素的新集合。

# 例题6.1 找到所有集合中的共同元素。
a = {1, 2, 3, 4, 5}
b = {2, 4, 6, 7, 1}
c = {1, 4, 5, 9}
triple_set = [a, b, c]
from functools import reduce
common = reduce(set.intersection, triple_set)  # 注意reduce()函数被移到functools模块中了。
print(common)
# reduce() 包含两个因子，reduce(f, i):第一个是有两个变量的的函数f(x, y)，第二个是迭代对象i(元组或列表)。
# 首先将迭代对象i中的第一个元素和第二个元传递至函数f，得到结果后，将该结果作为参数与第3个迭代元素再次传递到函数f中得倒最终结果。
# 如果迭代对象i中的元素多余3个就以此类推，直到全部迭代元素i计算完毕。

# 定义一个乘法函数
def multiply(x, y):
    return x * y
print(reduce(multiply, (1, 2, 3, 4)))


