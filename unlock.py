#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SkyEmie_'  https://github.com/SkyEmie
https://en.wikipedia.org/wiki/Luhn_algorithm
"""

import time
#from flashbootlib import test
import os
import math

##########################################################################################################################

def tryUnlockBootloader(checksum):

    unlock      = False
    algoOEMcode = 1000000000000000 #base
    incrementCalculated = int(checksum+math.sqrt(imei)*1024)
    
    while(unlock == False):
        print(algoOEMcode)
        sdrout = str(os.system('fastboot oem unlock '+str(algoOEMcode)))
        sdrout = sdrout.split(' ')
        for i in sdrout:
            if i == 'success':
                return(algoOEMcode)

        algoOEMcode += incrementCalculated

def luhn_checksum(imei):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(imei)
    oddDigits = digits[0::2]
    evenDigits = digits[1::2]
    checksum = 0
    checksum += sum(oddDigits)
    for i in evenDigits:
        checksum += sum(digits_of(i*2))
    return (10 - checksum % 10)

##########################################################################################################################

print('\n\n           Unlock Bootloader script - By SkyEmie_\'')
print('\n\n  (Please enable USB DEBBUG and OEM UNLOCK if the device isn\'t appear..)')
print('  /!\ All data will be erased /!\\\n')
input(' Press Enter to detect device..\n')

os.system('adb devices')

imei     = int(input('Type IMEI digit (14 digits):'))

input('Press Enter to reboot your device..\n')
os.system('adb reboot bootloader')
input('Press Enter when your device is ready.. (This may take time, depending on your cpu/serial port)\n')

codeOEM = tryUnlockBootloader(luhn_checksum(imei))

os.system('fastboot getvar unlocked')
os.system('fastboot reboot')

print('\n\nDevice unlock ! OEM CODE : '+codeOEM)
print('(Keep it safe)\n')
input('Press Enter to exit..\n')
exit()


