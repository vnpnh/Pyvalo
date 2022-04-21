import valorant
from valorant.utils.gameplay import check_buy_phase
from valorant.utils.gameplay import enemy_score_info, own_score_info
import time


from valorant.utils.helper import apply_config
# default config
# valo = valorant.config()
# custom config

valo = valorant.config(tesseract=r'D:\Program Files\Tesseract-OCR\tesseract.exe')
print(valo.__module__)
"""
Tesseract Path: D:\Program Files\Tesseract-OCR\tesseract.exe 
check_money_pos: (250, 120, 110, 55) 
check_buy_phase Path: (810, 140, 310, 140) 
enemy_score_info: (750, 25, 100, 55) 
own_score_info Path: (1050, 25, 100, 55) 
time_left_pos: (900, 25, 100, 55) 
failsafe Path: True
"""
print(valo.buy_phase_coor)  # (810, 140, 310, 140)

print("======")

# print(isinstance(valo, valo.__module__))

# print(check_buy_phase(valo))
time.sleep(1)
print(enemy_score_info(valo))
# print(own_score_info())