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