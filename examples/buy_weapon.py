from valorant import market

shop = market.Shop()
current_money = shop.check_money()
print(current_money)
shop.buy_weapon(money=current_money, primary_weapon="marshal", secondary_weapon="sheriff", shield="heavy_shields")


