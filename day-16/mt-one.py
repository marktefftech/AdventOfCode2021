'''
idx 0,1,2: packet version
idx 3,4,5: type ID

	if type == 4:
		it's literal
		n of 5-bit groups
		last group starts with 0

	if type != 4:
		it's operator
		idx 6: length type ID

		if length type ID == 0:
			idx from 7 to 22: length of all sub-packets

		if length type ID == 1:
			idx from 7 to 18: length of all sub-packets
'''
with open('/Users/mteffeteller/AoC2021/day-16/16.in', 'r') as f:
    inp = f.read().strip()
    full_binary = bin(int(inp, 16))[2:]

print(inp)
print(full_binary)

sumOfVersions = 0

def main(packet):
    version = int(packet[:3], 2)
    id_type = int(packet[3:6], 2)
    # 
    bits = tuple(packet[6:])

    print(f'{version=}')
    print(f'{id_type=}')
    print(f'{bits=}')

    if id_type == 4:
        # take the version numbers (literal)
        # we just need to know where the next packet begins
        lengthOfPacket = 6
        lenthOfGroup = 5
        # bits=('1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0')
        for i, val in enumerate(bits):
            if bits[i] == 1: # not the last group, skip the next 4 bits
                lengthOfPacket+= lenthOfGroup
                i+=5

            else:
                # last group
                lengthOfPacket+= lenthOfGroup
                print(lengthOfPacket)
                break
        
        print(lengthOfPacket)

    else:
        # operator packet
        lengthTypeId = 
        break
                
main(full_binary)