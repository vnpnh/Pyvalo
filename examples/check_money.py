from valorant import market
import valorant
import time

custom_config = valorant.config(tesseract=r'D:\Program Files\Tesseract-OCR\tesseract.exe')  # custom config
time.sleep(1)

shop = market.Shop()
money = shop.check_money(show=False, config=custom_config)
print(money)