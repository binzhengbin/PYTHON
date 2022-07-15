species = open("/Users/zhengbin/Desktop/MetaStats/species/species_qsig.csv", 'r')
out_file = open("/Users/zhengbin/Desktop/metastat/same/species_sam.csv", 'w')
for line in species:
    columns = line.strip().split(',')
    one = columns[1].count('-')
    two = columns[2].count('-')
    if one == 0 and two == 0 :
        out_file.write(line)
species.close()
out_file.close()