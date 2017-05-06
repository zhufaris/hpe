import pandas as pd
import numpy as np
from pprint import pprint
import re
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
tag_dir = os.path.join(root_dir, r"data\HPI BLOCKB_PLC Point to Point Check V4.xls")
tagslib = pd.ExcelFile(tag_dir)

# print tagslib.sheet_names

#df = tagslib.parse(u'L3 Analog Input', parse_cols=[1,2,3,4, 5, 6], skiprows=[0, 1])
#print df.head(n=5)

#pprint(getcolumns(df))
def getcolumns(dataframe1):
    return dataframe1.columns.values.tolist()

#print replacedash('HS-909-1601-101-Start')
def replacedash(tagname):
    return tagname.replace("-", "_")

def getalltags(sheet_name):
    df = tagslib.parse(sheet_name, parse_cols = [1,2,3,4,5,6], skiprows=[0,1])
    df.columns = change_name(df.columns)
    df = df.loc[df['TagName'] != 'Spare']
    return df[pd.notnull(df['TagName'])]

def change_name(lst):
    lst1 = [u'RANGE' if 'RANGE' in x else x for x in lst]
    return [u'Addr' if 'PLC Addr' in x else x for x in lst1]

#print(getalltags(u'L9 Digital Output')[['TagName', 'DESCRIPTION']].to_csv(header=False))#.head(n=5)#.set_index('TagName').to_dict()

def printstring(sheet_name, values):
    df1 = getalltags(sheet_name)
    for index, row in df1.iterrows():
        print '\t{} : {}; // {}'.format(replacedash(row['TagName']), values, row['DESCRIPTION'])

def splitaddress(address):
    match = re.match(r"([a-zA-Z]+)([\d\.]+)", address, flags=0)
    if match:
        return match.group(1) + ' '*6 + match.group(2)
    else:
        raise ValueError('Invalid address format!')

def splitrange(rangevalue):
    if not pd.notnull(rangevalue):
        return '', ''
    match = re.match(r"([0-9]+)\s*[-~]\s*([0-9X]+)", rangevalue, flags = 0)
    if match:
        return match.group(1), match.group(2)
    else:
        raise ValueError('Invalid range format!')

def splitrange1(rangevalue):
    if not pd.notnull(rangevalue):
        return '', ''
    match = re.match(r'(\d+)\s*=\s*(\w+)', rangevalue, flags = 0)
    if match:
        return match.group(1), match.group(2)
    else:
        raise ValueError('Invalid range value!')

def splitrange2(rangevalue):
    if not pd.notnull(rangevalue):
        return '', ''
    match = re.match(r'()\s*,\s*()', rangevaule, flags = 0)
    if match:
        first = match.group(1)
        second = match.group(2)
        return splitrange1(first), splitrange1(second)
    else:
        raise ValueError('Invalid range value!')

def int_to_hex(number):
    return '{:03x}'.format(number)

def df_filter(df, column, text):
    text_uppercase = text.upper()
    return df[df[column].str.upper().str.contains(text_uppercase)]

if __name__ == "__main__":
    # df = tagslib.parse(u'L3 Analog Input', parse_cols=[1,2,3,4,5,6], skiprows=[0, 1])
    # print df.head()
    # print df.columns
    df1 = getalltags('L3 Analog Output')
    '''for index, row in df1.iterrows():
        print splitrange(row['RANGE'])
    print root_dir'''
    print df_filter(df1, 'DESCRIPTION', 'damper')
