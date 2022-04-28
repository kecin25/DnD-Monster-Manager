# DND stat Tracker
# Made by: Kevin Boudreaux and Carlos Salinas
# main.py last edited by Kevin Boudreaux on 4/27/2022

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

# log_column is used to display what actions were recently taken by the user and stores buttons for Add Monster,
# Save, and Load
log_column = [
    [
        gui.Text(text="Action Log", auto_size_text=False, justification="center", size=(WIDTH, 1))
    ],
    [
        gui.Listbox(values=[], size=(WIDTH, HEIGHT), key="-LOG-", expand_x=True, expand_y=True)
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

# monster_list is used to list the creatures being used, first is the Text to show what is in the boxes below Next is
# the List box of monsters that are in play Then there is an Input box and a button on the same row for the User to
# use

# TODO add a third panel that displays the most recent selected monster's actions that it can take. Either
#  through text or picture
monster_list = \
    [
        [
            gui.Text(text="Monsters", auto_size_text=True, justification="center", size=(WIDTH, 3)),
        ],
        [
            gui.Checkbox(checkbox_color="black", text="Monster Type", key="-MONSTER TYPE-", enable_events=True),
            gui.Checkbox(checkbox_color="black", text="Monster Name", key="-MONSTER NAME-", enable_events=True,
                         default=True),
            gui.Checkbox(checkbox_color="black", text="HP", key="-HP-", enable_events=True),
            gui.Checkbox(checkbox_color="black", text="HP/Max HP", key="-HP/MAX HP-", enable_events=True, default=True),
            gui.Checkbox(checkbox_color="black", text="Max HP", key="-MAX HP-", enable_events=True)
        ],
        [
            gui.Checkbox(checkbox_color="black", text="Armor Class", key="-AC-", enable_events=True, default=True),
            gui.Checkbox(checkbox_color="black", text="Speed", key="-SPEED-", enable_events=True),
            gui.Checkbox(checkbox_color="black", text="STR", key="-STR-", enable_events=True),
            gui.Checkbox(checkbox_color="black", text="DEX", key="-DEX-", enable_events=True),
            gui.Checkbox(checkbox_color="black", text="CON", key="-CON-", enable_events=True),
            gui.Checkbox(checkbox_color="black", text="INT", key="-INT-", enable_events=True),
            gui.Checkbox(checkbox_color="black", text="WIS", key="-WIS-", enable_events=True),
            gui.Checkbox(checkbox_color="black", text="CHA", key="-CHA-", enable_events=True),

        ],
        [
            gui.Listbox(values=monster_display_list, enable_events=True, size=(WIDTH, HEIGHT), select_mode='multiple',
                        key="-MONSTERS-", font="Courier")
        ],
        [
            gui.In(size=(WIDTH - 20, 0), enable_events=True, key="-INPUT-"),
            gui.Button(button_text="Submit", size=(20, 1), bind_return_key=True, key="-SUBMIT BUTTON-")
        ]
    ]

layout_default = \
    [
        [
            gui.Column(monster_list),
            gui.VerticalSeparator(color="Black"),
            gui.Column(log_column),
        ]
    ]

Log = []
selected_checkboxes = [False, True, False, True, False, True, False, False, False, False, False, False, False]


# Window used when adding monsters to the manager
# It has its own function because PySimpleGUI does not allow a window to be open and closed
# The workaround is making a new copy of the layout every time the function is called
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
                gui.Text(text="Speed", auto_size_text=True, justification="left", size=TEXT_SIZE),
                gui.In(enable_events=True, key="-SPEED-", size=BOX_SIZE)
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
                gui.Button(button_text="Accept", auto_size_button=True, enable_events=True, key="-ACCEPT-"),
                gui.Button(button_text="Cancel", auto_size_button=True, enable_events=True, key="-CANCEL-")
            ],
        ]
    layout_add_monster = [[gui.Column(monster_maker)]]
    return gui.Window("Add Monster", layout_add_monster)


