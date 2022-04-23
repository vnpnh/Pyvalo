from valorant.utils.gameplay import time_left
from valorant import config
import time

time.sleep(1)
custom_config = config(tesseract=r'D:\Program Files\Tesseract-OCR\tesseract.exe')  # custom config
print(time_left(config=custom_config))
