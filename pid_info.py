import pandas as pd
import numpy as np
import pprint
import re
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
tag_dir = os.path.join(root_dir, r"data\L3_PID list.xlsx")
tagslib = pd.ExcelFile(tag_dir)

# print tagslib.sheet_names

#df = tagslib.parse(u'L3 Analog Input', parse_cols=[1,2,3,4, 5, 6], skiprows=[0, 1])
#print df.head(n=5)

#print replacedash('HS-909-1601-101-Start')    
def replacedash(tagname):
    return tagname.replace("-", "_")

def getalltags(sheet_name):
    df = tagslib.parse(sheet_name, parse_cols = [0,1,2,3,4])
    return df[pd.notnull(df['Controller'])]



if __name__ == '__main__':
    print getalltags('Sheet1').head()