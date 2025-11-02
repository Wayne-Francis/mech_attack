from mech_type import Tank, Gunner, Bomber
from stat_blocks import *

if __name__ == "__main__":
    tank = Tank("Atlas")
    gunner = Gunner("Viper")
    bomber = Bomber("Nova")

    print(tank)
    tank.show_stats()
    print()
    print(gunner)
    gunner.show_stats()
    print()
    print(bomber)
    bomber.show_stats()