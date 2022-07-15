import csv
f = open('/Users/zhengbin/Desktop/metastat/same/species_sam_fengdu.csv', 'w', encoding = 'utf-8', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['Database ID', 'Name', 'Organism'])

with open('ID.csv','r',encoding='utf8') as fp1:
    # 使用列表推导式，将读取到的数据装进列表
    list1 = [i for i in csv.reader(fp1)]  # csv.reader 读取到的数据是list类型
    print(list1)
with open('name_or.csv','r',encoding='utf8') as fp2:
    list2 = [i for i in csv.reader(fp2)]
    print(list2)
for i in list1:
    for j in list2:
        if i[0] == j[0]:#匹配到ID，就将内容写入到seq_sim_all.csv中
            csv_writer.writerow([i[0], j[1], j[2]])
            print(i[0], j[0], j[1], j[2])


