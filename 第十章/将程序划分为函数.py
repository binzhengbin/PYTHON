# 10.2.2
# Extract a FASTA sequence from a PDB file.
import struct
pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s10s2s3s'
amino_acids = {
    'ALA':'A', 'CYS':'C', 'ASP':'D', 'GLU':'E',
    'PHE':'F', 'GLY':'G', 'HIS':'H', 'LYS':'K',
    'ILE':'I', 'LEU':'L', 'MET':'M', 'ASN':'N',
    'PRO':'P', 'GLN':'Q', 'ARG':'R', 'SER':'S',
    'THR':'T', 'VAL':'V', 'TYR':'Y', 'TRP':'W'
     }
def threeletter2oneletter(residues):
    for i, threeletter in enumerate(residues):
        residues[i][0] = amino_acids[[threeletter[0]]]
# get_residues()
def get_residues(pdb_file):
    residues = []
    for line in pdb_file:
        if line[0:4] == 'ATOM':
            tmp = struct.unpack(pdb_format, line)
            ca = tmp[3].strip()
            if ca == 'CA':
                res_type = tmp[5].strip()
                chain = tmp[7]
                residues.append([res_type, chain])
    return residues
def write_fasta_records(residues, pdb_id, fasta_file):
    seq = ''
    chain = residues[0][1]
    for aa, new_chain in residues:
        if new_chain == chain:
            seq = seq + aa
        else:
            fasta_file.write(">%s_%s\n%s\n" % (pdb_id, chain, seq))  # 每个%s代表后面的括号里面同一顺序的那个。
            seq = aa
            chain = new_chain
    fasta_file.write(">%s_%s\n%s\n" % (pdb_id, chain, seq))
def extract_sequence(pdb_id):
    pdb_file = open(pdb_id + '.pdb')
    fasta_file = open(pdb_file + '.fasta', 'w')
    residues = get_residues(pdb_file)
    threeletter2oneletter(residues)
    write_fasta_records(residues, pdb_id, fasta_file)
    pdb_file.close()
    fasta_file.close()
    extract_sequence('3G5U')

# 内置函数enumerate(residues)会生成(n, residues[n])形式的元组
data = [['ALA', 'A'], ['CYS', 'A']]
for i, j in enumerate(data):
    print(i, j)

# 10.3.1 如何定义和调用函数
# def my_function(arg1, arg2): 函数名和函数的参数，在调用函数时，参数会被传递给该函数。
#     <instruction> 是指被调用是执行的指令，用于定义函数的功能。
#     return value1, value2 是指返回函数的结果
def addition(num1, num2):
    result = num1 + num2
    return result

# 专题10-3 带有range()和xrange()的循环
# 在for循环中，range(n, m)用于创建一列从n到m-1的整数，xrange(n,m)用于创建迭代器，如果这两个函数的n被忽略了也就是没写，那么0则就是n的默认值。
for i in range(5):
    print(i ** 2)
# range(i,j) = [i, i+1, i+2,…, j-1]
# range(k) = [0,1,2,…,k-1]
# range(i,j,l) = [i, i+l, i+2l, …, j-1]   (i<j)
# range(i,j,-l) = [i, i-l, i-2l, …, j+1]   (i>j)

# 专题10-6 lambda函数也叫匿名函数
g = lambda x: x**2
print(g(2))
# (lambda x: x**3)(3)
print((lambda x: x**3)(3))

# 在python中有四类参数：必选参数、关键字参数、默认参数和可变长参数

