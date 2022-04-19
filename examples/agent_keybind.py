from valorant.utils.agent import Agent

if __name__ == '__main__':
    agent = Agent(first_ability_keybind="m")
    print(agent) #Agent(first_ability_keybind='m', second_ability_keybind='e', third_ability_keybind='c', ultimate_keybind='x', get_keybind='f', first_ability=0, second_ability=0, third_ability=0, ultimate_ability=1)
    agent.use_first_ability()
    agent.use_second_ability()
    agent.use_ultimate_ability()