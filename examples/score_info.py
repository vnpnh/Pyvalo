import valorant
from valorant.utils.gameplay import enemy_score_info, own_score_info
import time

custom_config = valorant.config(tesseract=r'D:\Program Files\Tesseract-OCR\tesseract.exe')
time.sleep(1)

print(enemy_score_info(config=custom_config))
print(own_score_info(config=custom_config))