from valorant.utils.gameplay import time_left
import valorant
import time

custom_config = valorant.config(tesseract=r'D:\Program Files\Tesseract-OCR\tesseract.exe')  # custom config

time.sleep(1)
print(time_left(config=custom_config))
