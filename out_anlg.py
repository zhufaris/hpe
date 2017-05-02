import test
import sys

reload(test)

def main():
    
    header = '''DATA_BLOCK "DB_ANALOG_OUT"
    TITLE =
    VERSION : 0.1

    STRUCT'''

    footer = '''
    END_STRUCT;	
    BEGIN

END_DATA_BLOCK'''

    values = '"UDT_CM_OutAnlg"'
    sheet_name = sys.argv[1]

    print header
    test.printstring(sheet_name, values)
    print footer

if __name__ == '__main__':
    main()