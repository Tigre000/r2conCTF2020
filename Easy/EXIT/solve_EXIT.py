a = 0xDEADBEEFDEADBEEFCAFE1337CAFE13370102030405060708090A.to_bytes(26, 'big')
b = 0xDEADBEEFCAFE13371337CAFE133713370102030405060708090A.to_bytes(26, 'little')

# flag = 'r2con{Sit down next to my friendLight matchStay}'

print('r2con{', end='')
c = [ 0x97, 0xCD, 0xD2, 0xD6, 0xC0, 0xC7, 0xCD, 0x84, 0xEC, 0x91, 0xAD, 0x62, 0xF5, 0xF1, 0x65, 0x22, 0x58, 0x82, 0xB1, 0x37, 0x61, 0x3E, 0x5D, 0x2B, 0x14, 0x4C ]
for i in range(0, len(c)):
    print(chr(((c[i]-b[i]^a[i])) & 0xff), end='')
c = [ 0x9C, 0xCD, 0xE1, 0x8E, 0xB0, 0x92, 0xD7, 0x91, 0xC0, 0x9E, 0xB2 ]
for i in range(0, len(c)):
    print(chr(((c[i]-b[i]^a[i])) & 0xff), end='')
c = [ 0x97, 0xE2, 0xE7, 0x9D ]
for i in range(0, len(c)):
    print(chr(((c[i]-b[i]^a[i])) & 0xff), end='')
print('}')