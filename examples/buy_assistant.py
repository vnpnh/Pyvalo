from valorant import market
from valorant.utils.gameplay import check_buy_phase
import time
shop = market.Shop()
print("Start Bot")

while True:
    print("Checking buy phase")
    data = check_buy_phase()
    print(data)
    if data:
        current_money = shop.check_money()
        print("Current Money: ", str(current_money))
        # this is my buying strategy that mostly I use repeatedly
        primary = "vandal"
        secondary = "classic"
        shield = "heavy_shields"
        if 2000 <= current_money <= 2500:
            primary = "spectre"
        elif 2000 > current_money >= 1500:
            primary="marshal"
        elif 1400 <= current_money <= 2000:
            primary="marshal"
            shield = "light_shields"

        shop.buy_weapon(money=current_money, primary_weapon=primary, secondary_weapon=secondary,
                        shield=shield)
        shop.drop_weapon(weapon="all")
        print("Buy and drop weapon success")
    time.sleep(10)
