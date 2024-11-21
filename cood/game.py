"""
   the game call of oracle duty
"""
import sys
import tank


def main():
    thomas_tank = tank.Tank("German","tiger")
    rick_tank = tank.Tank("American","Sherman")
    rajat_tank = tank.Tank("British","Churchill")

    thomas_tank.accel(39)
    rick_tank.accel(28)
    rajat_tank.rotate_left(289)
    rajat_tank.accel(31)
    rajat_tank.shoot()
    thomas_tank.take_damage(62)
    rick_tank.take_damage(22)

    print(f"Thomas Tank health ({thomas_tank})")
    print(f"Rick Tank health ({rick_tank}")
    print(f"Rajat Tank health ({rajat_tank})")

    print(f"Team Tank health ({thomas_tank + rick_tank})")

    thomas_tank.tank_health = 100
    print(f"Thomas Tank now health ({thomas_tank})")



if __name__ == "__main__":
    main()
    sys.exit(0)