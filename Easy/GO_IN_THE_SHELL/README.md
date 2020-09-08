# Go in the Shell

이 친구는 서버에 접속해서 푸는 문제이다  
그래서 일단 로컬에서 실행시켜봤다
```
r2@Tigre000:/mnt/g/r2conCTF2020/Easy/GO_IN_THE_SHELL$ ./ctf

   ___        _         _   _            __ _          _ _
  / _ \___   (_)_ __   | |_| |__   ___  / _\ |__   ___| | |
 / /_\/ _ \  | | '_ \  | __| '_ \ / _ \ \ \| '_ \ / _ \ | |
/ /_\\ (_) | | | | | | | |_| | | |  __/ _\ \ | | |  __/ | |
\____/\___/  |_|_| |_|  \__|_| |_|\___| \__/_| |_|\___|_|_|

---------------------
$ ls
README.md
chall.txt
ctf
solve_go_in_the_shell.py

$ help
Available commands: ls, pwd, cat flag.txt, exit
$ cat flag.txt
The flag is r2con{...
lol it isn't going to be that easy
```
쉘 프로그램인 것 같고, cat flag.txt는 막혀있었다
<br/>

radare2로 열고 pdf @ sym.go.main.main을 해준다  
너무 길어서 짜르겠다
```
│ ╎╎╎╎╎│╎   0x004ad240      48ba67683073.  movabs rdx, 0x546e497473306867 ; 'gh0stInT'
│ ╎╎╎╎╎│╎   0x004ad24a      483911         cmp qword [rcx], rdx
│ ────────< 0x004ad24d      750d           jne 0x4ad25c
│ ╎╎╎╎╎│╎   0x004ad24f      817908686547.  cmp dword [rcx + 8], 0x30476568
```
이런 부분이 있었다  
느낌 상 히든 커맨드인듯하다
<br/>

아래는 스트링으로 바로 안 돌려줘서 직접 확인했다
```
[0x00457630]> ? 0x30476568 | grep string
string  "heG0"
```
히든 커맨드는 gh0stInTheG0이었다
<br/>

로컬에서 히든 커맨드를 넣어보니 프롬프트가 바꿔졌다
```
r2@Tigre000:/mnt/g/r2conCTF2020/Easy/GO_IN_THE_SHELL$ ./ctf

   ___        _         _   _            __ _          _ _
  / _ \___   (_)_ __   | |_| |__   ___  / _\ |__   ___| | |
 / /_\/ _ \  | | '_ \  | __| '_ \ / _ \ \ \| '_ \ / _ \ | |
/ /_\\ (_) | | | | | | | |_| | | |  __/ _\ \ | | |  __/ | |
\____/\___/  |_|_| |_|  \__|_| |_|\___| \__/_| |_|\___|_|_|

---------------------
$ gh0stInTheG0
what are you doing?...NO STOP PLEA--
#
```
<br/>

아쉽지만 지금은 서버가 닫혀 확인이 불가능하다ㅠㅜ  
아래는 pwntools를 써서 만들어둔 소스이다
```
from pwn import *
from time import sleep

# flag = 'r2con{!s3cr3tc0mmands4r3th3bestc0mmands!}'

r = remote("challenges.0xmurphy.me", 3333)

r.sendline("gh0stInTheG0")
sleep(5)
r.recv(1024)
r.sendline("cat flag.txt")
print(r.recv(1024)[:-4].decode())
r.close()
```
flag는 r2con{!s3cr3tc0mmands4r3th3bestc0mmands!}이었다