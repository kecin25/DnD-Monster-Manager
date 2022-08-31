# DND stat Tracker
# Made by: Kevin Boudreaux and Carlos Salinas
# main.py last edited by Kevin Boudreaux on 5/18/2022

import random

import PySimpleGUI as gui

import Monster_Dic
from MonsterClass import Monster as mon

WIDTH = 80
HEIGHT = 20
BOX_SIZE = 5
TEXT_SIZE = 20

monster_class_list = []
monster_display_list = []

# TODO see if there is a System call to see how big screen is and base Width and Height off that.
#   Consider making the checkboxes another screen if not, way to make sure everything is visible.

# TODO add a third panel that displays the most recent selected monster's actions that it can take. Either
#  through text or picture

# monster_list is used to list the creatures being used, first is the Text to show what is in the boxes below Next is
# the List box of monsters that are in play Then there is an Input box and a button on the same row for the User to
# use
monster_list = [
    [
        gui.Text(text="Monsters", auto_size_text=True, justification="center", size=(int(WIDTH * 1.5), 3)),
    ],
    [
        gui.Checkbox(checkbox_color="black", text="Monster Type", key="-MONSTER TYPE-", enable_events=True,
                     pad=((0, 8), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Monster Name", key="-MONSTER NAME-", enable_events=True,
                     pad=((0, 8), (0, 0)),
                     default=True),
        gui.Checkbox(checkbox_color="black", text="HP", key="-HP-", enable_events=True, pad=((0, 48), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="HP/Max HP", key="-HP/MAX HP-", enable_events=True, default=True,
                     pad=((0, 14), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Max HP", key="-MAX HP-", enable_events=True,
                     pad=((0, 8), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Ground Speed", key="-SPEED-", enable_events=True,
                     pad=((0, 8), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Swim Speed", key="-SWIM SPEED-", enable_events=True,
                     pad=((0, 8), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Fly Speed", key="-FLY SPEED-", enable_events=True,
                     pad=((0, 29), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Climb Speed", key="-CLIMB SPEED-", enable_events=True,
                     pad=((0, 60), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Condition Immunities", key="-CON IMMU-", enable_events=True,
                     pad=((0, 19), (0, 0))),
    ],
    [
        gui.Checkbox(checkbox_color="black", text="Armor Class", key="-AC-", enable_events=True, default=True,
                     pad=((0, 15), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="STR", key="-STR-", enable_events=True, pad=((0, 68), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="DEX", key="-DEX-", enable_events=True, pad=((0, 41), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="CON", key="-CON-", enable_events=True, pad=((0, 55), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="INT", key="-INT-", enable_events=True, pad=((0, 36), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="WIS", key="-WIS-", enable_events=True, pad=((0, 66), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="CHA", key="-CHA-", enable_events=True, pad=((0, 54), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Resistances", key="-RES-", enable_events=True,
                     pad=((0, 16), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Damage Immunities", key="-DMG IMMU-", enable_events=True,
                     pad=((0, 19), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Weaknesses", key="-WEAK-", enable_events=True,
                     pad=((0, 24), (0, 0))),

    ],
    [

        gui.Checkbox(checkbox_color="black", text="Size", key="-SIZE-", enable_events=True, pad=((0, 61), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Type", key="-TYPE-", enable_events=True, pad=((0, 65), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Alignment", key="-ALIGN-", enable_events=True,
                     pad=((0, 8), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Saving Throws", key="-ST-", enable_events=True,
                     pad=((0, 0), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Skills", key="-SKILLS-", enable_events=True,
                     pad=((0, 23), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Senses", key="-SENSES-", enable_events=True,
                     pad=((0, 47), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Languages", key="-LAN-", enable_events=True,
                     pad=((0, 18), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="CR", key="-CR-", enable_events=True, pad=((0, 70), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Additional", key="-ADDI-", enable_events=True,
                     pad=((0, 72), (0, 0))),
        gui.Checkbox(checkbox_color="black", text="Book Source", key="-BS-", enable_events=True),
    ],
    [
        gui.Listbox(values=monster_display_list, enable_events=True, size=(int(WIDTH * 1.2), HEIGHT),
                    select_mode='multiple', key="-MONSTERS-", font="Courier", horizontal_scroll=True,
                    auto_size_text=True)
    ],
    [
        gui.Checkbox(text="Saving Throw", enable_events=True, key="-SAVING THROW-", default=False),
        gui.Combo(list(["STR", "DEX", "CON", "INT", "WIS", "CHA"]), default_value="Str", readonly=True,
                  disabled=True, key="-SAVING THROW TYPE-"),
        gui.In(disabled=True, size=(3, 0), key="-SAVING THROW AMOUNT-"),
        gui.Text(text="Damage Type", pad=((30, 0), (0, 0))),
        gui.Combo(list(
            ["ACID", "BLUDGEONING", "COLD", "FIRE", "FORCE", "LIGHTNING", "NECROTIC", "PIERCING", "POISON",
             "PSYCHIC", "RADIANT", "SLASHING", "THUNDER"]), default_value="SLASHING", readonly=True,
            key="-DAMAGE TYPE-"),
        gui.Text(text="Damage Amount", pad=((30, 0), (0, 0))),
        gui.In(size=(int((WIDTH - 20) / 4), 0), enable_events=True, key="-INPUT-"),
        gui.Button(button_text="Submit", size=(20, 1), bind_return_key=True, key="-SUBMIT BUTTON-"),
    ]
]

# log_column is used to display what actions were recently taken by the user and stores buttons for Add Monster,
# Save, and Load
log_column = [
    [
        gui.Text(text="Action Log", auto_size_text=True, justification="center", size=(WIDTH, 3))
    ],
    [
        gui.Listbox(values=[], size=(WIDTH, int(HEIGHT * 1.5)), key="-LOG-", expand_x=True, expand_y=True, )
    ],
    [
        gui.Button(button_text="Add", size=(int(WIDTH / 2), 1), key="-ADD-"),
        # Input is used because FileBrowse does not cause events to trigger, so Input is used as a trigger when
        # FileBrowse is clicked
        gui.Input(visible=False, enable_events=True, key="-LOAD-"),
        gui.FileBrowse(button_text="Load", size=(int(WIDTH / 2), 1), key="-LOAD_FILE_NAME-",
                       file_types=[("Text", "*.txt"), ("ALL Files", ".*")], change_submits=True)
    ],
    [
        gui.Button(button_text="Edit", auto_size_button=True, size=(int(WIDTH / 2), 1), key="-EDIT-"),
        # Input is used because FileSaveAs does not cause events to trigger, so Input is used as a trigger when
        # FileSaveAs is clicked
        gui.Input(visible=False, enable_events=True, key="-SAVE-"),
        gui.FileSaveAs(button_text="Save", auto_size_button=True, size=(int(WIDTH / 2), 1), key="-SAVE_FILE_NAME-",
                       default_extension=".txt")

    ]

]

layout_default = [
    [
        gui.Column(monster_list),
        gui.VerticalSeparator(color="Black"),
        gui.Column(log_column),
    ]
]

Log = []
selected_checkboxes = [False, True, False, True, False, False, False, False, False, False, True, False, False, False,
                       False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                       False, False]


# Window used when adding monsters to the manager It has its own function because PySimpleGUI does not allow a window
# to be open and closed The workaround is making a new copy of the layout every time the function is called
# TODO: add boxes for Size, Type, Alignment, Saving throws, Skills, immunities, resistances,  weaknesses, Senses,
#  Languages, CR, Additional, Book Source
def make_add_monster_window():
    monster_maker = \
        [
            [
                gui.Text(text="Monster Name", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-NAME-")
            ],
            [
                gui.Text(text="Monster Type", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.Combo(list(Monster_Dic.mon_dic.keys()), default_value="", key="-TYPE-", auto_size_text=True,
                          size=20,
                          enable_events=True)
            ],
            [
                gui.Text(text="Number of copies", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-AMOUNT-", size=BOX_SIZE),
                gui.Text(text="(Will have the name of the monster you give and a number behind it starting at 1)",
                         auto_size_text=True)
            ],
            [
                gui.Text(text="Armor Class", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-AC-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Ground Speed", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-SPEED-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Fly Speed", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-FLY SPEED-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Swim Speed", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-SWIM SPEED-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Climb Speed", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-CLIMB SPEED-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Max HP", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-MAX_HP-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Current HP", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-HP-", size=BOX_SIZE),
                gui.Text(text=" (leave blank if starting at Max HP)", auto_size_text=True)
            ],
            [
                gui.Text(text="Strength", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-STR-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Dexterity", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-DEX-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Constitution", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-CON-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Intelligence", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-INT-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Wisdom", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-WIS-", size=BOX_SIZE)
            ],
            [
                gui.Text(text="Charisma", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-CHA-", size=BOX_SIZE),
                gui.Text(size=70 - TEXT_SIZE - BOX_SIZE),
                gui.Button(button_text="Accept", auto_size_button=True, enable_events=True, key="-ACCEPT-",
                           bind_return_key=True),
                gui.Button(button_text="Cancel", auto_size_button=True, enable_events=True, key="-CANCEL-")
            ],
        ]
    layout_add_monster = [[gui.Column(monster_maker)]]
    return gui.Window("Add Monster", layout_add_monster)


# TODO: add boxes for Size, Type, Alignment, Saving throws, Skills, immunities, resistances,  weaknesses, Senses,
#  Languages, CR, Additional, Book Source
def make_edit_monster_window(name, ac, speed, fly_speed, swim_speed, climb_speed, max_hp, hp, str, dex, con, int, wis, cha):
    monster_editor = \
        [
            [
                gui.Text(text="Monster Name", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-NAME-", default_text=name)
            ],
            [
                gui.Text(text="Armor Class", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-AC-", size=BOX_SIZE, default_text=ac)
            ],
            [
                gui.Text(text="Speed", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-SPEED-", size=BOX_SIZE, default_text=speed)
            ],
            [
                gui.Text(text="Fly Speed", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-FLY SPEED-", size=BOX_SIZE, default_text=fly_speed)
            ],
            [
                gui.Text(text="Swim Speed", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-SWIM SPEED-", size=BOX_SIZE, default_text=swim_speed)
            ],
            [
                gui.Text(text="Climb Speed", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-CLIMB SPEED-", size=BOX_SIZE, default_text=climb_speed)
            ],
            [
                gui.Text(text="Max HP", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-MAX_HP-", size=BOX_SIZE, default_text=max_hp)
            ],
            [
                gui.Text(text="Current HP", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-HP-", size=BOX_SIZE, default_text=hp),
            ],
            [
                gui.Text(text="Strength", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-STR-", size=BOX_SIZE, default_text=str)
            ],
            [
                gui.Text(text="Dexterity", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-DEX-", size=BOX_SIZE, default_text=dex)
            ],
            [
                gui.Text(text="Constitution", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-CON-", size=BOX_SIZE, default_text=con)
            ],
            [
                gui.Text(text="Intelligence", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-INT-", size=BOX_SIZE, default_text=int)
            ],
            [
                gui.Text(text="Wisdom", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-WIS-", size=BOX_SIZE, default_text=wis)
            ],
            [
                gui.Text(text="Charisma", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-CHA-", size=BOX_SIZE, default_text=cha),
                gui.Text(size=70 - TEXT_SIZE - BOX_SIZE),
                gui.Button(button_text="Accept", auto_size_button=True, enable_events=True, key="-ACCEPT-"),
                gui.Button(button_text="Cancel", auto_size_button=True, enable_events=True, key="-CANCEL-")
            ],
        ]
    layout_edit_monster = [[gui.Column(monster_editor)]]
    return gui.Window("Add Monster", layout_edit_monster)


# update_monster_menu is a function that goes through the display list and updates the stats being shown,
# is used when changing any stat or when adding/removing stats that the user wants to see

def update_monster_menu():
    # longest is used to find the longest character length of all possible strings in the monster_class_list
    longest = [0] * 30
    temp_names = []

    # To keep all for loops running each time, they will only run when their checkbox has been selected
    if selected_checkboxes[0]:
        for x in monster_class_list:
            temp_names.append(x.get_true_name())
        if len(monster_class_list) != 0:
            longest[0] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[1]:
        for x in monster_class_list:
            temp_names.append(x.get_name())
        if len(monster_class_list) != 0:
            longest[1] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[2]:
        for x in monster_class_list:
            temp_names.append(str(x.get_hp()))
        if len(monster_class_list) != 0:
            longest[2] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[3]:
        for x in monster_class_list:
            temp_names.append(str(x.get_hp()) + str(x.get_max_hp()))
        if len(monster_class_list) != 0:
            longest[3] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[4]:
        for x in monster_class_list:
            temp_names.append(str(x.get_max_hp()))
        if len(monster_class_list) != 0:
            longest[4] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[5]:
        for x in monster_class_list:
            temp_names.append(str(x.get_ground_speed()))
        if len(monster_class_list) != 0:
            longest[5] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[6]:
        for x in monster_class_list:
            temp_names.append(str(x.get_fly_speed()))
        if len(monster_class_list) != 0:
            longest[6] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[7]:
        for x in monster_class_list:
            temp_names.append(str(x.get_swim_speed()))
        if len(monster_class_list) != 0:
            longest[7] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[8]:
        for x in monster_class_list:
            temp_names.append(str(x.get_climb_speed()))
        if len(monster_class_list) != 0:
            longest[8] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[9]:
        for x in monster_class_list:
            temp_names.append(str(x.get_condition_immunities()))
        if len(monster_class_list) != 0:
            longest[9] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[10]:
        for x in monster_class_list:
            temp_names.append(str(x.get_ac()))
        if len(monster_class_list) != 0:
            longest[10] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[11]:
        for x in monster_class_list:
            temp_names.append(str(x.get_str()))
        if len(monster_class_list) != 0:
            longest[11] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[12]:
        for x in monster_class_list:
            temp_names.append(str(x.get_dex()))
        if len(monster_class_list) != 0:
            longest[12] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[13]:
        for x in monster_class_list:
            temp_names.append(str(x.get_con()))
        if len(monster_class_list) != 0:
            longest[13] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[14]:
        for x in monster_class_list:
            temp_names.append(str(x.get_int()))
        if len(monster_class_list) != 0:
            longest[14] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[15]:
        for x in monster_class_list:
            temp_names.append(str(x.get_wis()))
        if len(monster_class_list) != 0:
            longest[15] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[16]:
        for x in monster_class_list:
            temp_names.append(str(x.get_cha()))
        if len(monster_class_list) != 0:
            longest[16] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[17]:
        for x in monster_class_list:
            temp_names.append(str(x.get_resistances()))
        if len(monster_class_list) != 0:
            longest[17] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[18]:
        for x in monster_class_list:
            temp_names.append(str(x.get_damage_immunities()))
        if len(monster_class_list) != 0:
            longest[18] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[19]:
        for x in monster_class_list:
            temp_names.append(str(x.get_weaknesses()))
        if len(monster_class_list) != 0:
            longest[19] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[20]:
        for x in monster_class_list:
            temp_names.append(str(x.get_size()))
        if len(monster_class_list) != 0:
            longest[20] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[21]:
        for x in monster_class_list:
            temp_names.append(str(x.get_type()))
        if len(monster_class_list) != 0:
            longest[21] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[22]:
        for x in monster_class_list:
            temp_names.append(str(x.get_align()))
        if len(monster_class_list) != 0:
            longest[22] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[23]:
        for x in monster_class_list:
            temp_names.append(str(x.get_sav_throws()))
        if len(monster_class_list) != 0:
            longest[23] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[24]:
        for x in monster_class_list:
            temp_names.append(str(x.get_skills()))
        if len(monster_class_list) != 0:
            longest[24] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[25]:
        for x in monster_class_list:
            temp_names.append(str(x.get_senses()))
        if len(monster_class_list) != 0:
            longest[25] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[26]:
        for x in monster_class_list:
            temp_names.append(str(x.get_languages()))
        if len(monster_class_list) != 0:
            longest[26] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[27]:
        for x in monster_class_list:
            temp_names.append(str(x.get_cr()))
        if len(monster_class_list) != 0:
            longest[27] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[28]:
        for x in monster_class_list:
            temp_names.append(str(x.get_additional()))
        if len(monster_class_list) != 0:
            longest[28] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[29]:
        for x in monster_class_list:
            temp_names.append(str(x.get_book_source()))
        if len(monster_class_list) != 0:
            longest[29] = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    # This series of nested for loops prints the desired output given the selected_checkboxes and longest strings
    for num in range(0, len(monster_class_list)):
        if num >= len(monster_display_list):
            monster_display_list.append("")
        monster_display_list[num] = ""
        if selected_checkboxes[0]:
            monster_display_list[num] += monster_class_list[num].get_true_name()
            for i in range(len(monster_class_list[num].get_true_name()), longest[0]):
                monster_display_list[num] += " "
        if selected_checkboxes[1]:
            monster_display_list[num] += monster_class_list[num].get_name()
            for i in range(len(monster_class_list[num].get_name()), longest[1]):
                monster_display_list[num] += " "
        if selected_checkboxes[2]:
            monster_display_list[num] += "HP: " + str(monster_class_list[num].get_hp())
            for i in range(len(str(monster_class_list[num].get_hp())), longest[2]):
                monster_display_list[num] += " "
        if selected_checkboxes[3]:
            monster_display_list[num] += "HP/Max HP: " + str(monster_class_list[num].get_hp()) + "/" + str(
                monster_class_list[num].get_max_hp())
            for i in range(len(str(monster_class_list[num].get_hp())) + len(str(monster_class_list[num].get_max_hp())),
                           longest[3]):
                monster_display_list[num] += " "
        if selected_checkboxes[4]:
            monster_display_list[num] += "Max HP: " + str(monster_class_list[num].get_max_hp())
            for i in range(len(str(monster_class_list[num].get_max_hp())), longest[4]):
                monster_display_list[num] += " "
        if selected_checkboxes[5]:
            monster_display_list[num] += "Ground Speed: " + str(monster_class_list[num].get_ground_speed())
            for i in range(len(str(monster_class_list[num].get_ground_speed())), longest[5]):
                monster_display_list[num] += " "
        if selected_checkboxes[6]:
            monster_display_list[num] += "Fly Speed: " + str(monster_class_list[num].get_fly_speed())
            for i in range(len(str(monster_class_list[num].get_fly_speed())), longest[6]):
                monster_display_list[num] += " "
        if selected_checkboxes[7]:
            monster_display_list[num] += "Swim Speed: " + str(monster_class_list[num].get_swim_speed())
            for i in range(len(str(monster_class_list[num].get_swim_speed())), longest[7]):
                monster_display_list[num] += " "
        if selected_checkboxes[8]:
            monster_display_list[num] += "Climb Speed: " + str(monster_class_list[num].get_climb_speed())
            for i in range(len(str(monster_class_list[num].get_climb_speed())), longest[8]):
                monster_display_list[num] += " "
        if selected_checkboxes[9]:
            monster_display_list[num] += "Condition Immunities: " + str(
                monster_class_list[num].get_condition_immunities())
            for i in range(len(str(monster_class_list[num].get_condition_immunities())), longest[9]):
                monster_display_list[num] += " "
        if selected_checkboxes[10]:
            monster_display_list[num] += "AC: " + str(monster_class_list[num].get_ac())
            for i in range(len(str(monster_class_list[num].get_ac())), longest[10]):
                monster_display_list[num] += " "
        if selected_checkboxes[11]:
            monster_display_list[num] += "Str: " + str(monster_class_list[num].get_str())
            for i in range(len(str(monster_class_list[num].get_str())), longest[11]):
                monster_display_list[num] += " "
        if selected_checkboxes[12]:
            monster_display_list[num] += "Dex: " + str(monster_class_list[num].get_dex())
            for i in range(len(str(monster_class_list[num].get_dex())), longest[12]):
                monster_display_list[num] += " "
        if selected_checkboxes[13]:
            monster_display_list[num] += "Con: " + str(monster_class_list[num].get_con())
            for i in range(len(str(monster_class_list[num].get_con())), longest[13]):
                monster_display_list[num] += " "
        if selected_checkboxes[14]:
            monster_display_list[num] += "Int: " + str(monster_class_list[num].get_int())
            for i in range(len(str(monster_class_list[num].get_int())), longest[14]):
                monster_display_list[num] += " "
        if selected_checkboxes[15]:
            monster_display_list[num] += "Wis: " + str(monster_class_list[num].get_wis())
            for i in range(len(str(monster_class_list[num].get_wis())), longest[15]):
                monster_display_list[num] += " "
        if selected_checkboxes[16]:
            monster_display_list[num] += "Cha: " + str(monster_class_list[num].get_cha())
            for i in range(len(str(monster_class_list[num].get_cha())), longest[16]):
                monster_display_list[num] += " "
        if selected_checkboxes[17]:
            monster_display_list[num] += "Resistances: " + str(monster_class_list[num].get_resistances())
            for i in range(len(str(monster_class_list[num].get_resistances())), longest[17]):
                monster_display_list[num] += " "
        if selected_checkboxes[18]:
            monster_display_list[num] += "Damage Immunities: " + str(monster_class_list[num].get_damage_immunities())
            for i in range(len(str(monster_class_list[num].get_damage_immunities())), longest[18]):
                monster_display_list[num] += " "
        if selected_checkboxes[19]:
            monster_display_list[num] += "Weaknesses: " + str(monster_class_list[num].get_weaknesses())
            for i in range(len(str(monster_class_list[num].get_weaknesses())), longest[19]):
                monster_display_list[num] += " "
        if selected_checkboxes[20]:
            monster_display_list[num] += "Size: " + str(monster_class_list[num].get_size())
            for i in range(len(str(monster_class_list[num].get_size())), longest[20]):
                monster_display_list[num] += " "
        if selected_checkboxes[21]:
            monster_display_list[num] += "Type: " + str(monster_class_list[num].get_type())
            for i in range(len(str(monster_class_list[num].get_type())), longest[21]):
                monster_display_list[num] += " "
        if selected_checkboxes[22]:
            monster_display_list[num] += "Alignment: " + str(monster_class_list[num].get_align())
            for i in range(len(str(monster_class_list[num].get_align())), longest[22]):
                monster_display_list[num] += " "
        if selected_checkboxes[23]:
            monster_display_list[num] += "Saving Throws: " + str(monster_class_list[num].get_sav_throws())
            for i in range(len(str(monster_class_list[num].get_sav_throws())), longest[23]):
                monster_display_list[num] += " "
        if selected_checkboxes[24]:
            monster_display_list[num] += "Skills: " + str(monster_class_list[num].get_skills())
            for i in range(len(str(monster_class_list[num].get_skills())), longest[24]):
                monster_display_list[num] += " "
        if selected_checkboxes[25]:
            monster_display_list[num] += "Senses: " + str(monster_class_list[num].get_senses())
            for i in range(len(str(monster_class_list[num].get_senses())), longest[25]):
                monster_display_list[num] += " "
        if selected_checkboxes[26]:
            monster_display_list[num] += "Languages: " + str(monster_class_list[num].get_languages())
            for i in range(len(str(monster_class_list[num].get_languages())), longest[26]):
                monster_display_list[num] += " "
        if selected_checkboxes[27]:
            monster_display_list[num] += "CR: " + str(monster_class_list[num].get_cr())
            for i in range(len(str(monster_class_list[num].get_cr())), longest[27]):
                monster_display_list[num] += " "
        if selected_checkboxes[28]:
            monster_display_list[num] += "Additional: " + str(monster_class_list[num].get_additional())
            for i in range(len(str(monster_class_list[num].get_additional())), longest[28]):
                monster_display_list[num] += " "
        if selected_checkboxes[29]:
            monster_display_list[num] += "Book Source: " + str(monster_class_list[num].get_book_source())
            for i in range(len(str(monster_class_list[num].get_book_source())), longest[29]):
                monster_display_list[num] += " "

    default_window["-MONSTERS-"].update(monster_display_list)


default_window = gui.Window("Monster stat Tracker", layout_default, resizable=True, grab_anywhere_using_control=True)
while True:
    event, values = default_window.read()
    # selected_monsters is used to get the monsters the user selected in the form of a list
    selected_monsters = []
    # invalid_input is used when dealing with saving throws or dealing damage to the monsters
    invalid_input = False
    if event == "Exit" or event == gui.WIN_CLOSED:
        break

    # Add is ran when the ADD button is clicked
    # TODO: add boxes for Size, Type, Alignment, Saving throws, Skills, immunities, resistances,  weaknesses, Senses,
    #  Languages, CR, Additional, Book Source
    if event == "-ADD-":
        # makes a secondary window to get all the information needed
        monster_maker_window = make_add_monster_window()

        while True:
            adding_event, adding_values = monster_maker_window.read()
            if adding_event == "-CANCEL-" or adding_event == gui.WIN_CLOSED:
                monster_maker_window.close()
                break
            # If the user wants to use a default Monster then they can select the type and all the boxes, except for
            # name and amount will autofill to the default values for that monster
            if adding_event == "-TYPE-":
                mn = mon(adding_values["-TYPE-"], adding_values["-NAME-"])
                monster_maker_window["-AC-"].update(mn.get_ac())
                monster_maker_window["-SPEED-"].update(mn.get_ground_speed())
                monster_maker_window["-FLY SPEED-"].update(mn.get_fly_speed())
                monster_maker_window["-SWIM SPEED-"].update(mn.get_swim_speed())
                monster_maker_window["-CLIMB SPEED-"].update(mn.get_climb_speed())
                monster_maker_window["-MAX_HP-"].update(mn.get_max_hp())
                monster_maker_window["-HP-"].update(mn.get_hp())
                monster_maker_window["-STR-"].update(mn.get_str())
                monster_maker_window["-DEX-"].update(mn.get_dex())
                monster_maker_window["-CON-"].update(mn.get_con())
                monster_maker_window["-INT-"].update(mn.get_int())
                monster_maker_window["-WIS-"].update(mn.get_wis())
                monster_maker_window["-CHA-"].update(mn.get_cha())

            # Once the accept button has been clicked, the program will create a new monster to add to the manager
            # based off the data given from the user
            if adding_event == "-ACCEPT-":
                if adding_values["-NAME-"] == "":
                    gui.popup("You must give a name to the monster")
                else:
                    if adding_values["-AMOUNT-"] == "" or int(adding_values["-AMOUNT-"]) <= 0:
                        gui.popup("Number of Copies must be at least 1")
                        break
                    for x in range(1, int(adding_values["-AMOUNT-"]) + 1):
                        mn = mon(adding_values["-TYPE-"], str(adding_values["-NAME-"] + " " + str(x)))
                        mn.set_ac(adding_values["-AC-"])
                        mn.set_ground_speed(adding_values["-SPEED-"])
                        mn.set_fly_speed(adding_values["-FLY SPEED-"])
                        mn.set_swim_speed(adding_values["-SWIM SPEED-"])
                        mn.set_climb_speed(adding_values["-CLIMB SPEED-"])

                        if mn.get_max_hp() == 0:
                            mn.set_max_hp(adding_values["-MAX_HP-"])
                            if adding_values["-HP-"] == "":
                                mn.set_hp(adding_values["-MAX_HP-"])
                            else:

                                mn.set_hp(adding_values["-HP-"])
                        mn.set_str(adding_values["-STR-"])
                        mn.set_dex(adding_values["-DEX-"])
                        mn.set_con(adding_values["-CON-"])
                        mn.set_int(adding_values["-INT-"])
                        mn.set_wis(adding_values["-WIS-"])
                        mn.set_cha(adding_values["-CHA-"])
                        monster_class_list.append(mn)
                    update_monster_menu()
                    monster_maker_window.close()

    # Edit is used when wanting to change the stats of the selected monster(s)
    # TODO: add boxes for Size, Type, Alignment, Saving throws, Skills, immunities, resistances,  weaknesses, Senses,
    #  Languages, CR, Additional, Book Source
    if event == "-EDIT-":
        selected_monsters = values["-MONSTERS-"]
        # Nested for loop is used to edit each monster in the selected list, the user will be able to edit one monster
        # at a time until all the selected monsters have been processed
        for monster_name in selected_monsters:
            for x in range(0, len(monster_display_list)):
                if monster_display_list[x] == monster_name:
                    monster_maker_window = make_edit_monster_window(monster_class_list[x].get_name(),
                                                                    monster_class_list[x].get_ac(),
                                                                    monster_class_list[x].get_ground_speed(),
                                                                    monster_class_list[x].get_fly_speed(),
                                                                    monster_class_list[x].get_swim_speed(),
                                                                    monster_class_list[x].get_climb_speed(),
                                                                    monster_class_list[x].get_max_hp(),
                                                                    monster_class_list[x].get_hp(),
                                                                    monster_class_list[x].get_str(),
                                                                    monster_class_list[x].get_dex(),
                                                                    monster_class_list[x].get_con(),
                                                                    monster_class_list[x].get_int(),
                                                                    monster_class_list[x].get_wis(),
                                                                    monster_class_list[x].get_cha())

                    while True:
                        editing_event, editing_values = monster_maker_window.read()
                        if editing_event == "-CANCEL-" or editing_event == gui.WIN_CLOSED:
                            monster_maker_window.close()
                            break
                        # When the user clicks the Accept button, all the stats in the boxes will replace the
                        # given monster's current stats
                        if editing_event == "-ACCEPT-":
                            if editing_values["-NAME-"] == "":
                                gui.popup("You must give a name to the monster")
                            else:
                                monster_class_list[x].set_name(editing_values["-NAME-"])
                                monster_class_list[x].set_ac(editing_values["-AC-"])
                                monster_class_list[x].set_ground_speed(editing_values["-SPEED-"])
                                monster_class_list[x].set_fly_speed(editing_values["-FLY SPEED-"])
                                monster_class_list[x].set_swim_speed(editing_values["-SWIM SPEED-"])
                                monster_class_list[x].set_climb_speed(editing_values["-CLIMB SPEED-"])
                                monster_class_list[x].set_max_hp(editing_values["-MAX_HP-"])
                                if editing_values["-HP-"] == "":
                                    monster_class_list[x].set_hp(editing_values["-MAX_HP-"])
                                else:
                                    monster_class_list[x].set_hp(editing_values["-HP-"])
                                monster_class_list[x].set_str(editing_values["-STR-"])
                                monster_class_list[x].set_dex(editing_values["-DEX-"])
                                monster_class_list[x].set_con(editing_values["-CON-"])
                                monster_class_list[x].set_int(editing_values["-INT-"])
                                monster_class_list[x].set_wis(editing_values["-WIS-"])
                                monster_class_list[x].set_cha(editing_values["-CHA-"])
                            monster_maker_window.close()

        update_monster_menu()

    # Load is used when the user wants to use a pre-made file
    if event == "-LOAD-":
        file_name = values["-LOAD_FILE_NAME-"]
        monster_display_list = []
        monster_class_list = []
        error = True
        reset_view_point = False
        with open(file_name, "r") as file:
            contents = file.readlines()
            for x in range(0, len(contents)):
                if contents[x].endswith("\n"):
                    contents[x] = contents[x][:len(contents[x]) - 1]
            while len(contents) != 0:
                error_line = 1
                mn = mon()
                mn.set_true_name(contents[0])
                contents.pop(0)
                error_line += 1
                mn.set_name(contents[0])
                contents.pop(0)
                error_line += 1
                numeric_boolean = contents[0].isnumeric()
                # numeric_boolean is to make sure the file has the correct datatype to prevent the program crashing
                if numeric_boolean:
                    mn.set_hp(int(contents[0]))
                    contents.pop(0)
                    error_line += 1
                    numeric_boolean = contents[0].isnumeric()
                    if numeric_boolean:
                        mn.set_max_hp(int(contents[0]))
                        contents.pop(0)
                        error_line += 1
                        numeric_boolean = contents[0].isnumeric()
                        if numeric_boolean:
                            mn.set_ground_speed(int(contents[0]))
                            contents.pop(0)
                            error_line += 1
                            numeric_boolean = contents[0].isnumeric()
                            if numeric_boolean:
                                mn.set_fly_speed(int(contents[0]))
                                contents.pop(0)
                                error_line += 1
                                numeric_boolean = contents[0].isnumeric()
                                if numeric_boolean:
                                    mn.set_swim_speed(int(contents[0]))
                                    contents.pop(0)
                                    error_line += 1
                                    numeric_boolean = contents[0].isnumeric()
                                    if numeric_boolean:
                                        mn.set_climb_speed(int(contents[0]))
                                        contents.pop(0)
                                        error_line += 1
                                        if contents[0].isalpha() or contents[0] is None:
                                            if contents[0] != "None":
                                                mn.set_condition_immunities(int(contents[0]))
                                            contents.pop(0)
                                            error_line += 1
                                            numeric_boolean = contents[0].isnumeric()
                                            if numeric_boolean:
                                                mn.set_ac(int(contents[0]))
                                                contents.pop(0)
                                                error_line += 1
                                                numeric_boolean = contents[0].isnumeric()
                                                if numeric_boolean:
                                                    mn.set_str(int(contents[0]))
                                                    contents.pop(0)
                                                    error_line += 1
                                                    numeric_boolean = contents[0].isnumeric()
                                                    if numeric_boolean:
                                                        mn.set_dex(int(contents[0]))
                                                        contents.pop(0)
                                                        error_line += 1
                                                        numeric_boolean = contents[0].isnumeric()
                                                        if numeric_boolean:
                                                            mn.set_con(int(contents[0]))
                                                            contents.pop(0)
                                                            error_line += 1
                                                            numeric_boolean = contents[0].isnumeric()
                                                            if numeric_boolean:
                                                                mn.set_int(int(contents[0]))
                                                                contents.pop(0)
                                                                error_line += 1
                                                                numeric_boolean = contents[0].isnumeric()
                                                                if numeric_boolean:
                                                                    mn.set_wis(int(contents[0]))
                                                                    contents.pop(0)
                                                                    error_line += 1
                                                                    numeric_boolean = contents[0].isnumeric()
                                                                    if numeric_boolean:
                                                                        mn.set_cha(int(contents[0]))
                                                                        contents.pop(0)
                                                                        if contents[0].isalpha() or contents[0] is None:
                                                                            if contents[0] != "None":
                                                                                mn.set_resistances(contents[0])
                                                                            contents.pop(0)
                                                                            error_line += 1
                                                                            reset_view_point = True
                if reset_view_point:
                    if contents[0].isalpha() or contents[0] is None:
                        if contents[0] != "None":
                            mn.set_damage_immunities(contents[0])
                        contents.pop(0)
                        error_line += 1
                        if contents[0].isalpha() or contents[0] is None:
                            if contents[0] != "None":
                                mn.set_weaknesses(contents[0])
                            contents.pop(0)
                            error_line += 1
                            if contents[0].isalpha() or contents[0] is None:
                                if contents[0] != "None":
                                    mn.set_size(contents[0])
                                contents.pop(0)
                                error_line += 1
                                if contents[0].isalpha() or contents[0] is None:
                                    if contents[0] != "None":
                                        mn.set_type(contents[0])
                                    contents.pop(0)
                                    error_line += 1
                                    if contents[0].isalpha() or contents[0] is None:
                                        if contents[0] != "None":
                                            mn.set_align(contents[0])
                                        contents.pop(0)
                                        error_line += 1
                                        if contents[0] != "None":
                                            mn.set_sav_throws(contents[0])
                                        contents.pop(0)
                                        error_line += 1
                                        if contents[0] != "None":
                                            mn.set_skills(contents[0])
                                        contents.pop(0)
                                        error_line += 1
                                        if contents[0] != "None":
                                            mn.set_senses(contents[0])
                                        contents.pop(0)
                                        error_line += 1
                                        if contents[0] != "None":
                                            mn.set_languages(contents[0])
                                        contents.pop(0)
                                        error_line += 1
                                        temp = contents[0]
                                        numeric_boolean = temp.replace('.', '', 1).isdigit()
                                        if numeric_boolean:
                                            mn.set_cr(float(contents[0]))
                                            contents.pop(0)
                                            error_line += 1
                                            if contents[0] != "None":
                                                mn.set_additional(contents[0])
                                            contents.pop(0)
                                            error_line += 1
                                            if contents[0] != "None":
                                                mn.set_book_source(contents[0])
                                            contents.pop(0)
                                            error_line += 1
                                            monster_class_list.append(mn)
                                            error = False
                if error:
                    Log.append("File Corrupted, non numeric or incorrect value on line " + str(error_line))
                    break
        update_monster_menu()
        if numeric_boolean:
            Log.append("Loaded " + file_name)
        Log.append(
            "------------------------------------------------------------------------------------------" +
            "-------------------------------------------------------------------------------------------")
        default_window["-LOG-"].update(Log)

    # Save saves all the current monsters and their stats to a txt file at the location the user gives
    if event == "-SAVE-":
        file_name = values["-SAVE_FILE_NAME-"]
        with open(file_name, "w") as file:
            data_to_save = []
            for x in range(0, len(monster_class_list)):
                data_to_save.append(monster_class_list[x].get_true_name())
                data_to_save.append(monster_class_list[x].get_name())
                data_to_save.append(monster_class_list[x].get_hp())
                data_to_save.append(monster_class_list[x].get_max_hp())
                data_to_save.append(monster_class_list[x].get_ground_speed())
                data_to_save.append(monster_class_list[x].get_fly_speed())
                data_to_save.append(monster_class_list[x].get_swim_speed())
                data_to_save.append(monster_class_list[x].get_climb_speed())
                data_to_save.append(monster_class_list[x].get_condition_immunities())
                data_to_save.append(monster_class_list[x].get_ac())
                data_to_save.append(monster_class_list[x].get_str())
                data_to_save.append(monster_class_list[x].get_dex())
                data_to_save.append(monster_class_list[x].get_con())
                data_to_save.append(monster_class_list[x].get_int())
                data_to_save.append(monster_class_list[x].get_wis())
                data_to_save.append(monster_class_list[x].get_cha())
                data_to_save.append(monster_class_list[x].get_resistances())
                data_to_save.append(monster_class_list[x].get_damage_immunities())
                data_to_save.append(monster_class_list[x].get_weaknesses())
                data_to_save.append(monster_class_list[x].get_size())
                data_to_save.append(monster_class_list[x].get_type())
                data_to_save.append(monster_class_list[x].get_align())
                data_to_save.append(monster_class_list[x].get_sav_throws())
                data_to_save.append(monster_class_list[x].get_skills())
                data_to_save.append(monster_class_list[x].get_senses())
                data_to_save.append(monster_class_list[x].get_languages())
                data_to_save.append(monster_class_list[x].get_cr())
                data_to_save.append(monster_class_list[x].get_additional())
                data_to_save.append(monster_class_list[x].get_book_source())

            file.writelines("%s\n" % line for line in data_to_save)
            file.close()
            Log.append("Saved " + file_name)
            Log.append(
                "------------------------------------------------------------------------------------------" +
                "-------------------------------------------------------------------------------------------")
            default_window["-LOG-"].update(Log)

    # The events below are used to help the user select what they want to see, so they don't get overwhelmed with
    # information
    if event == "-MONSTER TYPE-":
        selected_checkboxes[0] = not selected_checkboxes[0]
        update_monster_menu()
    if event == "-MONSTER NAME-":
        selected_checkboxes[1] = not selected_checkboxes[1]
        update_monster_menu()
    if event == "-HP-":
        selected_checkboxes[2] = not selected_checkboxes[2]
        update_monster_menu()
    if event == "-HP/MAX HP-":
        selected_checkboxes[3] = not selected_checkboxes[3]
        update_monster_menu()
    if event == "-MAX HP-":
        selected_checkboxes[4] = not selected_checkboxes[4]
        update_monster_menu()
    if event == "-SPEED-":
        selected_checkboxes[5] = not selected_checkboxes[5]
        update_monster_menu()
    if event == "-FLY SPEED-":
        selected_checkboxes[6] = not selected_checkboxes[6]
        update_monster_menu()
    if event == "-SWIM SPEED-":
        selected_checkboxes[7] = not selected_checkboxes[7]
        update_monster_menu()
    if event == "-CLIMB SPEED-":
        selected_checkboxes[8] = not selected_checkboxes[8]
        update_monster_menu()
    if event == "-CON IMMU-":
        selected_checkboxes[9] = not selected_checkboxes[9]
        update_monster_menu()
    if event == "-AC-":
        selected_checkboxes[10] = not selected_checkboxes[10]
        update_monster_menu()
    if event == "-STR-":
        selected_checkboxes[11] = not selected_checkboxes[11]
        update_monster_menu()
    if event == "-DEX-":
        selected_checkboxes[12] = not selected_checkboxes[12]
        update_monster_menu()
    if event == "-CON-":
        selected_checkboxes[13] = not selected_checkboxes[13]
        update_monster_menu()
    if event == "-INT-":
        selected_checkboxes[14] = not selected_checkboxes[14]
        update_monster_menu()
    if event == "-WIS-":
        selected_checkboxes[15] = not selected_checkboxes[15]
        update_monster_menu()
    if event == "-CHA-":
        selected_checkboxes[16] = not selected_checkboxes[16]
        update_monster_menu()
    if event == "-RES-":
        selected_checkboxes[17] = not selected_checkboxes[17]
        update_monster_menu()
    if event == "-DMG IMMU-":
        selected_checkboxes[18] = not selected_checkboxes[18]
        update_monster_menu()
    if event == "-WEAK-":
        selected_checkboxes[19] = not selected_checkboxes[19]
        update_monster_menu()
    if event == "-SIZE-":
        selected_checkboxes[20] = not selected_checkboxes[20]
        update_monster_menu()
    if event == "-TYPE-":
        selected_checkboxes[21] = not selected_checkboxes[21]
        update_monster_menu()
    if event == "-ALIGN-":
        selected_checkboxes[22] = not selected_checkboxes[22]
        update_monster_menu()
    if event == "-ST-":
        selected_checkboxes[23] = not selected_checkboxes[23]
        update_monster_menu()
    if event == "-SKILLS-":
        selected_checkboxes[24] = not selected_checkboxes[24]
        update_monster_menu()
    if event == "-SENSES-":
        selected_checkboxes[25] = not selected_checkboxes[25]
        update_monster_menu()
    if event == "-LAN-":
        selected_checkboxes[26] = not selected_checkboxes[26]
        update_monster_menu()
    if event == "-CR-":
        selected_checkboxes[27] = not selected_checkboxes[27]
        update_monster_menu()
    if event == "-ADDI-":
        selected_checkboxes[28] = not selected_checkboxes[28]
        update_monster_menu()
    if event == "-BS-":
        selected_checkboxes[29] = not selected_checkboxes[29]
        update_monster_menu()
    if event == "-SAVING THROW-":
        default_window["-SAVING THROW TYPE-"].update(disabled=not default_window["-SAVING THROW TYPE-"].Disabled)
        default_window["-SAVING THROW AMOUNT-"].update(disabled=not default_window["-SAVING THROW AMOUNT-"].Disabled)

    # If user pushes enter or clicks the Submit button
    if event == "-SUBMIT BUTTON-":
        monsters_to_remove = []
        # Command is what was typed in the box in a string format
        command = str(values["-INPUT-"]).upper()
        # selected_monsters are monsters that were selected from the -MONSTERS- list
        selected_monsters = values["-MONSTERS-"]
        # Printing the command with the selected monsters
        if values["-SAVING THROW-"] and len(selected_monsters) != 0:
            if command is None or command is "" or command is 0:
                temp = values["-SAVING THROW TYPE-"] + " saving throw of " + values["-SAVING THROW AMOUNT-"]\
                       + " and DMG amount 0 with"
            else:
                temp = values["-SAVING THROW TYPE-"] + " saving throw of " + values[
                    "-SAVING THROW AMOUNT-"] + " and DMG amount" + command + " with"
        else:
            temp = command
        first_name = True
        for monster_name in selected_monsters:
            for x in range(0, len(monster_display_list)):
                if monster_display_list[x] == monster_name:
                    if x is not len(selected_monsters) and first_name is False:
                        temp += ", " + monster_class_list[x].get_name()
                        break
                    else:
                        if first_name is True:
                            first_name = False
                            temp += " " + monster_class_list[x].get_name()
                            break
                        else:
                            temp += ", and " + monster_class_list[x].get_name()
                            break
        Log.append(temp)

        # This occurs when there is a saving throw
        if values["-SAVING THROW-"]:
            # get the type of saving throw
            Saving_Throw_Type = str(values["-SAVING THROW TYPE-"]).upper()
            # gets the saving throw amount from the input, if not correct and if logs the error and reason why
            if values["-SAVING THROW AMOUNT-"].isnumeric():
                Saving_Throw_Amount = int(values["-SAVING THROW AMOUNT-"])
            else:
                Log.append(values["-SAVING THROW TYPE-"] + " is a incorrect, it must be a numeric number")
                default_window["-LOG-"].update(Log)
                continue
            modifier = 0
            # Nested for loops are used to find exactly what monster is needed to be updated
            for monster_name in selected_monsters:
                if not invalid_input:
                    for x in range(0, len(monster_display_list)):
                        if monster_display_list[x] == monster_name:
                            # series of if and else if statements get the type of saving throw stat that is needed
                            if Saving_Throw_Type == "STR":
                                modifier = monster_class_list[x].get_str()
                            elif Saving_Throw_Type == "INT":
                                modifier = monster_class_list[x].get_int()
                            elif Saving_Throw_Type == "CHA":
                                modifier = monster_class_list[x].get_cha()
                            elif Saving_Throw_Type == "CON":
                                modifier = monster_class_list[x].get_con()
                            elif Saving_Throw_Type == "DEX":
                                modifier = monster_class_list[x].get_dex()
                            elif Saving_Throw_Type == "WIS":
                                modifier = monster_class_list[x].get_wis()
                            # checks to see if the modifier is odd or even and finds the modifier value given DND
                            # 5e Rules
                            if modifier % 2 == 0:
                                modifier = int((modifier - 10) / 2)
                            else:
                                modifier = int((modifier - 11) / 2)
                            # adds modifier value to a random 1d20 roll
                            modifier += random.randint(1, 20)

                            # if the command was not a flat saving throw check
                            if not len(command) == 0:
                                # checks to see if rest of command is a number
                                if command.isnumeric():
                                    damage = int(command)
                                    passed = False
                                    # checks to see if current creature passes the saving throw or fails it
                                    # if passes, takes 1/2 damage as per DND 5e Rules
                                    if modifier >= Saving_Throw_Amount:
                                        passed = True
                                        damage = int(damage / 2)
                                    if monster_class_list[x].get_resistances() is not None and values["-DAMAGE TYPE-"] in monster_class_list[x].get_resistances():
                                        monster_class_list[x].take_damage(int(damage / 2))
                                    elif monster_class_list[x].get_damage_immunities() is not None and values["-DAMAGE TYPE-"] in monster_class_list[x].get_damage_immunities():
                                        pass
                                    elif monster_class_list[x].get_weaknesses() is not None and values["-DAMAGE TYPE-"] in monster_class_list[x].get_weaknesses():
                                        monster_class_list[x].take_damage(int(damage * 2))
                                    else:
                                        monster_class_list[x].take_damage(damage)
                                    # series of checks to see what combo of passing/failing and living or dying
                                    # happens to the creature
                                    if passed and monster_class_list[x].get_hp() <= 0:
                                        Log.append(
                                            monster_class_list[
                                                x].get_name() + " passed the " + Saving_Throw_Type +
                                            " saving throw but dies taking " + str(damage) + " damage")
                                        monsters_to_remove.append(x)
                                        break
                                    elif passed:
                                        Log.append(
                                            monster_class_list[
                                                x].get_name() + " passed the " + Saving_Throw_Type +
                                            " saving throw and takes " + str(damage) + " damage")
                                        break
                                    elif not passed and monster_class_list[x].get_hp() <= 0:
                                        Log.append(
                                            monster_class_list[
                                                x].get_name() + " failed the " + Saving_Throw_Type +
                                            " saving throw and dies taking " + str(damage) + " damage")
                                        monsters_to_remove.append(x)
                                        break
                                    else:
                                        Log.append(
                                            monster_class_list[
                                                x].get_name() + " failed the " + Saving_Throw_Type +
                                            " saving throw and takes " + str(damage) + " damage")
                                        break
                            # if there is no damage that needs to be applied with the saving throw
                            else:
                                if modifier >= Saving_Throw_Amount:
                                    Log.append(
                                        monster_class_list[x].get_name() + " passed the " + Saving_Throw_Type +
                                        " saving throw")
                                    break
                                else:
                                    Log.append(
                                        monster_class_list[x].get_name() + " failed the " + Saving_Throw_Type +
                                        " saving throw")
                                    break
        # if there is no saving throw and command starts with DMG
        else:
            # checks to see if rest of the command is a number
            if command.isnumeric():
                damage = int(command)
                # Nested for loops are used to find exactly what monster is needed to be updated
                for monster_name in selected_monsters:
                    for x in range(0, len(monster_display_list)):
                        if monster_display_list[x] == monster_name:
                            if monster_class_list[x].get_resistances() is not None and values["-DAMAGE TYPE-"] in monster_class_list[x].get_resistances():
                                monster_class_list[x].take_damage(int(damage / 2))
                            elif monster_class_list[x].get_damage_immunities() is not None and values["-DAMAGE TYPE-"] in monster_class_list[x].get_damage_immunities():
                                pass
                            elif monster_class_list[x].get_weaknesses() is not None and values["-DAMAGE TYPE-"] in monster_class_list[x].get_weaknesses():
                                monster_class_list[x].take_damage(int(damage * 2))
                            else:
                                monster_class_list[x].take_damage(damage)
                            # if else statement checks to see if monster dies or not
                            if monster_class_list[x].get_hp() <= 0:
                                Log.append(
                                    monster_class_list[x].get_name() + " dies taking " + str(damage) + " damage")
                                monsters_to_remove.append(x)
                                break
                            else:
                                Log.append(monster_class_list[x].get_name() + " takes " + str(damage) + " damage")
                                break

            else:
                Log.append("error " + command + " is not a number, input is incorrect")
        count = 0
        for x in monsters_to_remove:
            monster_class_list.remove(monster_class_list[x - count])
            selected_monsters.remove(monster_display_list[x - count])
            monster_display_list.remove(monster_display_list[x - count])
            count += 1
        update_monster_menu()
        Log.append(
            "------------------------------------------------------------------------------------------" +
            "-------------------------------------------------------------------------------------------")
        default_window["-LOG-"].update(Log)

default_window.close()
