# DnD Monster Manager
Description: DnD Monster Manager is  a program that helps a DM manager mosters' stats for DND 5e
Made by Kevin Boudreaux with the help of Carlos Salinas

How to use:
Once you run the program you will have 4 buttons on the bototm right of the screen, Save, Load, Add, and Edit as well as a text bar at the bottom left with a button 
called submit.

Add - Lets you add monsters to the manager, either through the dictanary or custom made.
      They are required to have a name and at least 1 must be made, all the other stats can be left blank

Edit - Allows you to edit the current selected monsters on the left side of the screen, you are able to edit each stat, including the name of the selected monster.
       The program will let you edit one at a time but forms a list if several monsters are selected

Load - You are able to load premade files formmated for the program

Save - You can save a list of monsters and their stats to be used for later
       Saves in the format needed for Load

Submit - Once you have clicked on the monster(s) you wish to either deal damage to or see if they pass a saving throw and then deal damage,
         enter a command in the format of:
         	(3 letter aberiavation for saving throw type) (score to beat for saving throw) dmg (damage on a failed save).
         	ex: str 10 dmg 15.
         or in the format of:
         	dmg (amount of damage the monster takes).
         	ex: dmg 15.
         Once you click submit, the program will roll for the selected monsters if needed and deal damage to them. If the monster's health reaches zero, then the
	 program will leave a message in the Action Log that the monster died and remove that monster from the list on the left.
									
Checkboxes - The checkboxes at the top left of the screen allow you to customize what stats you see for each monster, by default Monster Name, HP/Max HP, and Armor Class
													are selected. You are able to change what is shown by checking or unchecking each box
