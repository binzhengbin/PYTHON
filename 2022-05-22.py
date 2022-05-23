### 第四章 解析数据记录

#  if/elif/else 语句
# if语句中验证是否相等(=〉或不同(!=或<>)，，大于另一个或相反 C< ，<=，>=，>)，包含另一个或不包含(in，not in) ，或者与另一个相同或不同(is，is not)。
# 还可以验证是否两个或更多个条件都一起或单独满足。这三个布尔操作符 and, not, or 能够把条件结合在一起:
seq = 'MGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQTPSKPASADGHRGPSAAFAPAAAE'
if 'GGG' in seq and 'RRR' in seq:
    print('GGG is at position:', seq.find('GGG'))
    print('RRR is at position:', seq.find('RRR'))
if 'WWW' in seq or 'AAA' in seq:
    print('Either WWW or AAA occur in the sequence')
if 'AAA' in seq and 'PPP' not in seq:
    print('AAA occurs in the sequence but not PPP')

for i in range(30):
    if i < 4:
        print('prime number:', i)
    elif i % 2 == 0:
        print('multiple of two:', i)
    elif i % 3 == 0:
        print('multiple of three:', i)
    elif i % 5 == 0:
        print('multiple of five:', i)
    else:
        print('prime number:', i)



