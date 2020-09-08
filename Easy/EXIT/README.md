# eXit

radare2로 열고 pdf @ main을 해준다
```
[0x000011a0]> pdf @ main
            ; DATA XREF from entry0 @ 0x11c1
┌ 388: int main (char **argv, char **envp);
│           ; var uint32_t var_ch @ rbp-0xc
│           ; var ssize_t s1 @ rbp-0x8
│           ; arg char **argv @ rsi
│           ; arg char **envp @ rdx
│           0x00001721      f30f1efa       endbr64
│           0x00001725      55             push rbp
│           0x00001726      4889e5         mov rbp, rsp
│           0x00001729      4883ec10       sub rsp, 0x10
│           0x0000172d      488d3df70900.  lea rdi, str.eXit           ; 0x212b ; "--- eXit ---" ; const char *s
│           0x00001734      e8d7f9ffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00001739      488d3df80900.  lea rdi, [0x00002138]       ; const char *s
│           0x00001740      e8cbf9ffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00001745      488d3df40900.  lea rdi, str.It_s_time_to_leave_the_Land_of_Ecodelia... ; 0x2140 ; "It's time to leave the Land of Ecodelia..." ; const char *s
│           0x0000174c      e8bff9ffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00001751      488d3d130a00.  lea rdi, str.Press_Enter_to_continue ; 0x216b ; "Press Enter to continue" ; const char *s
│           0x00001758      e8b3f9ffff     call sym.imp.puts           ; int puts(const char *s)
│           0x0000175d      e80efaffff     call sym.imp.getchar        ; int getchar(void)
│           0x00001762      488d3d1f0a00.  lea rdi, str.You_re_trapped_in_a_dungeon_with_your_friend._You_see_a_barrel._What_do_you_do ; 0x2188 ; "\nYou're trapped in a dungeon with your friend. You see a barrel. What do you do?" ; const char *s
│           0x00001769      e8a2f9ffff     call sym.imp.puts           ; int puts(const char *s)
│           0x0000176e      b800000000     mov eax, 0
│           0x00001773      e811fbffff     call sym.read               ; ssize_t read(int fildes, void *buf, size_t nbyte)
│           0x00001778      488945f8       mov qword [s1], rax
│           0x0000177c      488b45f8       mov rax, qword [s1]
│           0x00001780      4889c7         mov rdi, rax                ; char *arg1
│           0x00001783      e855fdffff     call fcn.000014dd
│           0x00001788      8945f4         mov dword [var_ch], eax
│           0x0000178b      837df402       cmp dword [var_ch], 2
│       ┌─< 0x0000178f      7408           je 0x1799
│       │   0x00001791      8b45f4         mov eax, dword [var_ch]
│      ┌──< 0x00001794      e90a010000     jmp 0x18a3
│      ││   ; CODE XREF from main @ 0x178f
│      │└─> 0x00001799      488b45f8       mov rax, qword [s1]
│      │    0x0000179d      ba0b000000     mov edx, 0xb                ; size_t n
│      │    0x000017a2      488d35300a00.  lea rsi, str.Move_barrel    ; 0x21d9 ; "Move barrel" ; const char *s2
│      │    0x000017a9      4889c7         mov rdi, rax                ; const char *s1
│      │    0x000017ac      e84ff9ffff     call sym.imp.strncmp        ; int strncmp(const char *s1, const char *s2, size_t n)
│      │    0x000017b1      85c0           test eax, eax
│      │┌─< 0x000017b3      740f           je 0x17c4
│      ││   0x000017b5      b800000000     mov eax, 0
│      ││   0x000017ba      e803fdffff     call fcn.000014c2
│     ┌───< 0x000017bf      e9df000000     jmp 0x18a3
│     │││   ; CODE XREF from main @ 0x17b3
│     ││└─> 0x000017c4      488d3d1d0a00.  lea rdi, str.The_barrel_rolls_aside_and_you_find_a_secret_tunnel._What_do_you_do ; 0x21e8 ; "\nThe barrel rolls aside and you find a secret tunnel. What do you do?" ; const char *s
│     ││    0x000017cb      e840f9ffff     call sym.imp.puts           ; int puts(const char *s)
│     ││    0x000017d0      488d3d570a00.  lea rdi, str.Enter_tunnel   ; 0x222e ; "Enter tunnel" ; char *arg1
│     ││    0x000017d7      e855fbffff     call fcn.00001331
│     ││    0x000017dc      85c0           test eax, eax
│     ││┌─< 0x000017de      750f           jne 0x17ef
│     │││   0x000017e0      b800000000     mov eax, 0
│     │││   0x000017e5      e8d8fcffff     call fcn.000014c2
│    ┌────< 0x000017ea      e9b4000000     jmp 0x18a3
│    ││││   ; CODE XREF from main @ 0x17de
│    │││└─> 0x000017ef      488d3d4a0a00.  lea rdi, str.You_start_to_escape_but_your_friend_is_too_weak_to_go_with_you._They_hand_you_a_note._What_do_you_do ; 0x2240 ; "\nYou start to escape but your friend is too weak to go with you. They hand you a note. What do you do?" ; const char *s
│    │││    0x000017f6      e815f9ffff     call sym.imp.puts           ; int puts(const char *s)
│    │││    0x000017fb      488d3da50a00.  lea rdi, str.Read_note      ; 0x22a7 ; "Read note" ; char *arg1
│    │││    0x00001802      e82afbffff     call fcn.00001331
│    │││    0x00001807      85c0           test eax, eax
│    │││┌─< 0x00001809      750f           jne 0x181a
│    ││││   0x0000180b      b800000000     mov eax, 0
│    ││││   0x00001810      e8adfcffff     call fcn.000014c2
│   ┌─────< 0x00001815      e989000000     jmp 0x18a3
│   │││││   ; CODE XREF from main @ 0x1809
│   ││││└─> 0x0000181a      488d3d970a00.  lea rdi, str.It_is_to_dark_to_read_the_note._What_do_you_do ; 0x22b8 ; "\nIt is to dark to read the note. What do you do?" ; const char *s
│   ││││    0x00001821      e8eaf8ffff     call sym.imp.puts           ; int puts(const char *s)
│   ││││    0x00001826      488d3dbc0a00.  lea rdi, str.Leave          ; 0x22e9 ; "Leave" ; char *arg1
│   ││││    0x0000182d      e8fffaffff     call fcn.00001331
│   ││││    0x00001832      85c0           test eax, eax
│   ││││┌─< 0x00001834      750c           jne 0x1842
│   │││││   0x00001836      b800000000     mov eax, 0
│   │││││   0x0000183b      e882fcffff     call fcn.000014c2
│  ┌──────< 0x00001840      eb61           jmp 0x18a3
│  ││││││   ; CODE XREF from main @ 0x1834
│  │││││└─> 0x00001842      488d3da70a00.  lea rdi, str.You_crawl_through_the_tunnel_and_the_tunnel_leads_you_to_a_beach._What_do_you_do ; 0x22f0 ; "\nYou crawl through the tunnel and the tunnel leads you to a beach. What do you do?" ; const char *s
│  │││││    0x00001849      e8c2f8ffff     call sym.imp.puts           ; int puts(const char *s)
│  │││││    0x0000184e      488d3dee0a00.  lea rdi, str.Look           ; 0x2343 ; "Look" ; char *arg1
│  │││││    0x00001855      e8d7faffff     call fcn.00001331
│  │││││    0x0000185a      85c0           test eax, eax
│  │││││┌─< 0x0000185c      750c           jne 0x186a
│  ││││││   0x0000185e      b800000000     mov eax, 0
│  ││││││   0x00001863      e85afcffff     call fcn.000014c2
│ ┌───────< 0x00001868      eb39           jmp 0x18a3
│ │││││││   ; CODE XREF from main @ 0x185c
│ ││││││└─> 0x0000186a      488d3dd70a00.  lea rdi, str.In_the_water_you_see_a_boat._What_do_you_do ; 0x2348 ; "\nIn the water you see a boat. What do you do?" ; const char *s
│ ││││││    0x00001871      e89af8ffff     call sym.imp.puts           ; int puts(const char *s)
│ ││││││    0x00001876      488d3df90a00.  lea rdi, str.Get_on_boat    ; 0x2376 ; "Get on boat" ; char *arg1
│ ││││││    0x0000187d      e8affaffff     call fcn.00001331
│ ││││││    0x00001882      85c0           test eax, eax
│ ││││││┌─< 0x00001884      750c           jne 0x1892
│ │││││││   0x00001886      b800000000     mov eax, 0
│ │││││││   0x0000188b      e832fcffff     call fcn.000014c2
│ ────────< 0x00001890      eb11           jmp 0x18a3
│ │││││││   ; CODE XREF from main @ 0x1884
│ ││││││└─> 0x00001892      488d3def0a00.  lea rdi, str.Congratulations__you_re_heading_to_a_new_world ; 0x2388 ; "\nCongratulations, you're heading to a new world!" ; const char *s
│ ││││││    0x00001899      e872f8ffff     call sym.imp.puts           ; int puts(const char *s)
│ ││││││    0x0000189e      b800000000     mov eax, 0
│ ││││││    ; XREFS: CODE 0x00001794  CODE 0x000017bf  CODE 0x000017ea  CODE 0x00001815  CODE 0x00001840
│ ││││││    ; XREFS: CODE 0x00001868  CODE 0x00001890
│ └└└└└└──> 0x000018a3      c9             leave
└           0x000018a4      c3             ret
```
메인 함수에는 별 내용이 없었고, 나는 숨겨진 함수를 찾았다  
0x00001783에 fcn.000014dd 함수였다  
ex) 딱히 숨겨져있지는 않았다..
<br/>

