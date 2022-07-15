# -*- coding: UTF-8 -*-
import re
import sys
import os

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

str1 = []
str2 = []
str_dump = []
fa = open("/Users/zhengbin/Desktop/MetaStats/species/species_qsig.csv",'r')
fb = open("/Users/zhengbin/Desktop/metastat/same/species_sam.csv",'r')
fc = open("/Users/zhengbin/Desktop/metastat/diff/species_diff.csv",'w+')
# 将A.txt的内容逐行读到str1中
for line in fa.readlines():
    str1.append(line.replace("\n",''))
# 将B.txt中的内容逐行读到str2中
for line in fb.readlines():
    str2.append(line.replace("\n",''))

# 将两个文件中重复的行，添加到str_dump中
for i in str1:
    if i in str2:
        str_dump.append(i)

# 将两个文件的行合并，并去重
str_all=set(str1+str2)

# 将重复的行，在去重的合并行中，remove掉，剩下的就是不重复的行了
for i in str_dump:
    if i in str_all:
        str_all.remove(i)
# 写行文件中
for i in list(str_all):
    fc.write(i+'\n')

fa.close()
fb.close()
fc.close()
