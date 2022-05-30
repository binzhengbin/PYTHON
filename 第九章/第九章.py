# 在序列和自然语言文本中找到规律模式。
# 正则表达式（regular expression）
import re
seq = 'VSVLTMFRYAGWLDRLYMLVGTQLAAIIHGVALPLMMLI'
pattern = re.compile('[ST]Q')
match = pattern.search(seq)
if match:
    print('%10s' % (seq[match.start() - 4: match.end() + 4]))
    print('%6s' % match.group())
else:
    print('no match')
# compile()可以编译字符串并把它转换为正则表达对象（RegexpObject）

motif = 'R.[ST][^P]'  # 将匹配精氨酸（R）在第一位置的子字符串，任何氨基酸在第二位置都可以[.]，丝氨酸或苏氨酸在第三位置【ST】。最后的位置上为除脯氨酸外的任何氨基酸[^P]
regexp = re.compile(motif)
print(regexp)
seq = 'RQSAMGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQRPSKP'
match = regexp.search(seq)  # search()扫描字符串并寻找表达式第一次匹配的位置
match.group()  # 返回匹配的子字符串
print(match.group())
match.span()  # 返回匹配结果的包含（起点、终点）位置的元组
match.start()  # 返回匹配结果的起始位置
match.end()  # 返回匹配结果的结束位置

all = regexp.findall(seq)  # findall()可返回包含所有匹配的一个子字符串列表
print(all)
iter = regexp.finditer(seq)  # finditer()可找到所有对应的正则表达式对象并返回迭代器形式。
print(iter)
for s in iter:
    print(s.end())
    print(s.start())
    print(s.span())
    print(s.group())

# 9.3.3 分组
# 有时候可能要将一个正则表达式分解为若干个子组，每个子组匹配我们感兴趣的不同的部分。
import re
seq = 'QSAMGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQRPSKP'
pattern1 = re.compile('R(.)[ST][^P]')
match1 = pattern1.search(seq)
print(match1.group())
print(match1.group(1))
pattern2 = re.compile('R(.{0,3})[ST][^P]')
match2 = pattern2.search(seq)
print(match2.group())
print(match2.group(1))
# 子组可以嵌套，为了得到对应号码，就要计算从左至右有多少个左圆括号。
p = re.compile('(a(b)c)d')
m = p.match('abcd')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(2, 1, 2))  # 也可以向group()方法传递多个参数，在这个情况下将返回包含各组的值对应的元组。
print(m.groups())  # groups()返回所有与子组相关的子字符串

# 另外，也可以向每个子组分配名称以便于选择性地检索其内容。
pattern = 'R(?P<w1>.{0,3})[ST](?P<w2>[^P])'
regexp = re.compile(pattern)
m1 = regexp.search(seq)
print(m1.group('w1'))
print(m1.group('w2'))

# 9.3.4修改字符串
# split(s) sub(r,s,[c]) subn(r,s,[c]) 三种方法
import re
separaator = re.compile('\|')  # 字符｜是正则表达式的元字符，在元字符前面放一个反斜杠（'\'），可以让python解析它为一个正常的字符。
annotation = 'ATOM:CA|RES:ALA|CHAIN:B|NUMRES:166'
columns = separaator.split(annotation)
print(columns)
