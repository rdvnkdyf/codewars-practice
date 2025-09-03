class Marine:
    def __init__(self, damage, armor):
        self.damage = damage
        self.armor = armor

class Marine_weapon_upgrade:
    def __init__(self, marine):
        self.marine = marine

    @property
    def damage(self):
        return self.marine.damage + 1

    @property
    def armor(self):
        return self.marine.armor

class Marine_armor_upgrade:
    def __init__(self, marine):
        self.marine = marine

    @property
    def damage(self):
        return self.marine.damage

    @property
    def armor(self):
        return self.marine.armor + 1