### 第五章

codon_table = {
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGU':'R', 'CGC':'R',
    'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'UCU':'S', 'UCC':'S',
    'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 'AUU':'I', 'AUC':'I',
    'AUA':'I', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L',
    'CUG':'L', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'GUU':'V',
    'GUC':'V', 'GUA':'V', 'GUG':'V', 'ACU':'T', 'ACC':'T', 'ACA':'T',
    'ACG':'T', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'AAU':'N',
    'AAC':'N', 'GAU':'D', 'GAC':'D', 'UGU':'C', 'UGC':'C', 'CAA':'Q',
    'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAU':'H', 'CAC':'H', 'AAA':'K',
    'AAG':'K', 'UUU':'F', 'UUC':'F', 'UAU':'Y', 'UAC':'Y', 'AUG':'M',
    'UGG':'W',
    'UAG':'STOP', 'UGA':'STOP', 'UAA':'STOP'
    }

# read the RNA sequence into a single string
rna = ''
for line in open('A06662-RNA.fasta'):
    if not line.startswith('>'):
        rna = rna + line.strip()

# translate one frame at a time
for frame in range(3):
    prot = ''
    print('Reading frame ' + str(frame + 1))
    for i in range(frame, len(rna), 3):
        codon = rna[i:i + 3]
        if codon in codon_table:
            if codon_table[codon] == 'STOP':
                prot = prot + '*'
            else:
                prot = prot + codon_table[codon]
        else:
            # handle too short codons
            prot = prot + '-'

    # format to blocks of 48 columns
    i = 0
    while i < len(prot):
        print(prot[i:i + 48])
        i = i + 48


#  字典
# 真（TRUE）假（FALSE）布尔值
n = 0
while n < 4:
    n = n + 1
    print(n)

# 字典为'键（key）：值（value）'对的对象的无序集合，用花括号括起来：{'GCU':'A', 'GCC':'A'}
# 更特别的是，字典是不可变对象（键）映射任意对象（值）的结构。不可变对象可以是数字、字符串和元组。这意味着，，列表和字典本身不能用作字典键，但可以用作值。
print(codon_table['GCU'])  # 字典可用于快速搜信息。

codon_table2 = {'GCU': 'A'}
print(codon_table2)
codon_table2['CGA'] = 'R'
print(codon_table2)

print(codon_table2['CGA'])

del codon_table2['CGA']  # 删除 del
print(codon_table2)

if 'GCU' in codon_table2:
    print(1)
else:
    print(0)

print(len(codon_table2))  # 计算字典所含有元素的数量


### while 语句
# 为了生成更易阅读的结果，蛋白质序列按每行 48 个符号的块来进行输出
# i = 0
# while i < len(prot):
#    print(prot[i:i + 48])
#    i = i + 48
# while 语句会重复执行语句块直到一些条件得道满足。while循环实际上是for和if语句的组合。

# while <condition>:
#       <statements>
# while 1: # 1 对应的条件是TRUE， 0是FALSE
#     print('while loop still running')

swissprot = open('SwissProt.fasta')
insulin_ac = 'P61981'
result = None
while result is None:
    line = swissprot.__next__()
    if line.startswith('>'):
        ac = line.split('|')[1]
        if ac == insulin_ac:
            result = line.strip()
            print(result)

# 如果while语句找不到胰岛素登记码，程序除非插入一个break语句，否则就要在文件到达末尾是通过StopIteration报错结束。
# break语句
# 当解释器遇到 break 语句时会退出循环，不再执行循环语句的其余部分，包括 else语句(如果存在），直接进到循环后面的第一条语句
# continue语句
# continue语句跳过循环语句的其余部分，跳至下 次循环


# 列表搜索
bases = ['A', 'C', 'T', 'G']
seq = 'CAGGCCATTRKGL'
for i in seq:
    if i not in bases:
        print(i, 'is not a nucleotide')


# 2022-05-23

#
sequences = {}
ac = ''
seq = ''
for line in open('SwissProt.fasta'):
    if line.startswith('>') and seq != ' ':
        sequences[ac] = seq  # 在字典sequences中，把值（变量seq的内容）分配给键（变量ac的内容）
        seq = ''  # seq初始化为空字符串
    if line.startswith('>'):
        ac = line.split('|')[1]
    else:
        seq = seq + line.strip()
sequences[ac] = seq
print(sequences.keys())
print(sequences['P30443'])

