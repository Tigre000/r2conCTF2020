# Radare License Checker

radare2로 열고 main을 찾는다  
PE 리버싱 많이 하면 느낌으로 찾을 수 있다  
pdf @ fcn.00402e50을 할려했지만 너무 길다고 한다..  
pd @ fcn.00402e50을 해준다
```
[0x00401500]> pd @ fcn.00402e50
            ; CALL XREF from fcn.004011b0 @ 0x4013f3
┌ 523: fcn.00402e50 (int64_t arg1, int64_t arg2);
│           ; var int64_t var_1h @ rbp+0x49
│           ; var int64_t var_281h @ rbp+0x2c9
│           ; var int64_t var_24h @ rsp+0x2c
│           ; var int64_t var_28h @ rsp+0x30
│           ; var int64_t var_3eh @ rsp+0x46
│           ; var int64_t var_3fh @ rsp+0x47
│           ; var int64_t var_40h @ rsp+0x48
│           ; var uint32_t var_2c0h @ rsp+0x2c8
│           ; arg int64_t arg1 @ rcx
│           ; arg int64_t arg2 @ rdx
│           0x00402e50      4157           push r15
│           0x00402e52      4156           push r14
│           0x00402e54      4155           push r13
│           0x00402e56      4154           push r12
│           0x00402e58      55             push rbp
│           0x00402e59      57             push rdi
│           0x00402e5a      56             push rsi
│           0x00402e5b      53             push rbx
│           0x00402e5c      4881ecd80200.  sub rsp, 0x2d8
│           0x00402e63      89cb           mov ebx, ecx                ; arg1
│           0x00402e65      4889d6         mov rsi, rdx                ; arg2
│           0x00402e68      e8c3e9ffff     call fcn.00401830
│           0x00402e6d      488d0d8c7100.  lea rcx, str.Radare_License_Checker ; section..rdata
│                                                                      ; 0x40a000 ; "Radare License Checker" ; const char *s
│           0x00402e74      e837feffff     call sub.msvcrt.dll_puts    ; int puts(const char *s)
│           0x00402e79      83fb01         cmp ebx, 1                  ; 1
│       ┌─< 0x00402e7c      0f8e5d010000   jle 0x402fdf
│       │   0x00402e82      83fb02         cmp ebx, 2                  ; 2
│      ┌──< 0x00402e85      0f856a010000   jne 0x402ff5
│      ││   0x00402e8b      4c8b7608       mov r14, qword [rsi + 8]
│      ││   0x00402e8f      4c89f1         mov rcx, r14                ; const char *s
│      ││   0x00402e92      e809feffff     call sub.msvcrt.dll_strlen  ; size_t strlen(const char *s)
│      ││   0x00402e97      4883f822       cmp rax, 0x22               ; 34
│     ┌───< 0x00402e9b      0f856a010000   jne 0x40300b
│     │││   0x00402ea1      488d0d517200.  lea rcx, str.Decoding_license_data... ; 0x40a0f9 ; "Decoding license data...\n" ; const char *s
│     │││   0x00402ea8      4c8d3d116800.  lea r15, [0x004096c0]
│     │││   0x00402eaf      488d6c2440     lea rbp, [var_40h]
│     │││   0x00402eb4      4531e4         xor r12d, r12d
│     │││   0x00402eb7      48bb00260000.  movabs rbx, 0x100002600
│     │││   0x00402ec1      e8eafdffff     call sub.msvcrt.dll_puts    ; int puts(const char *s)
│     │││   0x00402ec6      488d44243e     lea rax, [var_3eh]
│     │││   0x00402ecb      488b359ab400.  mov rsi, qword [sym.imp.msvcrt.dll_isprint] ; [0x40e36c:8]=0xe6b4 reloc.msvcrt.dll_isprint
│     │││   0x00402ed2      4889442428     mov qword [var_28h], rax
│     │││   0x00402ed7      660f1f840000.  nop word [rax + rax]
│     │││   ; CODE XREF from fcn.00402e50 @ 0x402faa
│     │││   0x00402ee0      b901000000     mov ecx, 1                  ; DWORD dwMilliseconds
│     │││   0x00402ee5      4489642424     mov dword [var_24h], r12d
│     │││   0x00402eea      4889ef         mov rdi, rbp
│     │││   0x00402eed      e87efdffff     call fcn.00402c70
│     │││   0x00402ef2      430fb60426     movzx eax, byte [r14 + r12]
│     │││   0x00402ef7      b950000000     mov ecx, 0x50               ; 'P' ; 80
│     │││   0x00402efc      4989e9         mov r9, rbp                 ; int64_t arg4
│     │││   0x00402eff      41b881020000   mov r8d, 0x281              ; 641 ; int64_t arg3
│     │││   0x00402f05      4c89fa         mov rdx, r15                ; int64_t arg2
│     │││   0x00402f08      c644243f00     mov byte [var_3fh], 0
│     │││   0x00402f0d      8844243e       mov byte [var_3eh], al
│     │││   0x00402f11      31c0           xor eax, eax
│     │││   0x00402f13      f348ab         rep stosq qword [rdi], rax
│     │││   0x00402f16      488b4c2428     mov rcx, qword [var_28h]    ; int64_t arg1
│     │││   0x00402f1b      c60700         mov byte [rdi], 0
│     │││   0x00402f1e      e82de7ffff     call fcn.00401650
│     │││   0x00402f23      440fb66c2440   movzx r13d, byte [var_40h]
│     │││   0x00402f29      4584ed         test r13b, r13b
│    ┌────< 0x00402f2c      0f84ef000000   je 0x403021
│    ││││   0x00402f32      80bc24c00200.  cmp byte [var_2c0h], 0
│   ┌─────< 0x00402f3a      0f85e1000000   jne 0x403021
│   │││││   0x00402f40      4c8d7d01       lea r15, [rbp + 1]
│   │││││   0x00402f44      488dbd810200.  lea rdi, [rbp + 0x281]
│   │││││   0x00402f4b      0f1f440000     nop dword [rax + rax]
│   │││││   ; CODE XREF from fcn.00402e50 @ 0x402f84
│   │││││   0x00402f50      410fb6cd       movzx ecx, r13b
│   │││││   0x00402f54      ffd6           call rsi
│   │││││   0x00402f56      85c0           test eax, eax
│   │││││   0x00402f58      0f94c0         sete al
│   │││││   0x00402f5b      4180fd20       cmp r13b, 0x20              ; 32
│   │││││   0x00402f5f      770e           ja 0x402f6f
│   │││││   0x00402f61      4889da         mov rdx, rbx
```
<br/>

