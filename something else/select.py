# 首先将表格中的0替换成-，然后将表格转换为csv格式。
gene = open("/Users/zhengbin/Desktop/gene4.csv", 'r')
out_file = open('/Users/zhengbin/Desktop/gene_filter2.csv', 'w')
for line in gene:
    columns = line.strip().split(',')
    controltype = columns[1:22].count('-')
    treatment = columns[23:44].count('-')
    if controltype <= 11 and treatment <= 11:
        out_file.write(line)
gene.close()
out_file.close()