# 预测蛋白质序列中的无序（环）区域。
# 该预测程序的思想是每个氨基酸都有一个特定的二级结构元件倾向，可以通
# 过大量己知蛋白质结构 （PDB）级结构元件中各类氨基酸类型出现的频率f，估计氨基
# 酸的倾向。氨基酸"无序"(即成环)的倾向可用 1-f 计算。阈值为0.3
# 无序（成环）残基（倾向值>=0.3）为大写，"有序"残基(即倾
# 向于出现在 级结构元素中〉为小写。
propensities = {
   'N': 0.2299, 'P': 0.5523, 'Q':-0.18770, 'A':-0.2615,
   'R':-0.1766, 'S': 0.1429, 'C':-0.01515, 'T': 0.0089,
   'D': 0.2276, 'E':-0.2047, 'V':-0.38620, 'F':-0.2256,
   'W':-0.2434, 'G': 0.4332, 'H':-0.00120, 'Y':-0.2075,
   'I':-0.4222, 'K':-0.1001, 'L': 0.33793, 'M':-0.2259
   }
threshold = 0.3
input_seq = "IVGGYTCGANTVPYQVSLNSGYHFCGGSLINSQWVVSAAHCYKSG\
IQVRLGEDNINVVEGNEQFISASKSIVHPSYNSNTLNNDIMLIKLKSAASLNSR\
VASISLPTSCASAGTQCLISGWGNTKSSGTSYPDVLKCLKAPILSDSSCKSAYP\
GQITSNMFCAGYLEGGKDSCQGDSGGPVVCSGKLQGIVSWGSGCAQKNKPGVYT\
KVCNYVSWIKQTIASN"
output_seq = ''
for res in input_seq:
    if res in propensities:
        if propensities[res] >= threshold:
            output_seq += res.upper()
        else:
            output_seq += res.lower()
    else:
        print('unrecognized character:', res)
        break
print(output_seq)

# 如何从 PDB 文件中提取氨基酸序列
aa_codes = {
     'ALA':'A', 'CYS':'C', 'ASP':'D', 'GLU':'E',
     'PHE':'F', 'GLY':'G', 'HIS':'H', 'LYS':'K',
     'ILE':'I', 'LEU':'L', 'MET':'M', 'ASN':'N',
     'PRO':'P', 'GLN':'Q', 'ARG':'R', 'SER':'S',
     'THR':'T', 'VAL':'V', 'TYR':'Y', 'TRP':'W'}
seq = ''
for line in open('1TLD.pdb'):
    if line[0:6] == 'SEQRES':
        columns = line.split()
        for resname in columns[4:]:
            seq = seq + aa_codes[resname]
i = 0
print('>1TLd')
while i < len(seq):  # 输出结果为每行64个
    print(seq[i:i + 64])
    i = i + 64
# 结果如下
# >1TLd
# IVGGYTCGANTVPYQVSLNSGYHFCGGSLINSQWVVSAAHCYKSGIQVRLGEDNINVVEGNEQF
# ISASKSIVHPSYNSNTLNNDIMLIKLKSAASLNSRVASISLPTSCASAGTQCLISGWGNTKSSG
# TSYPDVLKCLKAPILSDSSCKSAYPGQITSNMFCAGYLEGGKDSCQGDSGGPVVCSGKLQGIVS
# WGSGCAQKNKPGVYTKVCNYVSWIKQTIASN

#  例题5.1
dir = {}
dir['UAA'] = 'Stop'
dir['UAG'] = 'Stop'
dir['UGA'] = 'Stop'
dir['AUG'] = 'Start'
dir['GGG'] = 'Glycin'
print(dir)


# 自测题 5.4
pref_H = {'A':'1.45', 'C':'0.77', 'D':'0.98', 'E':'1.53', 'F':'1.12', 'G':'0.53', 'H':'1.24', 'I':'1.00', 'K':'1.07',
          'L':'1.34', 'M':'1.20', 'N':'0.73', 'P':'0.59', 'Q':'1.17', 'R':'0.79', 'S':'0.79', 'T':'0.82', 'V':'1.14',
          'W':'1.14', 'Y':'0.61'}
pref_E = {'A':'0.97', 'C':'1.30', 'D':'0.80', 'E':'0.26', 'F':'1.28', 'G':'0.81', 'H':'0.71', 'I':'1.60', 'K':'0.74',
          'L':'1.22', 'M':'1.67', 'N':'0.65', 'P':'0.62', 'Q':'1.23', 'R':'0.90', 'S':'0.72', 'T':'1.20', 'V':'1.65',
          'W':'1.19', 'Y':'1.29'}
seq = ''
output = ''
threshold2 = 1.00
for line in open('SwissProt.fasta'):
    if not line.startswith('>'):
        seq = seq + line.strip()
i = 0
while i < len(seq):  # 输出结果为每行64个
    print(seq[i:i + 64])
    i = i + 64
for H in seq:
    if H in pref_H and pref_E:
        if float(pref_H[H]) >= threshold2 and float(pref_H[H]) > float(pref_E[H]):
            output += 'H'
        if float(pref_E[H]) >= threshold2 and float(pref_H[H]) < float(pref_E[H]):
            output += 'E'
        else:
            output += 'L'
i = 0
while i < len(output):  # 输出结果为每行64个
    print(output[i:i + 64])
    i = i + 64


### 第6章