그러면 fcn.000014dd 함수를 보겠다
```
[0x000011a0]> pdf @ fcn.000014dd
            ; CALL XREF from main @ 0x1783
┌ 580: fcn.000014dd (char *arg1);
│           ; var char *ptr @ rbp-0x3f8
│           ; var char *format @ rbp-0x3f0
│           ; var int64_t canary @ rbp-0x8
│           ; arg char *arg1 @ rdi
│           0x000014dd      f30f1efa       endbr64
│           0x000014e1      55             push rbp
│           0x000014e2      4889e5         mov rbp, rsp
│           0x000014e5      4881ec000400.  sub rsp, 0x400
│           0x000014ec      4889bd08fcff.  mov qword [ptr], rdi        ; arg1
│           0x000014f3      64488b042528.  mov rax, qword fs:[0x28]
│           0x000014fc      488945f8       mov qword [canary], rax
│           0x00001500      31c0           xor eax, eax
│           0x00001502      488d8510fcff.  lea rax, [format]
│           0x00001509      48c7c1ffffff.  mov rcx, 0xffffffffffffffff
│           0x00001510      4889c2         mov rdx, rax
│           0x00001513      b800000000     mov eax, 0
│           0x00001518      4889d7         mov rdi, rdx
│           0x0000151b      f2ae           repne scasb al, byte [rdi]
│           0x0000151d      4889c8         mov rax, rcx
│           0x00001520      48f7d0         not rax
│           0x00001523      488d50ff       lea rdx, [rax - 1]
│           0x00001527      488d8510fcff.  lea rax, [format]
│           0x0000152e      4801d0         add rax, rdx
│           0x00001531      c7007232636f   mov dword [rax], 0x6f633272 ; 'r2co'
│                                                                      ; [0x6f633272:4]=-1
│           0x00001537      66c740046e7b   mov word [rax + 4], 0x7b6e  ; 'n{'
│                                                                      ; [0x7b6e:2]=0xffff
│           0x0000153d      c6400600       mov byte [rax + 6], 0
│           0x00001541      488b8d08fcff.  mov rcx, qword [ptr]
│           0x00001548      488d8510fcff.  lea rax, [format]
│           0x0000154f      ba1e000000     mov edx, 0x1e               ; size_t n
│           0x00001554      4889ce         mov rsi, rcx                ; const char *s2
│           0x00001557      4889c7         mov rdi, rax                ; char *s1
│           0x0000155a      e8f1fbffff     call sym.imp.strncat        ; char *strncat(char *s1, const char *s2, size_t n)
│           0x0000155f      488d8510fcff.  lea rax, [format]
│           0x00001566      4889c7         mov rdi, rax                ; const char *s
│           0x00001569      e8b2fbffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│           0x0000156e      4883e801       sub rax, 1
│           0x00001572      c6840510fcff.  mov byte [rbp + rax - 0x3f0], 0
│           0x0000157a      488b8508fcff.  mov rax, qword [ptr]
│           0x00001581      488d35f30a00.  lea rsi, [0x0000207b]
│           0x00001588      4889c7         mov rdi, rax
│           0x0000158b      e819feffff     call fcn.000013a9
│           0x00001590      85c0           test eax, eax
│       ┌─< 0x00001592      750a           jne 0x159e
│       │   0x00001594      b802000000     mov eax, 2
│      ┌──< 0x00001599      e96d010000     jmp 0x170b
│      ││   ; CODE XREF from fcn.000014dd @ 0x1592
│      │└─> 0x0000159e      488d3df30a00.  lea rdi, str.Your_friend_hands_you_a_note._What_do_you_do ; 0x2098 ; "\nYour friend hands you a note. What do you do?" ; const char *s
│      │    0x000015a5      e866fbffff     call sym.imp.puts           ; int puts(const char *s)
│      │    0x000015aa      b800000000     mov eax, 0
│      │    0x000015af      e8d5fcffff     call sym.read               ; ssize_t read(int fildes, void *buf, size_t nbyte)
│      │    0x000015b4      48898508fcff.  mov qword [ptr], rax
│      │    0x000015bb      488b8d08fcff.  mov rcx, qword [ptr]
│      │    0x000015c2      488d8510fcff.  lea rax, [format]
│      │    0x000015c9      ba1e000000     mov edx, 0x1e               ; size_t n
│      │    0x000015ce      4889ce         mov rsi, rcx                ; const char *s2
│      │    0x000015d1      4889c7         mov rdi, rax                ; char *s1
│      │    0x000015d4      e877fbffff     call sym.imp.strncat        ; char *strncat(char *s1, const char *s2, size_t n)
│      │    0x000015d9      488d8510fcff.  lea rax, [format]
│      │    0x000015e0      4889c7         mov rdi, rax                ; const char *s
│      │    0x000015e3      e838fbffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│      │    0x000015e8      4883e801       sub rax, 1
│      │    0x000015ec      c6840510fcff.  mov byte [rbp + rax - 0x3f0], 0
│      │    0x000015f4      488b8508fcff.  mov rax, qword [ptr]
│      │    0x000015fb      488d35c50a00.  lea rsi, [0x000020c7]
│      │    0x00001602      4889c7         mov rdi, rax
│      │    0x00001605      e89ffdffff     call fcn.000013a9
│      │    0x0000160a      85c0           test eax, eax
│      │┌─< 0x0000160c      750f           jne 0x161d
│      ││   0x0000160e      b800000000     mov eax, 0
│      ││   0x00001613      e8aafeffff     call fcn.000014c2
│     ┌───< 0x00001618      e9ee000000     jmp 0x170b
│     │││   ; CODE XREF from fcn.000014dd @ 0x160c
│     ││└─> 0x0000161d      488b8508fcff.  mov rax, qword [ptr]
│     ││    0x00001624      4889c7         mov rdi, rax                ; void *ptr
│     ││    0x00001627      e8c4faffff     call sym.imp.free           ; void free(void *ptr)
│     ││    0x0000162c      488d3da50a00.  lea rdi, str.The_note_says:__Don_t_leave_me_here_._Do_you_leave_your_friend_or_stay ; 0x20d8 ; "\nThe note says: \"Don't leave me here\". Do you leave your friend or stay?" ; const char *s
│     ││    0x00001633      e8d8faffff     call sym.imp.puts           ; int puts(const char *s)
│     ││    0x00001638      b800000000     mov eax, 0
│     ││    0x0000163d      e847fcffff     call sym.read               ; ssize_t read(int fildes, void *buf, size_t nbyte)
│     ││    0x00001642      48898508fcff.  mov qword [ptr], rax
│     ││    0x00001649      488b8d08fcff.  mov rcx, qword [ptr]
│     ││    0x00001650      488d8510fcff.  lea rax, [format]
│     ││    0x00001657      ba1e000000     mov edx, 0x1e               ; size_t n
│     ││    0x0000165c      4889ce         mov rsi, rcx                ; const char *s2
│     ││    0x0000165f      4889c7         mov rdi, rax                ; char *s1
│     ││    0x00001662      e8e9faffff     call sym.imp.strncat        ; char *strncat(char *s1, const char *s2, size_t n)
│     ││    0x00001667      488d8510fcff.  lea rax, [format]
│     ││    0x0000166e      4889c7         mov rdi, rax                ; const char *s
│     ││    0x00001671      e8aafaffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│     ││    0x00001676      4883e801       sub rax, 1
│     ││    0x0000167a      c6840510fcff.  mov byte [rbp + rax - 0x3f0], 0
│     ││    0x00001682      488b8508fcff.  mov rax, qword [ptr]
│     ││    0x00001689      488d35910a00.  lea rsi, [0x00002121]
│     ││    0x00001690      4889c7         mov rdi, rax
│     ││    0x00001693      e811fdffff     call fcn.000013a9
│     ││    0x00001698      85c0           test eax, eax
│     ││┌─< 0x0000169a      751b           jne 0x16b7
│     │││   0x0000169c      488b8508fcff.  mov rax, qword [ptr]
│     │││   0x000016a3      4889c7         mov rdi, rax                ; void *ptr
│     │││   0x000016a6      e845faffff     call sym.imp.free           ; void free(void *ptr)
│     │││   0x000016ab      b800000000     mov eax, 0
│     │││   0x000016b0      e80dfeffff     call fcn.000014c2
│    ┌────< 0x000016b5      eb54           jmp 0x170b
│    ││││   ; CODE XREF from fcn.000014dd @ 0x169a
│    │││└─> 0x000016b7      488d8510fcff.  lea rax, [format]
│    │││    0x000016be      48c7c1ffffff.  mov rcx, 0xffffffffffffffff
│    │││    0x000016c5      4889c2         mov rdx, rax
│    │││    0x000016c8      b800000000     mov eax, 0
│    │││    0x000016cd      4889d7         mov rdi, rdx
│    │││    0x000016d0      f2ae           repne scasb al, byte [rdi]
│    │││    0x000016d2      4889c8         mov rax, rcx
│    │││    0x000016d5      48f7d0         not rax
│    │││    0x000016d8      488d50ff       lea rdx, [rax - 1]
│    │││    0x000016dc      488d8510fcff.  lea rax, [format]
│    │││    0x000016e3      4801d0         add rax, rdx
│    │││    0x000016e6      66c7007d00     mov word [rax], 0x7d        ; '}'
│    │││                                                               ; [0x7d:2]=0
│    │││    0x000016eb      488d8510fcff.  lea rax, [format]
│    │││    0x000016f2      4889c6         mov rsi, rax
│    │││    0x000016f5      488d3d2a0a00.  lea rdi, str.s              ; 0x2126 ; "\n%s\n" ; const char *format
│    │││    0x000016fc      b800000000     mov eax, 0
│    │││    0x00001701      e83afaffff     call sym.imp.printf         ; int printf(const char *format)
│    │││    0x00001706      b800000000     mov eax, 0
│    │││    ; CODE XREFS from fcn.000014dd @ 0x1599, 0x1618, 0x16b5
│    └└└──> 0x0000170b      488b75f8       mov rsi, qword [canary]
│           0x0000170f      644833342528.  xor rsi, qword fs:[0x28]
│       ┌─< 0x00001718      7405           je 0x171f
│       │   0x0000171a      e811faffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from fcn.000014dd @ 0x1718
│       └─> 0x0000171f      c9             leave
└           0x00001720      c3             ret
```
되게 길지만 딱 봐도 flag를 연산하는 부분이었다  
보면 format에 r2con{을 담고 연산하고 그 후 마지막에 }를 넣어서 출력한다  
즉, 중간 부분에서 flag를 만든다는 것!!
<br/>

