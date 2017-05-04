import test
import sys
reload(test)

header = '''FUNCTION "FC_ANALOG_IN" : VOID
TITLE =
VERSION : 0.1

BEGIN'''

footer = '''END_FUNCTION'''

template = '''NETWORK
TITLE =

      A(    ; 
      L     {1}; 
      T     "DB_ANALOG_IN".{0}.MAX_EU; 
      SET   ; 
      SAVE  ; 
      CLR   ; 
      A     BR; 
      )     ; 
      JNB   _{3}; 
      L     {2}; 
      T     "DB_ANALOG_IN".{0}.MIN_EU; 
_{3}: NOP   0; 
NETWORK
TITLE =

      CALL "TYP_ANALOG_IN" (
           ANALOG_IN                := "DB_ANALOG_IN".{0});
      NOP   0;
'''

def main():
    sheet_name = sys.argv[1] 
    df1= test.getalltags(sheet_name)
    number = 0

    print header

    for index, row in df1.iterrows():
        number = number + 1
        high, low = test.splitrange(row['RANGE'])
        hexnumber = test.int_to_hex(number)  
        print template.format(test.replacedash(row['TagName']), low, high, hexnumber)
        

    print footer

if __name__ == '__main__':
    main()
    
