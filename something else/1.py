# -*- coding: utf-8 -*-
# https://blog.csdn.net/destiny_python/article/details/78663460

import pandas as pd

# input.csv是那个大文件，有很多很多行
df1 = pd.read_csv('/Users/zhengbin/Desktop/Relative/Unigenes.relative.s.csv', encoding='gbk')

# input1.csv是那个小文件，其中他们有一行或者若干行存储的特征参数相同
df2 = pd.read_csv('/Users/zhengbin/Desktop/metastat/same/species_sam.csv', encoding='gbk')

# 加encoding=‘gbk’是因为文件中存在中文，不加可能出现乱码
index = df1['species'].isin(df2['Name'])

outfile = df1[index]

outfile.to_csv('outfile.csv', index=False, encoding='gbk')