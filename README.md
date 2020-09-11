## IP-Straw

Fetch IP information from internet and display it on CLI.

- [x] List IP Geo information
- [x] Check IP Reputation
- [ ] Generate report
- [ ] Custom provider selection

Build status : Beta

### Usage

./ip-straw.py ip-address

- Eg : ./ip-straw 5.157.56.105

```
 ___ ____            ____  _
|_ _|  _ \          / ___|| |_ _ __ __ ___      __
 | || |_) |  _____  \___ \| __| '__/ _` \ \ /\ / /
 | ||  __/  |_____|  ___) | |_| | | (_| |\ V  V /
|___|_|             |____/ \__|_|  \__,_| \_/\_/


----- By github.com/jamesarems   (c) 2020


[ * ] Processing 5.157.56.105

Findings are,
COUNTRY : Sweden
REGION : AB
REGION NAME : Stockholm County
CITY : Stockholm
ZIP : 100 05
ISP : InterConnects
ZONE : Europe/Stockholm
ORGANIZATION :

[*] Scanning botscout + ABUSE (botscout.com)
+++ Found

[*] Scanning Sblam + ABUSE (sblam.com)

[*] Scanning StopForum + ABUSE (stopforumspam.com)
+++ Found

[*] Scanning SockProxy + Proxy

[*] Scanning BadBots + ATTACKS

[*] Scanning haleySSH + ATTACKS
```
