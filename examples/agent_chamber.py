from valorant.utils.helper import shortcut
from valorant.utils.agent import Chamber

if __name__ == '__main__':
    #chamber = Chamber()  # default keybind
    chamber = Chamber(first_ability_keybind="e", get_keybind="f") #custom keybind

    @shortcut("capslock", "Capslock Detected")
    def chambers_fake_tp():
        chamber.fake_tp()
        print(chamber)
        #Chamber(first_ability_keybind='e', second_ability_keybind='e', third_ability_keybind='c', ultimate_keybind='x', get_keybind='f', first_ability=0, second_ability=0, third_ability=0, ultimate_ability=1, fake_tp_keybind='ef')

    chambers_fake_tp()

    # access information of chamber first ability
    print(chamber.first_ability)