fcn.000014dd 함수를 잘 보면 아래와 비슷한 코드가 3번 나온다
```
│           0x00001541      488b8d08fcff.  mov rcx, qword [ptr]
│           0x00001548      488d8510fcff.  lea rax, [format]
│           0x0000154f      ba1e000000     mov edx, 0x1e               ; size_t n
│           0x00001554      4889ce         mov rsi, rcx                ; const char *s2
│           0x00001557      4889c7         mov rdi, rax                ; char *s1
│           0x0000155a      e8f1fbffff     call sym.imp.strncat        ; char *strncat(char *s1, const char *s2, size_t n)
│           0x0000155f      488d8510fcff.  lea rax, [format]
│           0x00001566      4889c7         mov rdi, rax                ; const char *s
│           0x00001569      e8b2fbffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│           0x0000156e      4883e801       sub rax, 1
│           0x00001572      c6840510fcff.  mov byte [rbp + rax - 0x3f0], 0
│           0x0000157a      488b8508fcff.  mov rax, qword [ptr]
│           0x00001581      488d35f30a00.  lea rsi, [0x0000207b]
│           0x00001588      4889c7         mov rdi, rax
│           0x0000158b      e819feffff     call fcn.000013a9
```
format과 ptr을 strncat 후 format에 저장한다  
그리고 ptr과 어떤 배열(위 코드에서는 [0x0000207b])을 인자로 fcn.000013a9를 실행한다
<br/>

