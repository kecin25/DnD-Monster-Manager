"""
Author: C. Salinas
Date: 4/22/22
Purpose: Dnd monster stat tracker
"""

from Monster_Dic import mon_dic


# noinspection PyRedeclaration
class Monster:

    def __init__(self, monster_name="", monster_nickname=""):

        if monster_name == "" or monster_nickname == "":
            self.monster_name = ''
            self.monster_nickname = ''

            self.armor_class = 0
            self.speed = 0

            self.max_hit_points = 0
            self.cur_hit_points = 0

            self.str = 0
            self.dex = 0
            self.con = 0
            self.int = 0
            self.wis = 0
            self.cha = 0
        else:
            self.monster_name = monster_name
            self.monster_nickname = monster_nickname

            self.armor_class = mon_dic[monster_name]['Armor Class']
            self.speed = mon_dic[monster_name]['Speed']

            self.max_hit_points = mon_dic[monster_name]['Hit Points']
            self.cur_hit_points = mon_dic[monster_name]['Hit Points']

            self.str = mon_dic[monster_name]['STR']
            self.dex = mon_dic[monster_name]['DEX']
            self.con = mon_dic[monster_name]['CON']
            self.int = mon_dic[monster_name]['INT']
            self.wis = mon_dic[monster_name]['WIS']
            self.cha = mon_dic[monster_name]['CHA']

    def get_true_name(self):
        return self.monster_name

    def get_name(self):
        return self.monster_nickname

    def get_hp(self):
        return self.cur_hit_points

    def get_max_hp(self):
        return self.max_hit_points

    def get_str(self):
        return self.str

    def get_dex(self):
        return self.dex

    def get_con(self):
        return self.con

    def get_int(self):
        return self.int

    def get_wis(self):
        return self.wis

    def get_cha(self):
        return self.cha

    def get_ac(self):
        return self.armor_class

    def get_speed(self):
        return self.speed

    def take_damage(self, amount):
        self.cur_hit_points -= amount

    def heal(self, amount):
        self.cur_hit_points += amount

    def set_true_name(self, new_name):
        self.monster_name = new_name

    def set_name(self, new_name):
        self.monster_nickname = new_name

    def set_max_hp(self, new_max_hp):
        self.max_hit_points = int(new_max_hp)

    def set_hp(self, new_hp):
        self.cur_hit_points = int(new_hp)

    def set_str(self, new_str):
        self.str = int(new_str)

    def set_dex(self, new_dex):
        self.dex = int(new_dex)

    def set_con(self, new_con):
        self.con = int(new_con)

    def set_int(self, new_int):
        self.int = int(new_int)

    def set_wis(self, new_wis):
        self.wis = int(new_wis)

    def set_cha(self, new_cha):
        self.cha = int(new_cha)

    def set_ac(self, new_ac):
        self.armor_class = int(new_ac)

    def set_speed(self, new_speed):
        self.speed = int(new_speed)

