# -*- coding: utf-8 -*-
import time,random

def back_submit_order(cap=[],args_list=[],db=[]):
    try:
        
        #出库单号
        with cap.app_context():
            choice_str = 'ABCDEFGHJKLNMPQRSTUVWSXYZ'
            str_time =  time.time()
            number_str = 'T'
            number_str += str(int(int(str_time)*1.301))
            for i in range(4):
                number_str += random.choice(choice_str)

