import pandas as pd
def xlsx_to_csv_pd():
    data_xls = pd.read_excel('/Users/zhengbin/Desktop/MetaStats/phylum/phylum_qsiq.xls', index_col=0)
    data_xls.to_csv('/Users/zhengbin/Desktop/MetaStats/phylum/phylum_qsiq.csv', encoding='utf-8')
if __name__ == '__main__':
    xlsx_to_csv_pd()