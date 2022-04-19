from valorant.utils.gameplay import check_buy_phase
from valorant import market
from valorant.utils.gameplay import enemy_score_info, own_score_info
import random, time, pickle

shop = market.Shop()
with open(r'D:/valorant_model/buyassistmodel', 'rb') as training_model:
    model = pickle.load(training_model)

time.sleep(5)
while 1:
  if check_buy_phase():
      current_money = shop.check_money() 
      add_score = random.choice([1,2,3,4,5,6,7,8,9])
      enemy = enemy_score_info() + add_score
      own = own_score_info() + add_score
      total_round = enemy + own

      data = [[enemy, own, total_round, current_money]]
      weapon = model.predict(data)
      shop.buy_weapon(money=current_money, primary_weapon=weapon, 
                      secondary_weapon=random.choice(['classic', 'sheriff']),
                      shield=random.choice(['heavy_shield', 'light_shield']))
      shop.drop_weapon(weapon="all")

 