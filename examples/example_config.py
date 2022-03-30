from valorant.config import MarketConfig, Config

configuration = Config()
configuration.create_config()

print(configuration.get_item('COORDINATE', 'CHECK_MONEY_POS'))

configuration = MarketConfig()
print(configuration.money_coor)
print(type(configuration.buy_phase_coor))