#!C:\Python34\python.exe
# -*- coding: utf-8 -*-
'''
Created on 22 feb. 2017

@author: Levshinovsky Mikhail
'''

from pyhislip import HiSLIP

a = HiSLIP()
a.connect('192.168.0.7')

a.set_max_message_size(256)

a.device_clear()

a.request_lock()
a.write("MMEM:LOAD 'D:\Tower\PPM.csa'")

a.write("CALC1:PAR:SEL 'Meas_S21_Mag'")

raw_data = a.ask("CALC1:DATA:SNP:PORT? '1, 2'")


a.release_lock()

print(raw_data[0:100])