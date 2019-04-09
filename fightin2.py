from random import choice
import random
import time
import os

# races for the AI and the player to pick from
racePicker = ['human',
              'orc',
              'goblin',
              'dwarf',
              'troll',
              'elf',
              'halfling',
              'gnome']

race_human = {'HP_Mod': 3, 'AC_Mod': 0, 'ATK_Mod': 1}
race_orc = {'HP_Mod': 7, 'AC_Mod': 4, 'ATK_Mod': 3}
race_goblin = {'HP_Mod': 4, 'AC_Mod': 2, 'ATK_Mod': 2}
race_dwarf = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 3}
race_troll = {'HP_Mod': 3, 'AC_Mod': 3, 'ATK_Mod': 2}
race_elf = {'HP_Mod': 8, 'AC_Mod': 2, 'ATK_Mod': 2}
race_halfling = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 2}
race_gnome = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 2}

hitPoints, armorClass, attack = 50, 0, 1

player_name = ''
enemy_name = ''

# ---------------------------------------Player Stuff---------------------------------------
# User interface and player builder
# Opening Title screen
def playerInterface():

    player_name = ''
    global PLAYER_STATS

    print('-' * 90)
    print('-' * 90)
    print(' __     __     ______     __         ______     ______     __    __     ______    ')
    print('/\ \  _ \ \   /\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   ')
    print('\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\   ')
    print(' \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\ ')
    print('  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/ ')
    print('*' * 90)
    print(' ______   __         ______     __  __     ______     ______                      ')
    print('/\  == \ /\ \       /\  __ \   /\ \_\ \   /\  ___\   /\  == \                     ')
    print('\ \  _-/ \ \ \____  \ \  __ \  \ \____ \  \ \  __\   \ \  __<                     ')
    print(' \ \_\    \ \_____\  \ \_\ \_\  \/\_____\  \ \_____\  \ \_\ \_\                   ')
    print('  \/_/     \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/ /_/                   ')
    print('-' * 90)
    # Frankly true
    print('The GOD of this program was not sober when he made it so have fun')
    print('-' * 90)
    print('In this game you the player will be battling against another race which is randomly generated.')
    print('THE GAME IS TIMED SO IF YOU DO NOT REACT FAST ENOUGH YOU WILL LOOSE!!!!')
    print('The game only gets harder as you beat other players')

    player_name = input('Please Type your Character Name(EX.Grosssmash): ')
    race_choice = True
    while race_choice:
        print("Pick a race: 'Human', 'Orc', 'Goblin', 'Dwarf', 'Troll', 'Elf', 'Halfling', or 'Gnome'")
        #textTime(u ="Pick a race: 'Human', 'Orc', 'Goblin', 'Dwarf', 'Troll', 'Elf', 'Halfling', or 'Gnome'")
        player_race = input('Race: ')
        for i in racePicker:
            if player_race.lower() == i.lower():
                player_race = i
                race_choice = False
                break
            else:
                None


    PLAYER_STATS = {'NAME: ':player_name,'RACE: ':player_race,'HITPOINTS: ':hitPoints, 'ARMOR ClASS: ':armorClass, 'ATTACK: ':attack}

# Player stats depending upon what they pick.
def player_stats(racePicker):

    global ENEMY_STATS

    race_human = {'HP_Mod': 3, 'AC_Mod': 0, 'ATK_Mod': 1}
    race_orc = {'HP_Mod': 7, 'AC_Mod': 4, 'ATK_Mod': 3}
    race_goblin = {'HP_Mod': 4, 'AC_Mod': 2, 'ATK_Mod': 2}
    race_dwarf = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 3}
    race_troll = {'HP_Mod': 3, 'AC_Mod': 3, 'ATK_Mod': 2}
    race_elf = {'HP_Mod': 8, 'AC_Mod': 2, 'ATK_Mod': 2}
    race_halfling = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 2}
    race_gnome = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 2}

    hitPoints, armorClass, attack = 50, 0, 1

    if racePicker == 'human':
        hitPoints += race_human['HP_Mod']
        armorClass += race_human['AC_Mod']
        attack += race_human['ATK_Mod']

    elif racePicker == 'orc':
        hitPoints += race_orc['HP_Mod']
        armorClass += race_orc['AC_Mod']
        attack += race_orc['ATK_Mod']

    elif racePicker == 'goblin':
        hitPoints += race_goblin['HP_Mod']
        armorClass += race_goblin['AC_Mod']
        attack += race_goblin['ATK_Mod']

    elif racePicker == 'dwarf':
        hitPoints += race_dwarf['HP_Mod']
        armorClass += race_dwarf['AC_Mod']
        attack += race_dwarf['ATK_Mod']

    elif racePicker == 'troll':
        hitPoints += race_troll['HP_Mod']
        armorClass += race_troll['AC_Mod']
        attack += race_troll['ATK_Mod']

    elif racePicker == 'elf':
        hitPoints += race_elf['HP_Mod']
        armorClass += race_elf['AC_Mod']
        attack += race_elf['ATK_Mod']

    elif racePicker == 'halfling':
        hitPoints += race_halfling['HP_Mod']
        armorClass += race_halfling['AC_Mod']
        attack += race_halfling['ATK_Mod']

    elif racePicker == 'gnome':
        hitPoints += race_gnome['HP_Mod']
        armorClass += race_gnome['AC_Mod']
        attack += race_gnome['ATK_Mod']
    else:
        None

# User stats
# This is where the player it sets the players stats-damage and all that and what nots

