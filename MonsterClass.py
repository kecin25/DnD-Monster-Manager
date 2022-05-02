"""
Author: C. Salinas
Date: 4/22/22
Purpose: Dnd monster stat tracker
"""

from Monster_Dic import mon_dic
import random


# noinspection PyRedeclaration
class Monster:

    def __init__(self, monster_name="", monster_nickname=""):
        if monster_name == "" or monster_nickname == "":
            self.monster_name = monster_name
            self.monster_nickname = monster_nickname

            self.size = None
            self.type = None
            self.align = None
            self.armor_class = 0
            self.max_hit_points = 0
            self.cur_hit_points = self.max_hit_points

            self.ground_speed = 0
            self.fly_speed = 0
            self.swim_speed = 0
            self.climb_speed = 0
            self.sav_throws = None
            self.skills = None
            self.wri = None
            self.senses = None
            self.languages = None
            self.cr = 0
            self.additional = None
            self.book_source = None

            self.str = 0
            self.dex = 0
            self.con = 0
            self.int = 0
            self.wis = 0
            self.cha = 0
        else:
            if monster_name not in list(mon_dic.keys()):
                print(f'ERROR\nMonster name: {monster_name} not found')

            self.monster_name = monster_name
            self.monster_nickname = monster_nickname

            self.size = mon_dic[monster_name]['Size']
            self.type = mon_dic[monster_name]['Type']
            self.align = mon_dic[monster_name]['Align.']

            self.armor_class = mon_dic[monster_name]['AC']

            self.hp_min = mon_dic[monster_name]['hp']
            self.hp_max = mon_dic[monster_name]['HP']
            self.max_hit_points = random.randrange(self.hp_min, self.hp_max)
            self.cur_hit_points = self.max_hit_points

            self.ground_speed = mon_dic[monster_name][
                'Speed']  # ["Ground"] #TODO: wait for updated monster_dic to uncomment
            #       self.fly_speed = mon_dic[monster_name]['Speed']["Fly"]
            #      self.swim_speed = mon_dic[monster_name]['Speed']["Swim"]
            #     self.climb_speed = mon_dic[monster_name]['Speed']["Climb"]
            self.sav_throws = mon_dic[monster_name]['Sav. Throws']
            self.skills = mon_dic[monster_name]['Skills']
            self.wri = mon_dic[monster_name]['WRI']
            self.senses = mon_dic[monster_name]['Senses']
            self.languages = mon_dic[monster_name]['Languages']
            self.cr = mon_dic[monster_name]['CR']
            self.additional = mon_dic[monster_name]['Additional']
            self.book_source = mon_dic[monster_name]['Book Source']

            self.str = mon_dic[monster_name]['STR']
            self.dex = mon_dic[monster_name]['DEX']
            self.con = mon_dic[monster_name]['CON']
            self.int = mon_dic[monster_name]['INT']
            self.wis = mon_dic[monster_name]['WIS']
            self.cha = mon_dic[monster_name]['CHA']

    # Get Methods
    def get_true_name(self):
        return self.monster_name

    def get_name(self):
        return self.monster_nickname

    def get_size(self):
        return self.size

    def get_type(self):
        return self.type

    def get_align(self):
        return self.align

    def get_ac(self):
        return self.armor_class

    def get_hp(self):
        return self.cur_hit_points

    def get_max_hp(self):
        return self.max_hit_points

    def get_ground_speed(self):
        return self.ground_speed

    def get_fly_speed(self):
        return self.ground_speed

    def get_swim_speed(self):
        return self.ground_speed

    def get_climb_speed(self):
        return self.ground_speed

    def get_sav_throws(self):
        return self.sav_throws

    def get_skills(self):
        return self.skills

    def get_wri(self):
        return self.wri

    def get_senses(self):
        return self.senses

    def get_languages(self):
        return self.languages

    def get_cr(self):
        return self.cr

    def get_additional(self):
        return self.additional

    def get_book_source(self):
        return self.book_source

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

    # Set methods
    def set_true_name(self, new_name):
        self.monster_name = new_name

    def set_name(self, new_name):
        self.monster_nickname = str(new_name).capitalize()

    def set_size(self, new_size):

        new_size = str(new_size).capitalize()
        sizes = 'Small', 'Medium', 'Large', 'Gargantuan'
        size_set = set(sizes)

        if new_size not in size_set:
            print(f'ERROR: {new_size} is not a valid size')

        else:
            self.monster_nickname = new_size

    def set_type(self, new_type):  # TODO: error proof
        self.type = new_type

    def set_align(self, new_align):  # TODO: error proof
        self.align = new_align

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

    def set_ground_speed(self, new_speed):
        self.ground_speed = int(new_speed)

    def set_fly_speed(self, new_speed):
        self.fly_speed = int(new_speed)

    def set_swim_speed(self, new_speed):
        self.swim_speed = int(new_speed)

    def set_climb_speed(self, new_speed):
        self.climb_speed = int(new_speed)

    def set_sav_throws(self, new_sav_throws):

        new_sav_throws = str(new_sav_throws).upper()
        throws = 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'
        throw_set = set(throws)

        if new_sav_throws not in throw_set:
            print(f'ERROR: {new_sav_throws} is not a valid entry')

        else:
            self.sav_throws = new_sav_throws

    def set_skills(self, new_skills):  # TODO: error proof
        self.skills = new_skills

    def set_wri(self, new_wri):  # TODO: error proof
        self.wri = new_wri

    def set_senses(self, new_senses):  # TODO: error proof
        self.senses = new_senses

    def set_languages(self, new_language):  # TODO: error proof
        self.languages = new_language

    def set_cr(self, new_cr):

        if isinstance(new_cr, float):
            self.cr = new_cr

        else:
            print(f'ERROR: {new_cr} is not a valid entry')

    def set_additional(self, new_add):
        self.additional = new_add

    def set_book_source(self, new_book_source):
        self.book_source = new_book_source

    def set_str(self, new_str):
        self.str = int(new_str)

    def set_dex(self, new_dex):
        self.dex = new_dex

    def set_con(self, new_con):
        self.con = new_con

    def set_int(self, new_int):
        self.int = new_int

    def set_wis(self, new_wis):
        self.wis = new_wis

    def set_cha(self, new_cha):
        self.cha = new_cha

    # Play methods
    def take_damage(self, amount):
        self.cur_hit_points -= amount

    def heal(self, amount):
        self.cur_hit_points += amount
