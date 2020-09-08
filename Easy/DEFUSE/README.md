# Defuse

퍼블 먹었다 ㅎㅎ

radare2로 열고 pdf @ main을 해준다
```
[0x000010e0]> pdf @ main
            ; DATA XREF from entry0 @ 0x1101
┌ 422: int main (uint32_t argc, char **argv);
│           ; var char **s @ rbp-0x80
│           ; var uint32_t var_74h @ rbp-0x74
│           ; var int64_t var_6ch @ rbp-0x6c
│           ; var size_t var_68h @ rbp-0x68
│           ; var size_t var_64h @ rbp-0x64
│           ; var int64_t var_60h @ rbp-0x60
│           ; var int64_t var_5ch @ rbp-0x5c
│           ; var int64_t var_58h @ rbp-0x58
│           ; var int64_t var_54h @ rbp-0x54
│           ; var int64_t var_50h @ rbp-0x50
│           ; var int64_t var_4ch @ rbp-0x4c
│           ; var int64_t var_48h @ rbp-0x48
│           ; var int64_t var_44h @ rbp-0x44
│           ; var int64_t var_40h @ rbp-0x40
│           ; var int64_t var_3ch @ rbp-0x3c
│           ; var int64_t var_38h @ rbp-0x38
│           ; var int64_t var_34h @ rbp-0x34
│           ; var int64_t var_30h @ rbp-0x30
│           ; var int64_t var_2ch @ rbp-0x2c
│           ; var int64_t var_28h @ rbp-0x28
│           ; var int64_t var_24h @ rbp-0x24
│           ; var int64_t var_20h @ rbp-0x20
│           ; var int64_t var_1ch @ rbp-0x1c
│           ; var int64_t var_18h @ rbp-0x18
│           ; var int64_t var_14h @ rbp-0x14
│           ; var int64_t canary @ rbp-0x8
│           ; arg uint32_t argc @ rdi
│           ; arg char **argv @ rsi
│           0x00001447      f30f1efa       endbr64
│           0x0000144b      55             push rbp
│           0x0000144c      4889e5         mov rbp, rsp
│           0x0000144f      4883c480       add rsp, 0xffffffffffffff80
│           0x00001453      897d8c         mov dword [var_74h], edi    ; argc
│           0x00001456      48897580       mov qword [s], rsi          ; argv
│           0x0000145a      64488b042528.  mov rax, qword fs:[0x28]
│           0x00001463      488945f8       mov qword [canary], rax
│           0x00001467      31c0           xor eax, eax
│           0x00001469      837d8c02       cmp dword [var_74h], 2
│       ┌─< 0x0000146d      742c           je 0x149b
│       │   0x0000146f      488d3d511000.  lea rdi, str.Bomb_defusal   ; 0x24c7 ; "****** Bomb defusal*******" ; const char *s
│       │   0x00001476      e825fcffff     call sym.imp.puts           ; int puts(const char *s)
│       │   0x0000147b      b800000000     mov eax, 0
│       │   0x00001480      e8a7fdffff     call fcn.0000122c
│       │   0x00001485      488d3d561000.  lea rdi, str.Usage:_defuse__code ; 0x24e2 ; "Usage: defuse [code]" ; const char *s
│       │   0x0000148c      e80ffcffff     call sym.imp.puts           ; int puts(const char *s)
│       │   0x00001491      b801000000     mov eax, 1
│      ┌──< 0x00001496      e93c010000     jmp 0x15d7
│      ││   ; CODE XREF from main @ 0x146d
│      │└─> 0x0000149b      c745a0600000.  mov dword [var_60h], 0x60   ; '`'
│      │    0x000014a2      c745a4500000.  mov dword [var_5ch], 0x50   ; 'P'
│      │    0x000014a9      c745a8540000.  mov dword [var_58h], 0x54   ; 'T'
│      │    0x000014b0      c745ac710000.  mov dword [var_54h], 0x71   ; 'q'
│      │    0x000014b7      c745b0600000.  mov dword [var_50h], 0x60   ; '`'
│      │    0x000014be      c745b4650000.  mov dword [var_4ch], 0x65   ; 'e'
│      │    0x000014c5      c745b8540000.  mov dword [var_48h], 0x54   ; 'T'
│      │    0x000014cc      c745bc500000.  mov dword [var_44h], 0x50   ; 'P'
│      │    0x000014d3      c745c0600000.  mov dword [var_40h], 0x60   ; '`'
│      │    0x000014da      c745c4510000.  mov dword [var_3ch], 0x51   ; 'Q'
│      │    0x000014e1      c745c8540000.  mov dword [var_38h], 0x54   ; 'T'
│      │    0x000014e8      c745cc650000.  mov dword [var_34h], 0x65   ; 'e'
│      │    0x000014ef      c745d0600000.  mov dword [var_30h], 0x60   ; '`'
│      │    0x000014f6      c745d4510000.  mov dword [var_2ch], 0x51   ; 'Q'
│      │    0x000014fd      c745d8700000.  mov dword [var_28h], 0x70   ; 'p'
│      │    0x00001504      c745dc650000.  mov dword [var_24h], 0x65   ; 'e'
│      │    0x0000150b      c745e0510000.  mov dword [var_20h], 0x51   ; 'Q'
│      │    0x00001512      c745e4540000.  mov dword [var_1ch], 0x54   ; 'T'
│      │    0x00001519      c745e8700000.  mov dword [var_18h], 0x70   ; 'p'
│      │    0x00001520      c745ec600000.  mov dword [var_14h], 0x60   ; '`'
│      │    0x00001527      c74594010000.  mov dword [var_6ch], 1
│      │    0x0000152e      488b4580       mov rax, qword [s]
│      │    0x00001532      4883c008       add rax, 8
│      │    0x00001536      488b00         mov rax, qword [rax]
│      │    0x00001539      4889c7         mov rdi, rax                ; const char *s
│      │    0x0000153c      e86ffbffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│      │    0x00001541      89459c         mov dword [var_64h], eax
│      │    0x00001544      837d9c14       cmp dword [var_64h], 0x14
│      │┌─< 0x00001548      0f8584000000   jne 0x15d2
│      ││   0x0000154e      488b4580       mov rax, qword [s]
│      ││   0x00001552      4883c008       add rax, 8
│      ││   0x00001556      488b00         mov rax, qword [rax]
│      ││   0x00001559      4889c7         mov rdi, rax                ; int64_t arg1
│      ││   0x0000155c      e889fcffff     call fcn.000011ea
│      ││   0x00001561      85c0           test eax, eax
│     ┌───< 0x00001563      746d           je 0x15d2
│     │││   0x00001565      8b459c         mov eax, dword [var_64h]
│     │││   0x00001568      894598         mov dword [var_68h], eax
│    ┌────< 0x0000156b      eb3f           jmp 0x15ac
│    ││││   ; CODE XREF from main @ 0x15b0
│   ┌─────> 0x0000156d      488b4580       mov rax, qword [s]
│   ╎││││   0x00001571      4883c008       add rax, 8
│   ╎││││   0x00001575      488b10         mov rdx, qword [rax]
│   ╎││││   0x00001578      8b459c         mov eax, dword [var_64h]
│   ╎││││   0x0000157b      2b4598         sub eax, dword [var_68h]
│   ╎││││   0x0000157e      4898           cdqe
│   ╎││││   0x00001580      4801d0         add rax, rdx
│   ╎││││   0x00001583      0fb600         movzx eax, byte [rax]
│   ╎││││   0x00001586      0fbec0         movsx eax, al
│   ╎││││   0x00001589      89c7           mov edi, eax                ; int64_t arg1
│   ╎││││   0x0000158b      e839fcffff     call fcn.000011c9
│   ╎││││   0x00001590      8b5598         mov edx, dword [var_68h]
│   ╎││││   0x00001593      83ea01         sub edx, 1
│   ╎││││   0x00001596      4863d2         movsxd rdx, edx
│   ╎││││   0x00001599      8b5495a0       mov edx, dword [rbp + rdx*4 - 0x60]
│   ╎││││   0x0000159d      39d0           cmp eax, edx
│   ╎││││   0x0000159f      0f94c0         sete al
│   ╎││││   0x000015a2      0fb6c0         movzx eax, al
│   ╎││││   0x000015a5      214594         and dword [var_6ch], eax
│   ╎││││   0x000015a8      836d9801       sub dword [var_68h], 1
│   ╎││││   ; CODE XREF from main @ 0x156b
│   ╎└────> 0x000015ac      837d9800       cmp dword [var_68h], 0
│   └─────< 0x000015b0      7fbb           jg 0x156d
│     │││   0x000015b2      8b4594         mov eax, dword [var_6ch]
│     │││   0x000015b5      83e001         and eax, 1
│     │││   0x000015b8      85c0           test eax, eax
│    ┌────< 0x000015ba      740c           je 0x15c8
│    ││││   0x000015bc      b800000000     mov eax, 0
│    ││││   0x000015c1      e8b1fdffff     call fcn.00001377
│   ┌─────< 0x000015c6      eb0a           jmp 0x15d2
│   │││││   ; CODE XREF from main @ 0x15ba
│   │└────> 0x000015c8      b800000000     mov eax, 0
│   │ │││   0x000015cd      e8bcfdffff     call fcn.0000138e
│   │ │││   ; CODE XREFS from main @ 0x1548, 0x1563, 0x15c6
│   └─└─└─> 0x000015d2      b800000000     mov eax, 0
│      │    ; CODE XREF from main @ 0x1496
│      └──> 0x000015d7      488b4df8       mov rcx, qword [canary]
│           0x000015db      6448330c2528.  xor rcx, qword fs:[0x28]
│       ┌─< 0x000015e4      7405           je 0x15eb
│       │   0x000015e6      e8d5faffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from main @ 0x15e4
│       └─> 0x000015eb      c9             leave
└           0x000015ec      c3             ret
```
<br/>

이 부분을 보면 flag의 길이가 0x14(20)이라는 것을 알 수 있다
```
│      │    0x0000152e      488b4580       mov rax, qword [s]
│      │    0x00001532      4883c008       add rax, 8
│      │    0x00001536      488b00         mov rax, qword [rax]
│      │    0x00001539      4889c7         mov rdi, rax                ; const char *s
│      │    0x0000153c      e86ffbffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│      │    0x00001541      89459c         mov dword [var_64h], eax
│      │    0x00001544      837d9c14       cmp dword [var_64h], 0x14
```
<br/>

이 부분은 flag를 체크하는 부분이다
```
│     │││   0x00001565      8b459c         mov eax, dword [var_64h]
│     │││   0x00001568      894598         mov dword [var_68h], eax
│    ┌────< 0x0000156b      eb3f           jmp 0x15ac
│    ││││   ; CODE XREF from main @ 0x15b0
│   ┌─────> 0x0000156d      488b4580       mov rax, qword [s]
│   ╎││││   0x00001571      4883c008       add rax, 8
│   ╎││││   0x00001575      488b10         mov rdx, qword [rax]
│   ╎││││   0x00001578      8b459c         mov eax, dword [var_64h]
│   ╎││││   0x0000157b      2b4598         sub eax, dword [var_68h]
│   ╎││││   0x0000157e      4898           cdqe
│   ╎││││   0x00001580      4801d0         add rax, rdx
│   ╎││││   0x00001583      0fb600         movzx eax, byte [rax]
│   ╎││││   0x00001586      0fbec0         movsx eax, al
│   ╎││││   0x00001589      89c7           mov edi, eax                ; int64_t arg1
│   ╎││││   0x0000158b      e839fcffff     call fcn.000011c9
│   ╎││││   0x00001590      8b5598         mov edx, dword [var_68h]
│   ╎││││   0x00001593      83ea01         sub edx, 1
│   ╎││││   0x00001596      4863d2         movsxd rdx, edx
│   ╎││││   0x00001599      8b5495a0       mov edx, dword [rbp + rdx*4 - 0x60]
│   ╎││││   0x0000159d      39d0           cmp eax, edx
│   ╎││││   0x0000159f      0f94c0         sete al
│   ╎││││   0x000015a2      0fb6c0         movzx eax, al
│   ╎││││   0x000015a5      214594         and dword [var_6ch], eax
│   ╎││││   0x000015a8      836d9801       sub dword [var_68h], 1
│   ╎││││   ; CODE XREF from main @ 0x156b
│   ╎└────> 0x000015ac      837d9800       cmp dword [var_68h], 0
│   └─────< 0x000015b0      7fbb           jg 0x156d
```
위에 flag의 길이를 확인한 부분 보면 flag의 길이는 var_64h에 있다  
그리고 0x00001565~0x00001568 주소에서 var_68h에 복사한다  
그리고 flag를 한 글자 씩 가져와서 fcn.000011c9 함수를 실행하고 그 결과 값을 edx와 비교한다  
edx는 dword [rbp + (*[var_68h]-1)*4 - 0x60]이므로 var_68h의 값에 따라 [rbp - 0x14]의 값부터 [rbp - 0x60]의 값까지 flag와 비교하게된다
<br/>

아래는 [rbp - 0x14]의 값부터 [rbp - 0x60]의 값이다
```
│      │└─> 0x0000149b      c745a0600000.  mov dword [var_60h], 0x60   ; '`'
│      │    0x000014a2      c745a4500000.  mov dword [var_5ch], 0x50   ; 'P'
│      │    0x000014a9      c745a8540000.  mov dword [var_58h], 0x54   ; 'T'
│      │    0x000014b0      c745ac710000.  mov dword [var_54h], 0x71   ; 'q'
│      │    0x000014b7      c745b0600000.  mov dword [var_50h], 0x60   ; '`'
│      │    0x000014be      c745b4650000.  mov dword [var_4ch], 0x65   ; 'e'
│      │    0x000014c5      c745b8540000.  mov dword [var_48h], 0x54   ; 'T'
│      │    0x000014cc      c745bc500000.  mov dword [var_44h], 0x50   ; 'P'
│      │    0x000014d3      c745c0600000.  mov dword [var_40h], 0x60   ; '`'
│      │    0x000014da      c745c4510000.  mov dword [var_3ch], 0x51   ; 'Q'
│      │    0x000014e1      c745c8540000.  mov dword [var_38h], 0x54   ; 'T'
│      │    0x000014e8      c745cc650000.  mov dword [var_34h], 0x65   ; 'e'
│      │    0x000014ef      c745d0600000.  mov dword [var_30h], 0x60   ; '`'
│      │    0x000014f6      c745d4510000.  mov dword [var_2ch], 0x51   ; 'Q'
│      │    0x000014fd      c745d8700000.  mov dword [var_28h], 0x70   ; 'p'
│      │    0x00001504      c745dc650000.  mov dword [var_24h], 0x65   ; 'e'
│      │    0x0000150b      c745e0510000.  mov dword [var_20h], 0x51   ; 'Q'
│      │    0x00001512      c745e4540000.  mov dword [var_1ch], 0x54   ; 'T'
│      │    0x00001519      c745e8700000.  mov dword [var_18h], 0x70   ; 'p'
│      │    0x00001520      c745ec600000.  mov dword [var_14h], 0x60   ; '`'
```
<br/>

그럼 인제 fcn.000011c9을 보겠다
```
[0x000010e0]> pdf @ fcn.000011c9
            ; CALL XREF from main @ 0x158b
