import subprocess, itertools, string

# flag = 'r2con{D0nt_Do_Crypt0_At_Hom3_Kids}'
flag = list('r2con{555555555555555555555555555}')

print('r2con{', end='')
for count in range(6, 33):
    for a in itertools.product(string.ascii_letters+string.digits+string.punctuation):
        flag[count] = a[0]
        fd = subprocess.Popen(['patched.exe', ''.join(flag)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = fd.stdout.read()
        if result.find(b'decryption error in block ') == -1:
            print(a[0] + '}')
            exit()
        result = result[result.find(b'decryption error in block ')+26:]
        result = int(result[:result.find(b'!')].decode())
        if (count+1) == result:
            print(a[0], end='')
            break

# cp radarelicensechecker.exe patched.exe
# r2 -w patched.exe
# wa ret @ 0x00402c70
# exit