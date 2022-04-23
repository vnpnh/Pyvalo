from valorant.utils.gameplay import check_buy_phase
import time, valorant

custom_config = valorant.config(tesseract=r'D:\Program Files\Tesseract-OCR\tesseract.exe')

time.sleep(1)
print(check_buy_phase(config=custom_config))
