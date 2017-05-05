import pid_info
import sys
import re

reload(pid_info)

header = '''DmStructtag	Structure tags	Structure tag
[NAME][100][1]	[TYPE][101][1]	[LENGTH][105][1]	[FORMAT][106][1]	[CONNECTION][102][1]	[GROUP][104][1]	[ADDRPARAMS][108][1]	[SCALEVALID][112][2]	[SCALEPARAM1][113][1]	[SCALEPARAM2][114][1]	[SCALEPARAM3][115][1]	[SCALEPARAM4][116][1]	[MINLIMIT][117][1]	[MAXLIMIT][118][1]	[STARTVALUE][119][1]	[SUBSTVALUE][120][1]	[SUBSTVALUE_ON_MINLIMIT][121][2]	[SUBSTVALUE_ON_MAXLIMIT][122][2]	[SUBSTVALUE_AS_STARTVALUE][123][2]	[SUBSTVALUE_ON_ERROR][124][2]	[UPDATEMODE][111][2]	[SYNCHRONIZATION][125][2]	[RUNTIMEPERSISTENCE][126][2]	[PLCVARIABLENAME][209][1]
Name	Data type	Length	Format adaptation	Connection	Group	Address	Linear scaling	AS value range from	AS value range to	OS value range from	OS value range to	Low limit	High limit	Start value	Substitute value	Substitute value at low limit	Substitute value at high limit	Substitute value as start value	Substitute value on connection errors	Computer-local	Synchronization	Runtime persistence	AS tag name'''

template = '''{0}	PID	0		{1}		{2}	0									0	0	0	0	0	0	0	'''

def main():
    groupbase = 'DB4,DBB'
    number = 0
    sheet_name = sys.argv[1] 
    df1= pid_info.getalltags(sheet_name)
    match = re.search(r'(\d)', sheet_name, flags=0)
    if match:
        value = 'CPU' + match.group(1) + '_1'
    else:
        raise ValueError('Wrong sheetname format!')

    print header

    for index, row in df1.iterrows():
        groupname = groupbase + str(102*number)
        number = number + 1
        print template.format(pid_info.replacedash(row['Controller']), value, groupname)
    

if __name__ == '__main__':
    main()