인제 fcn.000013a9 함수를 보겟다
```
[0x000011a0]> pdf @ fcn.000013a9
            ; CALL XREFS from fcn.000014dd @ 0x158b, 0x1605, 0x1693
┌ 281: fcn.000013a9 (char *arg1, char *arg2);
│           ; var char *s @ rbp-0x80
│           ; var char *var_78h @ rbp-0x78
│           ; var uint32_t var_65h @ rbp-0x65
│           ; var int64_t var_64h @ rbp-0x64
│           ; var int64_t var_60h @ rbp-0x60
│           ; var int64_t var_58h @ rbp-0x58
│           ; var int64_t var_50h @ rbp-0x50
│           ; var int64_t var_48h @ rbp-0x48
│           ; var int64_t var_40h @ rbp-0x40
│           ; var int64_t var_38h @ rbp-0x38
│           ; var int64_t var_30h @ rbp-0x30
│           ; var int64_t var_28h @ rbp-0x28
│           ; var int64_t canary @ rbp-0x18
│           ; arg char *arg1 @ rdi
│           ; arg char *arg2 @ rsi
│           0x000013a9      f30f1efa       endbr64
│           0x000013ad      55             push rbp
│           0x000013ae      4889e5         mov rbp, rsp
│           0x000013b1      53             push rbx
│           0x000013b2      4883ec78       sub rsp, 0x78
│           0x000013b6      48897d88       mov qword [var_78h], rdi    ; arg1
│           0x000013ba      48897580       mov qword [s], rsi          ; arg2
│           0x000013be      64488b042528.  mov rax, qword fs:[0x28]
│           0x000013c7      488945e8       mov qword [canary], rax
│           0x000013cb      31c0           xor eax, eax
│           0x000013cd      48b8deadbeef.  movabs rax, 0xefbeaddeefbeadde
│           0x000013d7      48bacafe1337.  movabs rdx, 0x3713feca3713feca
│           0x000013e1      488945a0       mov qword [var_60h], rax
│           0x000013e5      488955a8       mov qword [var_58h], rdx
│           0x000013e9      48b801020304.  movabs rax, 0x807060504030201
│           0x000013f3      488945b0       mov qword [var_50h], rax
│           0x000013f7      66c745b8090a   mov word [var_48h], 0xa09   ; 2569
│           0x000013fd      48b80a090807.  movabs rax, 0x30405060708090a
│           0x00001407      48ba02013713.  movabs rdx, 0xcafe133713370102
│           0x00001411      488945c0       mov qword [var_40h], rax
│           0x00001415      488955c8       mov qword [var_38h], rdx
│           0x00001419      48b837133713.  movabs rax, 0xbeefcafe13371337
│           0x00001423      488945d0       mov qword [var_30h], rax
│           0x00001427      66c745d8adde   mov word [var_28h], 0xdead
│           0x0000142d      c7459c000000.  mov dword [var_64h], 0
│       ┌─< 0x00001434      eb55           jmp 0x148b
│       │   ; CODE XREF from fcn.000013a9 @ 0x14a0
│      ┌──> 0x00001436      8b459c         mov eax, dword [var_64h]
│      ╎│   0x00001439      4863d0         movsxd rdx, eax
│      ╎│   0x0000143c      488b4588       mov rax, qword [var_78h]
│      ╎│   0x00001440      4801d0         add rax, rdx
│      ╎│   0x00001443      0fb600         movzx eax, byte [rax]
│      ╎│   0x00001446      88459b         mov byte [var_65h], al
│      ╎│   0x00001449      8b459c         mov eax, dword [var_64h]
│      ╎│   0x0000144c      4898           cdqe
│      ╎│   0x0000144e      0fb64405a0     movzx eax, byte [rbp + rax - 0x60]
│      ╎│   0x00001453      30459b         xor byte [var_65h], al
│      ╎│   0x00001456      8b459c         mov eax, dword [var_64h]
│      ╎│   0x00001459      4898           cdqe
│      ╎│   0x0000145b      0fb64405c0     movzx eax, byte [rbp + rax - 0x40]
│      ╎│   0x00001460      89c2           mov edx, eax
│      ╎│   0x00001462      0fb6459b       movzx eax, byte [var_65h]
│      ╎│   0x00001466      01d0           add eax, edx
│      ╎│   0x00001468      88459b         mov byte [var_65h], al
│      ╎│   0x0000146b      8b459c         mov eax, dword [var_64h]
│      ╎│   0x0000146e      4863d0         movsxd rdx, eax
│      ╎│   0x00001471      488b4580       mov rax, qword [s]
│      ╎│   0x00001475      4801d0         add rax, rdx
│      ╎│   0x00001478      0fb600         movzx eax, byte [rax]
│      ╎│   0x0000147b      38459b         cmp byte [var_65h], al
│     ┌───< 0x0000147e      7407           je 0x1487
│     │╎│   0x00001480      b800000000     mov eax, 0
│    ┌────< 0x00001485      eb20           jmp 0x14a7
│    ││╎│   ; CODE XREF from fcn.000013a9 @ 0x147e
│    │└───> 0x00001487      83459c01       add dword [var_64h], 1
│    │ ╎│   ; CODE XREF from fcn.000013a9 @ 0x1434
│    │ ╎└─> 0x0000148b      8b459c         mov eax, dword [var_64h]
│    │ ╎    0x0000148e      4863d8         movsxd rbx, eax
│    │ ╎    0x00001491      488b4580       mov rax, qword [s]
│    │ ╎    0x00001495      4889c7         mov rdi, rax                ; const char *s
│    │ ╎    0x00001498      e883fcffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│    │ ╎    0x0000149d      4839c3         cmp rbx, rax
│    │ └──< 0x000014a0      7294           jb 0x1436
│    │      0x000014a2      b801000000     mov eax, 1
│    │      ; CODE XREF from fcn.000013a9 @ 0x1485
│    └────> 0x000014a7      488b4de8       mov rcx, qword [canary]
│           0x000014ab      6448330c2528.  xor rcx, qword fs:[0x28]
│       ┌─< 0x000014b4      7405           je 0x14bb
│       │   0x000014b6      e875fcffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from fcn.000013a9 @ 0x14b4
│       └─> 0x000014bb      4883c478       add rsp, 0x78
│           0x000014bf      5b             pop rbx
│           0x000014c0      5d             pop rbp
└           0x000014c1      c3             ret
```
이 친구는 딱 봐도 복잡하다..  
치트키 커터를 사용했다
```
undefined8 fcn.000013a9(char *arg1, char *arg2)
{
    uint64_t uVar1;
    undefined8 uVar2;
    int64_t in_FS_OFFSET;
    char *s;
    char *var_78h;
    int32_t var_64h;
    int64_t var_60h;
    int64_t var_58h;
    int64_t var_50h;
    int64_t var_48h;
    int64_t var_40h;
    int64_t var_38h;
    int64_t var_30h;
    int64_t var_28h;
    int64_t canary;
    
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    var_60h = -0x1041522110415222;
    var_58h = 0x3713feca3713feca;
    var_50h = 0x807060504030201;
    var_48h._0_2_ = 0xa09;
    var_40h = 0x30405060708090a;
    var_38h = -0x3501ecc8ecc8fefe;
    var_30h = -0x41103501ecc8ecc9;
    var_28h._0_2_ = 0xdead;
    var_64h = 0;
    do {
        uVar1 = strlen(arg2);
        if (uVar1 <= (uint64_t)(int64_t)var_64h) {
            uVar2 = 1;
code_r0x000014a7:
            if (canary != *(int64_t *)(in_FS_OFFSET + 0x28)) {
    // WARNING: Subroutine does not return
                __stack_chk_fail();
            }
            return uVar2;
        }
        if ((uint8_t)((arg1[var_64h] ^ *(uint8_t *)((int64_t)&var_60h + (int64_t)var_64h)) + *(char *)((int64_t)&var_40h + (int64_t)var_64h)) != arg2[var_64h]) {
            uVar2 = 0;
            goto code_r0x000014a7;
        }
        var_64h = var_64h + 1;
    } while( true );
}
```
arg1과 var_60h 배열의 값을 xor하고 var_40h 배열의 값과 더한 값을 arg2와 비교한다  
arg1은 ptr이고 arg2는 임의의 배열의 값이다  
즉, 이 문제는 역연산 문제인 것이다  
<br/>
임의의 배열 3개와 var_60h, var_40h의 배열을 따서 코드를 짰다
```
# flag = 'r2con{Sit down next to my friendLight matchStay}'

var_60h = 0xDEADBEEFDEADBEEFCAFE1337CAFE13370102030405060708090A.to_bytes(26, 'big')
var_40h = 0xDEADBEEFCAFE13371337CAFE133713370102030405060708090A.to_bytes(26, 'little')
First_arr = [ 0x97, 0xCD, 0xD2, 0xD6, 0xC0, 0xC7, 0xCD, 0x84, 0xEC, 0x91, 0xAD, 0x62, 0xF5, 0xF1, 0x65, 0x22, 0x58, 0x82, 0xB1, 0x37, 0x61, 0x3E, 0x5D, 0x2B, 0x14, 0x4C ]
Second_arr = [ 0x9C, 0xCD, 0xE1, 0x8E, 0xB0, 0x92, 0xD7, 0x91, 0xC0, 0x9E, 0xB2 ]
Third_arr = [ 0x97, 0xE2, 0xE7, 0x9D ]

print('r2con{', end='')

for i in range(0, len(First_arr)):
    print(chr((((First_arr[i]-var_40h[i])^var_60h[i])) & 0xff), end='')

for i in range(0, len(Second_arr)):
    print(chr((((Second_arr[i]-var_40h[i])^var_60h[i])) & 0xff), end='')

for i in range(0, len(Third_arr)):
    print(chr((((Third_arr[i]-var_40h[i])^var_60h[i])) & 0xff), end='')

print('}')
```
flag는 r2con{Sit down next to my friendLight matchStay}이었다