# AI-Network-Intrusion-Detection

Raw TCP/IP dump data for a network simulating a typical US Air Force LAN is analyzed by AI to detect attacks.

Made by Divesh Bansal and Jordan Jamali.



## Groupings

The following service and flag fields were categorized as safe or potentially unsafe to feed to our model.

### Service

**Safe**
- ssh
- http_443
- imap4
- ntp_u
- domain_u
- domain
- ldap
- echo
- printer
- time
- whois
- efs
- name

**Unsafe**
- hostnames
- IRC
- nnsp
- X11
- mtp
- uucp
- http
- urp_i
- tim_i
- Z39_50
- smtp
- systat
- klogin
- sunrpc
- http_8001
- gopher
- supdup
- discard
- courier
- iso_tsap
- finger
- rje
- red_i
- eco_i
- shell
- kshell
- exec
- remote_job
- ftp
- daytime
- pm_dump
- ctf
- pop_2
- private
- ftp_data
- bgp
- csnet_ns
- netstat
- netbios_ns
- pop_3
- login
- vmnet
- auth
- sql_net
- other
- urh_i
- netbios_ssn
- nntp
- telnet
- uucp_path
- link
- netbios_dgm
- ecr_i

### Flag

**Safe**
- SF
- RSTO
- RSTOS0
- OTH

**Unsafe**
- SH
- S0
- S2
- REJ
- S3
- S1
- RSTR