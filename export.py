import test
reload(test)

header = '''Name	Data type	Length	Format adaptation	Connection	Group	Address	Linear scaling	AS value range from	AS value range to	OS value range from	OS value range to	Low limit	High limit	Start value	Substitute value	Substitute value at low limit	Substitute value at high limit	Substitute value as start value	Substitute value on connection errors	Computer-local	Synchronization	Runtime persistence	AS tag name'''
template = '''{0}.ACK	Binary Tag	1		Internal tags			0									0	0	0	0	0	0	0	
{0}.BIO	Binary Tag	1		Internal tags			0									0	0	0	0	0	0	0	
{0}.Comment	Text tag 8-bit character set	255		Internal tags			0									0	0	0	0	0	0	0	
{0}.EH	Binary Tag	1		{1}		DB1,D12.1	0									0	0	0	0	0	0	0	
{0}.EHH	Binary Tag	1		{1}		DB1,D12.0	0									0	0	0	0	0	0	0	
{0}.EL	Binary Tag	1		Internal tags			0									0	0	0	0	0	0	0	
{0}.ELL	Binary Tag	1		Internal tags			0									0	0	0	0	0	0	0	
{0}.HA	Binary Tag	1		Internal tags			0									0	0	0	0	0	0	0	
{0}.HA_UNACK	Text tag 8-bit character set	255		Internal tags			0									0	0	0	0	0	0	0	
{0}.HHA	Binary Tag	1		Internal tags			0									0	0	0	0	0	0	0	
{0}.HHA_UNACK	Text tag 8-bit character set	255		Internal tags			0									0	0	0	0	0	0	0	
{0}.HHV	Unsigned 32-bit value	4		Internal tags			0									0	0	0	0	0	0	0	
{0}.HHV_1	Unsigned 32-bit value	4		Internal tags			0									0	0	0	0	0	0	0	
{0}.HV	Unsigned 32-bit value	4		Internal tags			0									0	0	0	0	0	0	0	
{0}.HV_1	Unsigned 32-bit value	4		Internal tags			0									0	0	0	0	0	0	0	
{0}.IN	Floating-point number 32-bit IEEE 754	4	FloatToFloat	{1}		DB1,DD0	0									0	0	0	0	0	0	0	
{0}.LA	Binary Tag	1		Internal tags			0									0	0	0	0	0	0	0	
{0}.LA_UNACK	Text tag 8-bit character set	255		Internal tags			0									0	0	0	0	0	0	0	
{0}.LLA	Binary Tag	1		Internal tags			0									0	0	0	0	0	0	0	
{0}.LLA_UNACK	Text tag 8-bit character set	255		Internal tags			0									0	0	0	0	0	0	0	
{0}.LLV	Unsigned 32-bit value	4		Internal tags			0									0	0	0	0	0	0	0	
{0}.LLV_1	Unsigned 32-bit value	4		Internal tags			0									0	0	0	0	0	0	0	
{0}.LV	Unsigned 32-bit value	4		Internal tags			0									0	0	0	0	0	0	0	
{0}.LV_1	Unsigned 32-bit value	4		Internal tags			0									0	0	0	0	0	0	0	
{0}.MAINT	Binary Tag	1		Internal tags			0									0	0	0	0	0	0	0	
{0}.MAX	Unsigned 32-bit value	4	DwordToUnsignedDword	{1}		DB1,DD4	0									0	0	0	0	0	0	0	
{0}.MIN	Unsigned 32-bit value	4	DwordToUnsignedDword	{1}		DB1,DD8	0									0	0	0	0	0	0	0	
{0}.Name	Text tag 8-bit character set	255		Internal tags			0									0	0	0	0	0	0	0	
{0}.TagPrefix	Text tag 8-bit character set	255		Internal tags			0									0	0	0	0	0	0	0	'''


def print_export(sheet_name, value):
    print header
    for index, row in test.getalltags(sheet_name).iterrows():
        print template.format(test.replacedash(row['TagName']), value)


if __name__ == '__main__':
    print_export('L3 Analog Input', '########')