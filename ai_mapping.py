import test
import sys

reload(test)

header = '''
FUNCTION "FC_AI_MAPPING" : VOID
TITLE =
VERSION : 0.1


VAR_TEMP
  PIW512_DI : DINT ;	
END_VAR
BEGIN'''

footer = '''END_FUNCTION'''

template = '''
NETWORK
TITLE =

      A(    ; 
      L     {1}; 
      L     0; 
      >=I   ; 
      )     ; 
      A(    ; 
      L     {1}; 

      L     27648; 
      <=I   ; 
      )     ; 
      JNB   _{3}; 
      CALL "TYP_AI_SCALE" (
           Low_Limit                := 0.000000e+000,
           High_Limit               := 1.000000e+002,
           Max_Raw                  := 2.764800e+004,
           Raw_In                   := {1},
           Scaled                   := "DB_ANALOG_IN".{2}.IN_VALUE_IO);
_{3}: NOP   0; 
NETWORK
TITLE =

      L     {1}; 
      L     0; 
      <=I   ; 
      =     "DB_ANALOG_IN".{2}.IN_VALUE_UNDERRANGE; 
NETWORK
TITLE =

      L     {1}; 
      L     27648; 
      >=I   ; 
      =     "DB_ANALOG_IN".{2}.IN_VALUE_OVERRANGE; 
NETWORK
TITLE =

      O(    ; 
      L     {1}; 
      L     30000; 
      >I    ; 
      )     ; 
      O(    ; 
      L     {1}; 
      L     -30000; 
      <I    ; 
      )     ; 
      =     "DB_ANALOG_IN".{2}.IO_FAULT;'''


def main():
    number = 1
    sheet_name = sys.argv[1] 
    df1= test.getalltags(sheet_name)
    print header
    for index, row in df1.iterrows():
        print template.format(row['Addr'], test.splitaddress(row['Addr']), test.replacedash(row['TagName']), test.int_to_hex(number))
        number = number + 1
    print footer

if __name__ == '__main__':
    main();



