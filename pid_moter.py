import test
import pid_info

header = '''DmStructtag	Structure tags	Structure tag
[NAME][100][1]	[TYPE][101][1]	[LENGTH][105][1]	[FORMAT][106][1]	[CONNECTION][102][1]	[GROUP][104][1]	[ADDRPARAMS][108][1]	[SCALEVALID][112][2]	[SCALEPARAM1][113][1]	[SCALEPARAM2][114][1]	[SCALEPARAM3][115][1]	[SCALEPARAM4][116][1]	[MINLIMIT][117][1]	[MAXLIMIT][118][1]	[STARTVALUE][119][1]	[SUBSTVALUE][120][1]	[SUBSTVALUE_ON_MINLIMIT][121][2]	[SUBSTVALUE_ON_MAXLIMIT][122][2]	[SUBSTVALUE_AS_STARTVALUE][123][2]	[SUBSTVALUE_ON_ERROR][124][2]	[UPDATEMODE][111][2]	[SYNCHRONIZATION][125][2]	[RUNTIMEPERSISTENCE][126][2]	[PLCVARIABLENAME][209][1]
Name	Data type	Length	Format adaptation	Connection	Group	Address	Linear scaling	AS value range from	AS value range to	OS value range from	OS value range to	Low limit	High limit	Start value	Substitute value	Substitute value at low limit	Substitute value at high limit	Substitute value as start value	Substitute value on connection errors	Computer-local	Synchronization	Runtime persistence	AS tag name
'''

template = '''{0}	MOTOR	0		{1}			0									0	0	0	0	0	0	0	'''

def main (value):
    df1 = test.df_filter(test.df_tags, 'DESCRIPTION', 'DAMPER')
    for index, row in df1.iterrows():
        print template.format(test.replacedash(row['TagName']), value)
    
if __name__ == '__main__':
    main('NewConnection_1')

