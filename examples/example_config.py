import valorant


valo = valorant.config(tesseract=r'D:\Program Files\Tesseract-OCR\tesseract.exe')
print(valo)
"""
Tesseract: D:\Program Files\Tesseract-OCR\tesseract.exe 
check_money_pos: (250, 120, 110, 55) 
check_buy_phase Path: (810, 140, 310, 140) 
enemy_score_info: (750, 25, 100, 55) 
own_score_info Path: (1050, 25, 100, 55) 
time_left_pos: (900, 25, 100, 55) 
failsafe Path: True
"""

print(valo.buy_phase_coor)  # (810, 140, 310, 140)