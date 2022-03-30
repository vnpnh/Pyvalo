from valorant import market

#edit value
"""
[price, (x, y)]
x,y mean position
[3000, (904, 670)]
"""
shop = market.Shop()
shop['vandal']=[3000, (904, 670)]
print(shop['vandal'])

#add new weapon
shop['new weapon']=[3100, (904, 670)]
print(shop['new weapon'])