from valorant.utils.gameplay import enemy_score_info, own_score_info
import valorant
import time

default_config = valorant.config()  # default config
time.sleep(1)
print(enemy_score_info(config=default_config))
print(own_score_info(config=default_config))