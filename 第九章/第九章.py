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
