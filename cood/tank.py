"""
this module describes a tank class
"""

class Tank:

    def __init__(self,country,model):
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'x':0,"y":0}
        self._shells = 20
        self._health = 100

    def accel(self,increase):
        self._speed += increase
        return None

    def deccel(self,decrease):
        self._speed -= decrease
        return None

    def rotate_left(self,deg):
        self._direction -= deg % 360
        return None

    def rotate_right(self,deg):
        self._direction += deg %360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def reload(self):
        self._shells = 20
        return None

    def take_damage(self,amount):
        self._health -= amount
        return None

    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    def tank_health(self,amount):
        self._health = amount
        return None


    def get_shells(self):
        return self._shells

    def get_speed(self):
        return self._speed

    def get_direction(self):
        return self._direction

    def __str__(self):
        return str(self._health)

    def __add__(self, other):
        return self._health + other._health

    #tank_health = property(get_health,set_health)