# user attack

# ---------------------------------------Enemy Stuff-----------------------------------------

# Generate Enemy
def genEnemy():
    #generates the AI player race
    #generates the names
    #adds the stats given to AI
    #so it knows what stats to use for what races it is using
    #The time in which the AI and the program moves itself
    #also sets the time limit between attacks
    #A friend of mine who I play Dungeons and Dragons with helped me pick so names out
    male_names = ['Grosssmash', 'Dogplunder', 'Greenfoot', 'Shriekvenger', 'Redface', 'Cruelanger',
                  'Redspark', 'Traphammer', 'Cruelvenger', 'Inatheyiu', 'Thaleriu', 'Scatinoo',
                  'Hexaneskiu', 'Stingtansol', 'Herinon', 'Fretharum', 'Matun', 'Funochun', 'Awdpio', 'Wardov',
                  'Laridan', 'Cilired', 'Borewin', 'Gwiratha', 'Falenidd', 'Galeamos', 'Morlune', 'Miriawan', 'Higo',
                  'Foli', 'Voilir',
                  'Dumli', 'Glegnus', 'Fulin', 'Febur', 'Gagan', 'Noiin', 'Toimli', 'Huginn', 'Jengo', 'Zobogo',
                  'Trojahsus', 'Galjin',
                  'Chesuk', 'Baba', 'Mezilalor', 'Zic', 'Maji', 'Texmon']
    #AI player races choice
    enemy_race = random.choice(racePicker)
    #Plus the random name
    enemy_name = random.choice(male_names)
    #plus the AI stats depending upon who he or she uses it.
    enemy_stats(enemy_race)


# enemy stats
def enemy_stats(racePicker):

    global ENEMY_STATS
    enemy_race = ''
    enemy_name = ''

    race_human = {'HP_Mod': 3, 'AC_Mod': 0, 'ATK_Mod': 1}
    race_orc = {'HP_Mod': 7, 'AC_Mod': 4, 'ATK_Mod': 3}
    race_goblin = {'HP_Mod': 4, 'AC_Mod': 2, 'ATK_Mod': 2}
    race_dwarf = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 3}
    race_troll = {'HP_Mod': 3, 'AC_Mod': 3, 'ATK_Mod': 2}
    race_elf = {'HP_Mod': 8, 'AC_Mod': 2, 'ATK_Mod': 2}
    race_halfling = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 2}
    race_gnome = {'HP_Mod': 6, 'AC_Mod': 4, 'ATK_Mod': 2}

    hitPoints, armorClass, attack = 50, 0, 1

    if racePicker == 'human':
        hitPoints += race_human['HP_Mod']
        armorClass += race_human['AC_Mod']
        attack += race_human['ATK_Mod']

    elif racePicker == 'orc':
        hitPoints += race_orc['HP_Mod']
        armorClass += race_orc['AC_Mod']
        attack += race_orc['ATK_Mod']

    elif racePicker == 'goblin':
        hitPoints += race_goblin['HP_Mod']
        armorClass += race_goblin['AC_Mod']
        attack += race_goblin['ATK_Mod']

    elif racePicker == 'dwarf':
        hitPoints += race_dwarf['HP_Mod']
        armorClass += race_dwarf['AC_Mod']
        attack += race_dwarf['ATK_Mod']

    elif racePicker == 'troll':
        hitPoints += race_troll['HP_Mod']
        armorClass += race_troll['AC_Mod']
        attack += race_troll['ATK_Mod']

    elif racePicker == 'elf':
        hitPoints += race_elf['HP_Mod']
        armorClass += race_elf['AC_Mod']
        attack += race_elf['ATK_Mod']

    elif racePicker == 'halfling':
        hitPoints += race_halfling['HP_Mod']
        armorClass += race_halfling['AC_Mod']
        attack += race_halfling['ATK_Mod']

    elif racePicker == 'gnome':
        hitPoints += race_gnome['HP_Mod']
        armorClass += race_gnome['AC_Mod']
        attack += race_gnome['ATK_Mod']
    else:
        None

        ENEMY_STATS = {'NAME: ': enemy_name, 'RACE: ': enemy_race, 'HITPOINTS: ': hitPoints,
                       'ARMOR ClASS: ': armorClass, 'ATTACK: ': attack}
# enemy attack

# ----------------------------------------Battle Stuff----------------------------------------
#battle stats
def printBattleStats():

    print('      |Battle|     ')
    print(('NAME:       %s VS %s') % (player_name, enemy_name))
    print(('Hitpoints:     %s        %s') % (PLAYER_STATS['HITPOINTS: '], ENEMY_STATS['HITPOINTS: ']))
    print(('ArmorClass:    %s         %s') % (PLAYER_STATS['ARMOR ClASS: '], ENEMY_STATS['ARMOR CLASS: ']))
    print(('Race:          %s     %s') % (PLAYER_STATS['RACE: '], ENEMY_STATS['RACE: ']))
    print(('Attack:        %s         %s') % (PLAYER_STATS['ATTACK:  '], ENEMY_STATS['ATTACK: ']))
# Battle settings


# Quick play(still battle stuff)

# ----------------------------------------Game Detail Stuff-----------------------------------
# Makes new line after each play
# nl = next line
def nl():
    print('\n')


# text time and player time depend upon what it is(overall time)
def textTime(u):
    for i in u:
        time.sleep(0.03)
        print(i, end='')
    nl()


# prints battles stats before game starts

# User interface
playerInterface()
