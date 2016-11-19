# Domain Password Analyzer (DPA)

DPA is a Windows Domain user/password analyzer and a visualizer assessment. This is a web based service that takes the following files as input:
- Windows NTDS
- Password file (Cracked NTDS)
 or
- Windows NTDS 
- Hash Password file (Hashcat output)


The results are disaplayed into detailes in a web interface.

Features:
- Domain user information (number of users, suspicious names in use...)
- NTLM and LM in use
- Detailed cracked passwords
- Which accounts have been hacked

![alt tag](https://github.com/danTaler/Domain-Password-Analyzer/blob/master/screenshots/screenshot_1.PNG)

![alt tag](https://github.com/danTaler/Domain-Password-Analyzer/blob/master/screenshots/screenshot_2.PNG)

![alt tag](https://github.com/danTaler/Domain-Password-Analyzer/blob/master/screenshots/screenshot_3.PNG)


### Software

- Python 2.7
- Flask (http://flask.pocoo.org/)

### Usage

```sh
# git clone https://github.com/danTaler/Domain-Password-Analyzer.git
# cd Dissector-Web
# ./run.py
```
Navigate to the: http://x.x.x.x:8889


### About the Input Files:

1. The Windows NTDS should be your PwDump style format.
... user:id:lm:ntlm:::

2. The Password file should be your file containing passwords only.
...password1
...password2
...password3

3. The Hash Password file should be a file containing hashes following by passwords. Similar to hashcat output or its .pot file:
...872BFACBE774904406D0D250B89AAD0C:some_pass
...C0A9E41E3A55882283358449B915CD9B:another_pass



### Todos

 -
 
 
 License
-------------

Apache LICENSE-2.0
https://www.apache.org/licenses/LICENSE-2.0
