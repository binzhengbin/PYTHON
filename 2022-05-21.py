import math

f = open('count.txt', 'w')
f.write('this is just a dummy test')
f.close()
g = open('count.txt')
g.read()

# 字符串转换成浮点数
number = float('100.132') + 100.0
print(number)
number2 = '100.132' + '100.0'
print(number2)

# 浮点数转换成整数
number3 = int(100.2121)
print(number3)
f_number3 = float(number3)

# 将数字转换成文本
text = str(number3)
print(text)

# str() 的替代方法之一是使用字符串格式化，可以在数值转换成字符串时使用百分号指示要分配给整数的位数
print('Result :%3i' % 17)  # %3i表示字符串应该包含格式化为三位的整数，整数的实际值在结尾的括号里面。

# 以同样的方式可以插入浮点数字符串%x.yf，其中x是总字符数（也包括小数点），y是小数位数。
print('%8.3f' % 12.3456)  # 结果为四舍五入的结果

# 也可以用%s来格式化字符串,这个s代表的是字符串string的意思
# 还有其它的%d 整数型 和%f 浮点型以及%i 整数型等等
name = 'E.coli'
print('Hello, %s' % name)
print('Hello,', format('E.coli'))
#### 没搞懂格式化是什么意思

print('test:%20s numbers:%4i%4i%5.2f' % ('right-justified', 1, 2, 3))


## 将数据列写入文本文件
data = [16.38, 139.90, 441.46, 29.03, 40.93, 202.07, 142.30, 346.00, 300.00]
out = []
for value in data:
    out.append(str(value) + '\n')  # 将转换为字符串的值写入out列表中，然后添加换行符（'\n'）
open('result.txt', 'w').writelines(out)  # 打开一个文件，并使用writelines()函数将字符串列表写入该文件。

# 如果倾向于将结果格式化为长的单个字符串，那么循环的表达会稍有不同:
out = []
for value in data:
    out.append(str(value))
out = '\n'.join(out)  # '\n'.join()函数将所有值用换行符连接成一个字符串，以便write()使用。
open('5.21.txt', 'w').write(out)
print(out)
# 可以使用join()方法将任何数量的字符串连在一起，用一个链接字符串连接它们。
L = ['1', '2', '3', '4']
print('+'.join(L))

### 计算数值列表
print(data)
print(len(data))
print(max(data))
print(min(data))
print(sum(data))
print(sum(data)/len(data))
print(float(sum(data)/len(data)))

# 计算标准差
# import math
d = [3.53, 3.47, 3.51, 3.72, 3.43]
average = sum(d)/len(d)
total = 0.0
for value in d:
    total += (value - average) ** 2  # += 在python中表示1、两个值相加，返回值给符号左侧的变量；2、用于字符串连接，变量值带引号，数据类型为字符串。
std = math.sqrt(total / len(d))
print(std)

# 计算中位数
dd = [3.53, 3.47, 3.51, 3.72, 3.43]
dd.sort()  # 升序排序
mid = len(dd)/2
if len(dd) % 2 == 0:
    median = (dd[int(mid-1)]+dd[int(mid)])/2.0
else:
    median = dd[int(mid)]
print(median)
print(mid)

# 自测题3.3
alphabet = 'AGCT'
for sth in open('nucl.txt'):
    zb = sth.strip()
for z in alphabet:
    number = zb.count(z)
    print(z, number)

# 自测题3.4 计算GC含量
for sth in open('nucl.txt'):
    zb = sth.strip()
    nG = zb.count('G')
    nC = zb.count('C')
    total = len(zb)
print((nG+nC)/total)












