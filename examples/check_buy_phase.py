from valorant.utils.gameplay import check_buy_phase
import valorant
import time

default_config = valorant.config()  # default config
time.sleep(1)
print(check_buy_phase(config=default_config))
