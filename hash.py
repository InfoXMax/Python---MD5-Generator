#!/usr/bin/env python3

import hashlib
import colorama
from colorama import Fore, Style

print(" _        ,__         _     _ __   __             ")
print(" | , __   /  `   __.  `.   /  |    |    ___  _  .-")
print(" | |'  `. |__  .'   \   \,'   |\  /|   /   `  \,' ")
print(" | |    | |    |    |  ,'\    | \/ |  |    |  /\  	MD5 Encrypted")
print(" / /    | |     `._.' /   \   /    /  `.__/| /  \ ")
print("          /                                       ")

str = input('Your TEXT: ')
MD5 = hashlib.md5(str.encode())
print(Fore.WHITE + "Your Text : ", Fore.RED + str )
print(Fore.WHITE + "The MD5 Hash :",Fore.GREEN + MD5.hexdigest())
