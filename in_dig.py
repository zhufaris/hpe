import test
import sys

reload(test)

def main():
    
    header = '''DATA_BLOCK "DB_DIGITAL_IN"
    TITLE =
    VERSION : 0.1

    STRUCT'''

    footer = '''
    END_STRUCT;	
    BEGIN

END_DATA_BLOCK'''

    values = "BOOL"
    sheet_name = sys.argv[1]

    print header
    test.printstring(sheet_name, values)
    print footer

if __name__ == '__main__':
    main()