from valorant.utils.gameplay import check_buy_phase
from valorant import market
import time

shop = market.Shop()
time.sleep(4)
current_money = shop.check_money()
if check_buy_phase():

    shop.buy_weapon(money=current_money, primary_weapon="vandal", secondary_weapon="sheriff",
                    shield="heavy_shield")
    shop.drop_weapon(weapon="all")

    shop.buy_weapon(money=current_money, primary_weapon="phantom", secondary_weapon="classic",
                    shield="light_shield")
    shop.drop_weapon(weapon="all")

    shop.buy_weapon(money=current_money, primary_weapon="marshal", secondary_weapon="sheriff",
                    shield="heavy_shield")
    shop.drop_weapon(weapon="all")

    shop.buy_weapon(money=current_money, primary_weapon="operator", secondary_weapon="classic",
                    shield="light_shield")
    shop.drop_weapon(weapon="all")

    shop.buy_weapon(money=current_money, primary_weapon="judge", secondary_weapon="sheriff",
                    shield="heavy_shield")
    shop.drop_weapon(weapon="all")

    shop.buy_weapon(money=current_money, primary_weapon="odin", secondary_weapon="classic",
                    shield="light_shield")
    shop.drop_weapon(weapon="all")

    shop.buy_weapon(money=current_money, primary_weapon="ares", secondary_weapon="sheriff",
                    shield="heavy_shield")
    shop.drop_weapon(weapon="all")

    shop.buy_weapon(money=current_money, primary_weapon="bucky", secondary_weapon="classic",
                    shield="light_shield")
    shop.drop_weapon(weapon="all")

    shop.buy_weapon(money=current_money, primary_weapon="stinger", secondary_weapon="sheriff",
                    shield="heavy_shield")
    shop.drop_weapon(weapon="all")

    shop.buy_weapon(money=current_money, primary_weapon="spectre", secondary_weapon="classic",
                    shield="light_shield")
    shop.drop_weapon(weapon="all")

    shop.buy_weapon(money=current_money, primary_weapon="stinger", secondary_weapon="sheriff",
                    shield="light_shield")
