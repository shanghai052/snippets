import math

#hex = raw_input("Enter your hex value here")
hex = 'B23DB59D15F736E32A347F1F'




#reg query HKLM\Sam\Sam\Domains\Account\v
def sidify(hex_string):
    hex_groups = []
    tmp_group = []
    byte = ''
    for (i, char) in enumerate(hex_string):
        i = i + 1
        byte += char
        if i % 2 == 0:
            tmp_group.append(byte)
            byte = ''
        if i % 8 == 0:
            hex_groups.append(tmp_group)
            tmp_group = []
    for i in hex_groups:
        rev_hex = ''.join(i[::-1])
        tmp_group.append(int(rev_hex, 16))
    return 'Your sid is S-1-5-21-%d-%d-%d' % (tmp_group[0],tmp_group[1],tmp_group[2])
    
hex = 'B23DB59D15F736E32A347F1F'
print sidify(hex)
