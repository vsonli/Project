# -*- coding:utf-8 -*-
# @Time   :2019/5/17 12:26
# @File   :test.py
# @Author :Vsonli
# 导入pandas包并重命名为pd
import pandas as pd

# Import retail sales data from an Excel Workbook into a data frame
# path = '/Documents/analysis/python/examples/2015sales.xlsx'
path = 'aa.xlsx'
xlsx = pd.ExcelFile(path)
df = pd.read_excel(xlsx, 'Sheet1')

# Let's add a new boolean column to our dataframe that will identify a duplicated order line item (False=Not a duplicate; True=Duplicate)
df['is_duplicated'] = df.duplicated(['test'])

# We can sum on a boolean column to get a count of duplicate order line items
# df['is_duplicated'].sum()

# Get the records of duplicated, If you need non-dup just use False instead
df_dup = df.loc[df['is_duplicated'] == True]

# Finally let's save our cleaned up data to a csv file
df_dup.to_csv('dup.csv', encoding='utf-8')
import xlrd


def open_excel(fileName="aa.xls"):
    try:
        fileHandler = xlrd.open_workbook(fileName)
        return fileHandler
    except Exception as e:
        print(str(e))



def scan_excel(sheet_name1=u''):
    handler = open_excel()
    page = handler.sheet_by_name('Sheet1')
    return page

def trim_cols(index=0):
    page = scan_excel()
    col1 = page.col_values(index)
    col2 = []
    for item in col1:
        if item not in col2:
            col2.append(item)
    print(col1)
    print(col2)
def main():
    trim_cols()


if __name__ == "__main__":
    main()