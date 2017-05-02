import test
import sys

reload(test)

header = '''
FUNCTION "FC_DO_MAPPING" : VOID
TITLE =
VERSION : 0.1

BEGIN'''

footer = '''END_FUNCTION'''

template = '''
NETWORK
TITLE = 

      A     "DB_DIGITAL_OUT".{1};
      =     {0};'''


def main():
    sheet_name = sys.argv[1] 
    df1= test.getalltags(sheet_name)
    print header
    for index, row in df1.iterrows():
        print template.format(test.splitaddress(row['Addr']), test.replacedash(row['TagName']))
    print footer

if __name__ == '__main__':
    main();



