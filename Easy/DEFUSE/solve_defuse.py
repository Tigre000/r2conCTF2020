from string import ascii_lowercase

# flag = 'r2con{esilrulezonemoretime}'
arr = [ 0x60, 0x50, 0x54, 0x71, 0x60, 0x65, 0x54, 0x50, 0x60, 0x51, 0x54, 0x65, 0x60, 0x51, 0x70, 0x65, 0x51, 0x54, 0x70, 0x60 ]
arr.reverse()
index = '10101101321112110111'

print('r2con{', end='')
for i in range(0, len(arr)):
    count = 0
    for input_str in ascii_lowercase:
        tmp = ((ord(input_str) ^ 0x28) + 0x15) & 0x5ff5fff5
        if arr[i] == tmp:
            if count == int(index[i]):
                print(input_str, end='')
            count += 1
print('}')