이 부분을 보면 flag의 길이가 0x22(34)이라는 것을 알 수 있다
```
│      ││   0x00402e8b      4c8b7608       mov r14, qword [rsi + 8]
│      ││   0x00402e8f      4c89f1         mov rcx, r14                ; const char *s
│      ││   0x00402e92      e809feffff     call sub.msvcrt.dll_strlen  ; size_t strlen(const char *s)
│      ││   0x00402e97      4883f822       cmp rax, 0x22               ; 34
```
flag는 프로그램 시 인자로 주고, 34글자가 아니면 종료된다
<br/>

그냥 직접 실행해봤다
```
G:\r2conCTF2020\Medium\RADARE_LICENSE_CHECKER>radarelicensechecker.exe
Radare License Checker
ERROR: no license provided!

Usage: radarelicensechecker.exe <license>


G:\r2conCTF2020\Medium\RADARE_LICENSE_CHECKER>radarelicensechecker.exe 1234567890123456789012345678901234
Radare License Checker
Decoding license data...



ERROR: decryption error in block 0!


G:\r2conCTF2020\Medium\RADARE_LICENSE_CHECKER>radarelicensechecker.exe r234567890123456789012345678901234
Radare License Checker
Decoding license data...

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNNNNNNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXXXXXXXXXXXXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXXXXXXXXXXXXXXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXXXKKKKKKKKKXXXXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNNNXXXXKKKKK00000OOOOOOOOO0000KKXXNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXXKK000OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO00KKXXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMM

ERROR: decryption error in block 2!


G:\r2conCTF2020\Medium\RADARE_LICENSE_CHECKER>radarelicensechecker.exe r2con{7890123456789012345678901234
Radare License Checker
Decoding license data...

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNNNNNNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXXXXXXXXXXXXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXXXXXXXXXXXXXXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXXXKKKKKKKKKXXXXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNNNXXXXKKKKK00000OOOOOOOOO0000KKXXNNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXXKK000OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO00KKXXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXK00OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO00KXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXK0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO00KNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0000000000OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0KXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWNXXXXXNWMMMMMMMMMMMMMMMMMMMMMMWNXK0OOOOOOOOOOOOOOOOOOOOOO000KKXXXXNNNNNNWWWWWWWWWNNNNNXXXKKK000OOOOOOOOOOOOOOOOOOOOOO0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWXXXXXXXXWMMMMMMMMMMMMMMMMMMMWNXK0OOOOOOOOOOOOOOOOOOO0KKXXNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNXXKK00OOOOOOOOOOOOOOOOOO0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNXXXXXXXXXNWMMMMMMMMMMMMMMMWNXK0OOOOOOOOOOOOOOOOO0KXXNWWMMMMMMMMMMMMWXK0kkkOOO000KXXNWMMMMMMMMMMMMMMMMWWNNXK00OOOOOOOOOOOOOOO0KNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWNXXXXXXXXXXXWMMMMMMMMMMMMMWNK0OOOOOOOOOOOOOOOO0KXNWWMMMMMMMMWNKOxdl:;,..        .....',;cloxO0XNWMMMMMMMMMMMMWWNXK0OOOOOOOOOOOOOOKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWNXXXXXXXXXXXXNMMMMMMMMMMWNX0OOOOOOOOOOOOOOO0KXNWWMMMMMWNKOdl:,..                              ..';coxOKNWMMMMMMMMMMWNXK0OOOOOOOOOOOO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWNXXXXXXXXXXXXXNWMMMMMMMWNK0OOOOOOOOOOOOOO0KXNWMMMMMWKxo:'.                      .''''''...
.';ldkKNWMMMMMMMWNXK0OOOOOOOOOOO0XWMMMMMMMMMMMMMMMMMMMMMMMWWNXXXNNWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWNXXXXXXXXXXXXXXXNMMMMMWXKOOOOOOOOOOOOOOO0XNWMMMMN0xc,.     ..,:clloolc;.        .oKKKKKKK0d.          ...     .';cdOXWMMMMMWWXKOOOOOOOOOOO0NWMMMMMMMMMMMMMMMMMMMMWNXXXXXXXNWMMMMMMMMMMMM
MMMMMMMMMMMMMMMWXXXXXXXXXXXXXXXXNMMMWN0OOOOOOOOOOOOOOO0XWWMMWNOo,.         c0KXXXXXXXXKOc.      :0XKKXXKKXKc          :0Oxo:.       .:dONMMMMMWNK0OOOOOOOOO0KNWMMMMMMMMMMMMMMMMMWXXXXXXXXXXNMMMMMMMMMMMM
MMMMMMMMMMMMMMMWXXXXXXXXXXXXXXXXNMMW

ERROR: decryption error in block 6!
```
실행해보니 flag가 어디까지 맞았는지 알려줬다
즉, 브루트포스 문제였다
하지만 실행속도가 느렸다
<br/>

코드를 확인해보니 Sleep 함수가 중간에 있었다
```
[0x00401500]> pdf @ fcn.00402c70
            ; CALL XREF from fcn.00402e50 @ 0x402eed
┌ 23: fcn.00402c70 (DWORD dwMilliseconds);
│           ; arg DWORD dwMilliseconds @ rcx
│           0x00402c70      4883ec28       sub rsp, 0x28
│           0x00402c74      69c9e8030000   imul ecx, ecx, 0x3e8
│           0x00402c7a      ff1504b60000   call qword [sym.imp.KERNEL32.dll_Sleep] ; [0x40e284:8]=0xe53c reloc.KERNEL32.dll_Sleep ; "<\xe5" ; VOID Sleep(DWORD dwMilliseconds)
│           0x00402c80      31c0           xor eax, eax
│           0x00402c82      4883c428       add rsp, 0x28
└           0x00402c86      c3             ret
```
이 함수를 바로 return하게 패치하였다
<br/>

브루트포스 코드를 짜서 돌렸다
```
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
```
flag는 r2con{D0nt_Do_Crypt0_At_Hom3_Kids}이었다