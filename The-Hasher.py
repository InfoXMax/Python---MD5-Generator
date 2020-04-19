#!/usr/bin/env python3

import hashlib,binascii
import colorama
from colorama import Fore, Style
import base64

print(" _        ,__         _     _ __   __             ")
print(" | , __   /  `   __.  `.   /  |    |    ___  _  .-")
print(" | |'  `. |__  .'   \   \,'   |\  /|   /   `  \,' ")
print(" | |    | |    |    |  ,'\    | \/ |  |    |  /\  	The Hasher ")
print(" / /    | |     `._.' /   \   /    /  `.__/| /  \ ")
print("          /                                       ")

str = input('Type Your TEXT: ')
# Start The Coder
MD5 = hashlib.md5(str.encode())
SHA1 = hashlib.sha1(str.encode())
SHA256 = hashlib.sha256(str.encode())
SHA512 = hashlib.sha512(str.encode())
base64Value = base64.b64encode(str.encode())
NTLM =  hashlib.new('md4', str.encode('utf-16le')).digest()
# End The Coder
print(Fore.WHITE + "Your Text : ", Fore.RED + str )
#The Result
print(Fore.WHITE + "The MD5 Hash :",Fore.YELLOW + MD5.hexdigest())
print(Fore.WHITE + "The SHA1 Hash :",Fore.GREEN + SHA1.hexdigest())
print(Fore.WHITE + "The SHA256 Hash :",Fore.GREEN + SHA256.hexdigest())
print(Fore.WHITE + "The SHA512 Hash :",Fore.GREEN + SHA512.hexdigest())
print (Fore.WHITE + "The NTLM Hash :",Fore.BLUE + binascii.hexlify(NTLM).decode('utf-8'))
print(Fore.WHITE + "The Base64 : " , Fore.MAGENTA + base64Value.decode('utf-8'))

with open('HASHES.txt', 'a') as f:
	print("MD5 : ", MD5.hexdigest(),'\n', "SHA1 : " , SHA1.hexdigest(),'\n', "SHA256 : " , SHA256.hexdigest(),'\n', "SHA512 : " , SHA512.hexdigest(),'\n', "BASE64 : " , base64Value,'\n', "NTLM : " , binascii.hexlify(NTLM),'\n' ,file=f)