def make_edit_monster_window(name, ac, speed, max_hp, hp, str, dex, con, int, wis, cha):
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
    # longest_x is used to find the longest character length of all possible strings in the monster_class_list
    longest_0 = 0
    longest_1 = 0
    longest_2 = 0
    longest_3 = 0
    longest_4 = 0
    longest_5 = 0
    longest_6 = 0
    longest_7 = 0
    longest_8 = 0
    longest_9 = 0
    longest_10 = 0
    longest_11 = 0
    temp_names = []

    # To keep all for loops running each time, they will only run when their checkbox has been selected
    if selected_checkboxes[0]:
        for x in monster_class_list:
            temp_names.append(x.get_true_name())
        if len(monster_class_list) != 0:
            longest_0 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[1]:
        for x in monster_class_list:
            temp_names.append(x.get_name())
        if len(monster_class_list) != 0:
            longest_1 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[2]:
        for x in monster_class_list:
            temp_names.append(str(x.get_hp()))
        if len(monster_class_list) != 0:
            longest_2 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[3]:
        for x in monster_class_list:
            temp_names.append(str(x.get_hp()) + str(x.get_max_hp()))
        if len(monster_class_list) != 0:
            longest_3 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[4]:
        for x in monster_class_list:
            temp_names.append(str(x.get_max_hp()))
        if len(monster_class_list) != 0:
            longest_4 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[1]:
        for x in monster_class_list:
            temp_names.append(str(x.get_ac()))
        if len(monster_class_list) != 0:
            longest_5 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[6]:
        for x in monster_class_list:
            temp_names.append(str(x.get_speed()))
        if len(monster_class_list) != 0:
            longest_6 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[7]:
        for x in monster_class_list:
            temp_names.append(str(x.get_str()))
        if len(monster_class_list) != 0:
            longest_7 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[8]:
        for x in monster_class_list:
            temp_names.append(str(x.get_dex()))
        if len(monster_class_list) != 0:
            longest_8 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[9]:
        for x in monster_class_list:
            temp_names.append(str(x.get_con()))
        if len(monster_class_list) != 0:
            longest_9 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[10]:
        for x in monster_class_list:
            temp_names.append(str(x.get_int()))
        if len(monster_class_list) != 0:
            longest_10 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    if selected_checkboxes[11]:
        for x in monster_class_list:
            temp_names.append(str(x.get_wis()))
        if len(monster_class_list) != 0:
            longest_11 = len(max(temp_names, key=len)) + 5
        temp_names.clear()

    # This series of nested for loops prints the desired output given the selected_checkboxes and longest strings
    for num in range(0, len(monster_class_list)):
        if num >= len(monster_display_list):
            monster_display_list.append("")
        monster_display_list[num] = ""
        if selected_checkboxes[0]:
            monster_display_list[num] += monster_class_list[num].get_true_name()
            for i in range(len(monster_class_list[num].get_true_name()), longest_0):
                monster_display_list[num] += " "
        if selected_checkboxes[1]:
            monster_display_list[num] += monster_class_list[num].get_name()
            for i in range(len(monster_class_list[num].get_name()), longest_1):
                monster_display_list[num] += " "
        if selected_checkboxes[2]:
            monster_display_list[num] += "HP: " + str(monster_class_list[num].get_hp())
            for i in range(len(monster_class_list[num].get_hp()), longest_2):
                monster_display_list[num] += " "
        if selected_checkboxes[3]:
            monster_display_list[num] += "HP/Max HP: " + str(monster_class_list[num].get_hp()) + "/" + str(
                monster_class_list[num].get_max_hp())
            for i in range(len(str(monster_class_list[num].get_hp())) + len(str(monster_class_list[num].get_max_hp())),
                           longest_3):
                monster_display_list[num] += " "
        if selected_checkboxes[4]:
            monster_display_list[num] += "Max HP: " + str(monster_class_list[num].get_max_hp())
            for i in range(len(str(monster_class_list[num].get_max_hp())), longest_4):
                monster_display_list[num] += " "
        if selected_checkboxes[5]:
            monster_display_list[num] += "AC: " + str(monster_class_list[num].get_ac())
            for i in range(len(str(monster_class_list[num].get_ac())), longest_5):
                monster_display_list[num] += " "
        if selected_checkboxes[6]:
            monster_display_list[num] += "Speed: " + str(monster_class_list[num].get_speed())
            for i in range(len(str(monster_class_list[num].get_speed())), longest_6):
                monster_display_list[num] += " "
        if selected_checkboxes[7]:
            monster_display_list[num] += "Str: " + str(monster_class_list[num].get_str())
            for i in range(len(str(monster_class_list[num].get_str())), longest_7):
                monster_display_list[num] += " "
        if selected_checkboxes[8]:
            monster_display_list[num] += "Dex: " + str(monster_class_list[num].get_dex())
            for i in range(len(str(monster_class_list[num].get_dex())), longest_8):
                monster_display_list[num] += " "
        if selected_checkboxes[9]:
            monster_display_list[num] += "Con: " + str(monster_class_list[num].get_con())
            for i in range(len(str(monster_class_list[num].get_con())), longest_9):
                monster_display_list[num] += " "
        if selected_checkboxes[10]:
            monster_display_list[num] += "Int: " + str(monster_class_list[num].get_int())
            for i in range(len(str(monster_class_list[num].get_int())), longest_10):
                monster_display_list[num] += " "
        if selected_checkboxes[11]:
            monster_display_list[num] += "Wis: " + str(monster_class_list[num].get_wis())
            for i in range(len(str(monster_class_list[num].get_wis())), longest_11):
                monster_display_list[num] += " "
        if selected_checkboxes[12]:
            monster_display_list[num] += "Cha: " + str(monster_class_list[num].get_cha())
    default_window["-MONSTERS-"].update(monster_display_list)


