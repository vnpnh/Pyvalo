from valorant import market

shop = market.Shop()
money = shop.check_money(show=False)
print(money)