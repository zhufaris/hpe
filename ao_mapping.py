import test
import sys

reload(test)

header = '''
FUNCTION "FC_AO_MAPPING" : VOID
TITLE =
VERSION : 0.1


VAR_TEMP
  temp : WORD ;	
END_VAR
BEGIN'''

footer = '''END_FUNCTION'''

template = '''
NETWORK
TITLE =

      A     "OFF"; 
      =     L      2.0; 
      BLD   103; 
      CALL "TYP_AO_SCALE" (
           IN                       := "DB_ANALOG_OUT".{2}.OUT_VALUE_IO,
           HI_LIM                   := 1.000000e+002,
           LO_LIM                   := 0.000000e+000,
           BIPOLAR                  := L      2.0,
           RET_VAL                  := #temp,
           OUT                      := {1});'''


def main():
    sheet_name = sys.argv[1] 
    df1= test.getalltags(sheet_name)
    print header
    for index, row in df1.iterrows():
        print template.format(row['Addr'], test.splitaddress(row['Addr']) ,test.replacedash(row['TagName']))
    print footer

if __name__ == '__main__':
    main();