default_window = gui.Window("Monster stat Tracker", layout_default, resizable=True, grab_anywhere=True)
while True:
    event, values = default_window.read()
    # selected_monsters is used to get the monsters the user selected in the form of a list
    selected_monsters = []
    # invalid_input is used when dealing with saving throws or dealing damage to the monsters
    invalid_input = False
    if event == "Exit" or event == gui.WIN_CLOSED:
        break

    # Add is ran when the ADD button is clicked
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
                monster_maker_window["-SPEED-"].update(mn.get_speed())
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
                    for x in range(1, int(adding_values["-AMOUNT-"]) + 1):
                        mn = mon(adding_values["-TYPE-"], str(adding_values["-NAME-"] + " " + str(x)))
                        mn.set_ac(adding_values["-AC-"])
                        mn.set_speed(adding_values["-SPEED-"])
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
    if event == "-EDIT-":
        selected_monsters = values["-MONSTERS-"]
        # Nested for loop is used to edit each monster in the selected list, the user will be able to edit one monster
        # at a time until all the selected monsters have been processed
        for monster_name in selected_monsters:
            for x in range(0, len(monster_display_list)):
                if monster_display_list[x] == monster_name:
                    monster_maker_window = make_edit_monster_window(monster_class_list[x].get_name(),
                                                                    monster_class_list[x].get_ac(),
                                                                    monster_class_list[x].get_speed(),
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
                                monster_class_list[x].set_speed(editing_values["-SPEED-"])
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
                    mn.set_hp(contents[0])
                    contents.pop(0)
                    error_line += 1
                    numeric_boolean = contents[0].isnumeric()
                    if numeric_boolean:
                        mn.set_max_hp(contents[0])
                        contents.pop(0)
                        error_line += 1
                        numeric_boolean = contents[0].isnumeric()
                        if numeric_boolean:
                            mn.set_ac(contents[0])
                            contents.pop(0)
                            error_line += 1
                            numeric_boolean = contents[0].isnumeric()
                            if numeric_boolean:
                                mn.set_speed(contents[0])
                                contents.pop(0)
                                error_line += 1
                                numeric_boolean = contents[0].isnumeric()
                                if numeric_boolean:
                                    mn.set_str(contents[0])
                                    contents.pop(0)
                                    error_line += 1
                                    numeric_boolean = contents[0].isnumeric()
                                    if numeric_boolean:
                                        mn.set_dex(contents[0])
                                        contents.pop(0)
                                        error_line += 1
                                        numeric_boolean = contents[0].isnumeric()
                                        if numeric_boolean:
                                            mn.set_con(contents[0])
                                            contents.pop(0)
                                            error_line += 1
                                            numeric_boolean = contents[0].isnumeric()
                                            if numeric_boolean:
                                                mn.set_int(contents[0])
                                                contents.pop(0)
                                                error_line += 1
                                                numeric_boolean = contents[0].isnumeric()
                                                if numeric_boolean:
                                                    mn.set_wis(contents[0])
                                                    contents.pop(0)
                                                    error_line += 1
                                                    numeric_boolean = contents[0].isnumeric()
                                                    if numeric_boolean:
                                                        mn.set_cha(contents[0])
                                                        contents.pop(0)
                                                        monster_class_list.append(mn)
                if not numeric_boolean:
                    Log.append("File Corrupted, non numeric value on line " + str(error_line))
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
                data_to_save.append(monster_class_list[x].get_ac())
                data_to_save.append(monster_class_list[x].get_speed())
                data_to_save.append(monster_class_list[x].get_str())
                data_to_save.append(monster_class_list[x].get_dex())
                data_to_save.append(monster_class_list[x].get_con())
                data_to_save.append(monster_class_list[x].get_int())
                data_to_save.append(monster_class_list[x].get_wis())
                data_to_save.append(monster_class_list[x].get_cha())
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
    if event == "-AC-":
        selected_checkboxes[5] = not selected_checkboxes[5]
        update_monster_menu()
    if event == "-SPEED-":
        selected_checkboxes[6] = not selected_checkboxes[6]
        update_monster_menu()
    if event == "-STR-":
        selected_checkboxes[7] = not selected_checkboxes[7]
        update_monster_menu()
    if event == "-DEX-":
        selected_checkboxes[8] = not selected_checkboxes[8]
        update_monster_menu()
    if event == "-CON-":
        selected_checkboxes[9] = not selected_checkboxes[9]
        update_monster_menu()
    if event == "-INT-":
        selected_checkboxes[10] = not selected_checkboxes[10]
        update_monster_menu()
    if event == "-WIS-":
        selected_checkboxes[11] = not selected_checkboxes[11]
        update_monster_menu()
    if event == "-CHA-":
        selected_checkboxes[12] = not selected_checkboxes[12]
        update_monster_menu()

    # If user pushes enter or clicks the Submit button
    if event == "-SUBMIT BUTTON-":
        # Command is what was typed in the box in a string format
        command = str(values["-INPUT-"]).upper()
        # selected_monsters are monsters that were selected from the -MONSTERS- list
        selected_monsters = values["-MONSTERS-"]
        # Printing the command with the selected monsters
        if len(selected_monsters) != 0:
            temp = command + " with "
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
        if command.startswith("STR") or command.startswith("INT") or command.startswith("CHA") \
                or command.startswith("CON") or command.startswith("DEX") or command.startswith("WIS"):
            # First three characters are the saving throw type if correct command
            Saving_Throw_Type = command[0:3]
            command = command[4:]
            # gets the saving throw amount from the command input if correct and if logs the error and reason why
            if command.find(" ") > 0:
                Saving_Throw_Amount = int(command[0:command.index(" ")])
            elif command.isnumeric():
                Saving_Throw_Amount = int(command)
            else:
                Log.append(command + " is a incorrect type of command; first error detected is a missing space")
                default_window["-LOG-"].update(Log)
                continue
            if command.find(" ") > 0:
                command = command[command.index(" ") + 1:]
            else:
                command = ""
            modifier = 0
            # checks to see if what is stored in Saving_Throw_Type is valid
            if Saving_Throw_Type != "STR" and not "DEX" and not "CON" and not "INT" and not "WIS" and not "CHA":
                Log.append(command + " is not a valid saving throw command")
                default_window["-LOG-"].update(Log)
            else:
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
                                    # checks to see if first part of the rest of the command is calling for Damage
                                    if not command[0:3] == "DMG":
                                        Log.append(
                                            command + " is a invalid input; should have dmg next or nothing else in "
                                                      "the command line")
                                        default_window["-LOG-"].update(Log)
                                        invalid_input = True
                                        break
                                    # checks to see if rest of command is a number
                                    if command[4:].isnumeric():
                                        damage = int(command[4:])
                                        passed = False
                                        # checks to see if current creature passes the saving throw or fails it
                                        # if passes, takes 1/2 damage as per DND 5e Rules
                                        if modifier >= Saving_Throw_Amount:
                                            passed = True
                                            damage = int(damage / 2)
                                        monster_class_list[x].take_damage(damage)
                                        # series of checks to see what combo of passing/failing and living or dying
                                        # happens to the creature
                                        if passed and monster_class_list[x].get_hp() <= 0:
                                            Log.append(
                                                monster_class_list[
                                                    x].get_name() + " passed the " + Saving_Throw_Type +
                                                " saving throw but dies taking " + str(damage) + " damage")
                                            monster_class_list.remove(monster_class_list[x])
                                            selected_monsters.remove(monster_display_list[x])
                                            monster_display_list.remove(monster_display_list[x])
                                            break
                                        elif passed:
                                            Log.append(
                                                monster_class_list[
                                                    x].get_name() + " passed the " + Saving_Throw_Type +
                                                " saving throw and takes " + str(damage) + " damage")
                                        elif not passed and monster_class_list[x].get_hp() <= 0:
                                            Log.append(
                                                monster_class_list[
                                                    x].get_name() + " failed the " + Saving_Throw_Type +
                                                " saving throw and dies taking " + str(damage) + " damage")
                                            monster_class_list.remove(monster_class_list[x])
                                            selected_monsters.remove(monster_display_list[x])
                                            monster_display_list.remove(monster_display_list[x])
                                            break
                                        else:
                                            Log.append(
                                                monster_class_list[
                                                    x].get_name() + " failed the " + Saving_Throw_Type +
                                                " saving throw and takes " + str(damage) + " damage")
                                # if there is no damage that needs to be applied with the saving throw
                                else:
                                    if modifier >= Saving_Throw_Amount:
                                        Log.append(
                                            monster_class_list[x].get_name() + " passed the " + Saving_Throw_Type +
                                            " saving throw")
                                    else:
                                        Log.append(
                                            monster_class_list[x].get_name() + " failed the " + Saving_Throw_Type +
                                            " saving throw")
        # if there is no saving throw and command starts with DMG
        else:
            # checks to see if rest of the command is a number
            if command[4:].isnumeric():
                damage = int(command[4:])
                # Nested for loops are used to find exactly what monster is needed to be updated
                for monster_name in selected_monsters:
                    for x in range(0, len(monster_display_list)):
                        if monster_display_list[x] == monster_name:
                            monster_class_list[x].take_damage(damage)
                            # if else statement checks to see if monster dies or not
                            if monster_class_list[x].get_hp() <= 0:
                                Log.append(
                                    monster_class_list[x].get_name() + " dies taking " + str(damage) + " damage")
                                monster_class_list.remove(monster_class_list[x])
                                selected_monsters.remove(monster_display_list[x])
                                monster_display_list.remove(monster_display_list[x])
                            else:
                                Log.append(monster_class_list[x].get_name() + " takes " + str(damage) + " damage")
                            break
            else:
                print("error " + command[4:] + " is not a number, input is incorrect")

        update_monster_menu()
        Log.append(
            "------------------------------------------------------------------------------------------" +
            "-------------------------------------------------------------------------------------------")
        default_window["-LOG-"].update(Log)

default_window.close()
