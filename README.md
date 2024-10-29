# AI-Network-Intrusion-Detection

Raw TCP/IP dump data for a network simulating a typical US Air Force LAN is analyzed by AI to detect attacks.

Made by Divesh Bansal and Jordan Jamali.



## Proposed Groupings

### Service

**Safe**
ssh
http_443
imap4
ntp_u
domain_u
domain
ldap
echo
printer
time
whois

**Unsafe**
telnet
ftp
ftp_data
smtp
http
pop_2
pop_3
exec
login
shell
kshell
netbios_ns
netbios_dgm
iso_tsap
eco_i
ecr_i
urp_i
X11
sunrpc
uucp
uucp_path
sql_net
pm_dump
ctf
red_i
rje
discard
systat
gopher
finger
daytime
vmnet
auth
bgp
pop_2
pop_3

### Flag

**Safe**
SF
RSTO
RSTOS0
OTH

**Unsafe**
SH
S0
S2
REJ
S3
S1
RSTR