┌ 33: fcn.000011c9 (int64_t arg1);
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg int64_t arg1 @ rdi
│           0x000011c9      f30f1efa       endbr64
│           0x000011cd      55             push rbp
│           0x000011ce      4889e5         mov rbp, rsp
│           0x000011d1      89f8           mov eax, edi                ; arg1
│           0x000011d3      8845fc         mov byte [var_4h], al
│           0x000011d6      0fb645fc       movzx eax, byte [var_4h]
│           0x000011da      83f028         xor eax, 0x28
│           0x000011dd      0fbec0         movsx eax, al
│           0x000011e0      83c015         add eax, 0x15
│           0x000011e3      25f5fff55f     and eax, 0x5ff5fff5
│           0x000011e8      5d             pop rbp
└           0x000011e9      c3             ret
```
이 함수는 되게 간단하다  
입력 값을 0x28과 xor하고 0x15를 더하고 0x5ff5fff5와 and 연산한 뒤 리턴한다
<br/>

인제 코드를 작성해보겠다
```
from string import ascii_lowercase

arr = [ 0x60, 0x50, 0x54, 0x71, 0x60, 0x65, 0x54, 0x50, 0x60, 0x51, 0x54, 0x65, 0x60, 0x51, 0x70, 0x65, 0x51, 0x54, 0x70, 0x60 ]
arr.reverse()

