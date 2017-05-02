import pandas as pd
import numpy as np
import pprint
import re
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
tag_dir = os.path.join(root_dir, r"data\HPI BLOCKB_PLC Point to Point Check V2.xls")
tagslib = pd.ExcelFile(tag_dir)

# print tagslib.sheet_names

#df = tagslib.parse(u'L3 Analog Input', parse_cols=[1,2,3,4, 5, 6], skiprows=[0, 1])
#print df.head(n=5)

#pprint.pprint(getcolumns(df))
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
        raise ValueError('Address format wrong!')

def splitrange(rangevalue):
    if not rangevalue:
        raise ValueError('Range empty!')
    match = re.match(r"([0-9]+)[-~]+([0-9]+)", rangevalue, flags=0)
    if match:
        pass

if __name__ == "__main__":
    df = tagslib.parse(u'L3 Analog Input', parse_cols=[1,2,3,4, 5, 6], skiprows=[0, 1])
    print df.head()
    print df.columns
    df1 = getalltags('L3 Digital Input')
    for index, row in df1.iterrows():
        print splitaddress(row['Addr'])
    print root_dir