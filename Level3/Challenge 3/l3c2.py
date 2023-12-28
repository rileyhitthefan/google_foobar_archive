def l3c2(start, length):
    # Your code here
    checksum = 0
    for i in range(length):
        checksum ^= range_xor(start+i*length, start+i*length+length-i-1)
    return checksum
    
def range_xor(start, end):
    if start%2==0:
        rotation = [end, 1, end+1, 0]
    else:
        rotation = [start, start^end, start-1, (start-1)^end];
    return rotation[(end-start) % 4];

    
'''
def xor(num):
    rem = num%4
    if rem == 0:
        return num
    if rem == 1:
        return 1
    if rem == 2:
        return num+1
    return 0
'''