for i in range(0, len(arr)):
    count = 0
    for input_str in ascii_lowercase:
        tmp = ((ord(input_str) ^ 0x28) + 0x15) & 0x5ff5fff5
        if arr[i] == tmp:
            print(i, input_str)
```
<br/>

망했다 결과 값을 보니 게싱 문제였다..
```
0 e
1 s
1 u
2 a
2 i
2 o
3 l
3 n
4 p
4 r
4 x
4 z
5 s
5 u
6 l
6 n
7 c
7 e
8 p
8 r
8 x
8 z
9 a
9 i
9 o
10 l
10 n
11 c
11 e
12 k
12 m
13 a
13 i
13 o
14 p
14 r
14 x
14 z
15 c
15 e
16 t
16 v
17 a
17 i
17 o
18 k
18 m
19 c
19 e
```
생긴걸로 봤을때 esilrule로 시작하고 moretime으로 끝나는 것으로 보인다
<br/>

중간에 4자리만 돌려봣다
```
import itertools

for a in product("prxz", "aio", "ln", "ce"):
    print(''.join(a))
```
```
palc
pale
panc
pane
pilc
pile
pinc
pine
polc
pole
ponc
pone
ralc
rale
ranc
rane
rilc
rile
rinc
rine
rolc
role
ronc
rone
xalc
xale
xanc
xane
xilc
xile
xinc
xine
xolc
xole
xonc
xone
zalc
zale
zanc
zane
zilc
zile
zinc
zine
zolc
zole
zonc
zone
```
돌려보니 마지막에 있는 zone이 너무 잘 보였다
<br/>

flag는 r2con{esilrulezonemoretime}이었다
<br/>

```
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

# from itertools import product
# 
# for a in product("prxz", "aio", "ln", "ce"):
#     print(''.join(a))
```