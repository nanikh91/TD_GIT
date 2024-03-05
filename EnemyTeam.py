# EnemyTeam.py

from team import Team

class EnemyTeam(Team):
    def __init__(self, members, unit, damage, loot):
        super().__init__(members)
        self.__unit = unit
        self.__damage = damage
        self.__loot = loot

    def get_damage(self):
        return self.__damage

    def get_loot(self):
        return self.__loot

    def get_unit_type(self):
        return self.__unit

    def __iter__(self):
        return TeamIterator(self)