# Domain Password Analyzer (DPA)

DPA is a Windows Domain user/password analyzer and a visualizer assessment. This is a web based service that takes the following files as input:
-Windows NTDS
-Password file (Cracked NTDS)
 or
-Hash Password file (Hashcat output)


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

### Running

```sh
# git clone https://github.com/danTaler/Dissector-Web.git
# cd Dissector-Web
# ./run.py
```
Navigate to the: http://x.x.x.x:8889


### Todos

 -
 
 
 License
-------------

Apache LICENSE-2.0
https://www.apache.org/licenses/LICENSE-2.0
