phylum = open("/Users/zhengbin/Desktop/MetaStats/phylum/phylum_qsig_detail.csv", 'r')
out_file = open("/Users/zhengbin/Desktop/metastat/same/phylum_sam.csv", 'w')
for line in phylum:
    columns = line.strip().split(',')
    one = columns[1].count('-')
    two = columns[2].count('-')
    if one == 0 and two == 0 :
        out_file.write(line)
phylum.close()
out_file.close()