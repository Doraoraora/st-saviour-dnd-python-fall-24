import time
import random
from tav import Tav
from draw import draw_d20

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


if __name__ == '__main__':
    #print('THE LAST OF US 2')
    #collecting user input!!
    name = input('Name: ')
    print("SERAPHITE, JACKSON RESIDENT, WOLF, FEDRA")
    role = input("Choose your role: ")
    player = Tav(name, role)
    player.print_character_sheet()

    print_dramatic_text('Would you like to proceed or change stats/name? ')
    response = input()
    if response == 'YES':
        print(role)
    if response == 'NO':
        print('Too bad! /n' + role)

    print_dramatic_text('Which weapon would you like to wield?')
    print('SHIV, MOTOLOV, BASEBALL BAT, MACHETE, BOW AND ARROW')
    weapon = input()
   
    sv = 'SHIV'
    mv = 'MOTOLOV'
    bb = 'BASEBALL BAT'
    m = 'MACHETE'
    ba = 'BOW AND ARROW'

    s = 'SERAPHITE'
    jr = 'JACKSON RESIDENT'
    w = 'WOLF'
    f = 'FEDRA'

    if role == s:
        print_dramatic_text("The wolves have been bombarding our defense lines. /n If only they had kept their side of the agreement. /n The war is futile. /n Why won't they join into the hands of our prophet?")
    if role == jr:
        print_dramatic_text("You, Ellie, and Dina are still on the search for Tommy and Abby. /n Tensions are high after finding out about Dina's pregnancy.")
    if role == w:
         print_dramatic_text('You and Abby must rescue Owen from the hands of the Scars.')
    if role == f:
        print_dramatic_text("The government has abandoned us. /n You have to do it yourself. /n Restore society.")
    print_dramatic_text("It’s a chilly day in Seattle. Where will you begin your journey?")
    print("ST. MARY'S HOSPITAL, THE FOREST, HILLCREST, THE COAST, DOWNTOWN SEATTLE")
    location = input()
    
    mH = "ST. MARY'S HOSPITAL"
    tF = 'THE FOREST'
    h = 'HILLCREST'
    tC = 'THE COAST'
    dS = 'DOWNTOWN SEATTLE'
    
    if location == mH and role == w:
        print_dramatic_text("Here is where everyting changed. Abby's father... Joel's got what was coming to him... ")
    if location == mH:
        print_dramatic_text('You investigate a run-down hospital. /n Some form of slaugter must ave transpired here...')
    if location == tF and role == s:
        print_dramatic_text('You have to regroup. The plan to save the prophet will take place as soon as you arrive. /n ')
    if location == tF:
        print_dramatic_text('The area is overrun with Scars. You must be careful with other enemies in the area as well.')
    if location == h:
        print_dramatic_text(input('The houses and shops are either run down or filled with enemies. /n Do you wish to proceed? /n'))
        if input == 'YES':
            print('The Ruston Coffee shop is completely run down. You fall into a basement... /n Enemies are swarming you!')
    if location == tC:
        print_dramatic_text('The waves crash impatiently on the coast. You walk through the pier and encounter an enemy!')
    if location == dS:
        print_dramatic_text('You travel through the streets looking for supplies. The Bank looks promising. /n You swerve through the debris and make it to the bank lobby. /n A swarm of enemies swarm you!')

   
def generate_monster() -> int:
    r = random.randint(1, 12)
    draw_d20(20)
    if r == 1 or r == 2 or r == 3:
        print('+++++++ ' ' RUNNERS ' ' +++++++')
        print('+                                     +')
        print('+          roll required:  8          +')
        print('+                                     +')
        print('+++++++++++++++++++++++++++++++++++++++')
        return 8
    if r < 8:
        print('You died to a runner...? Embarassing...')


    if r == 4 or r == 5:
        print('+++++++ ' ' STALKERS ' ' +++++++')
        print('+                                     +')
        print('+          roll required: 12          +')
        print('+                                     +')
        print('+++++++++++++++++++++++++++++++++++++++')
        return 12
    if r > 12:
        print('I understand. These things are scary... / G A M E   O V E R ')

    if r == 6 or r == 7:
        print('++++++++ ' ' CLICKERS ' ' ++++++++')
        print('+                                     +')
        print('+          roll required: 14          +')
        print('+                                     +')
        print('+++++++++++++++++++++++++++++++++++++++')
        return 12
    if r > 14:
        print(' /n G A M E   O V E R ')

    if r == 8 or r == 9:
        print('+++++++ ' ' SHAMBLERS ' ' +++++++')
        print('+                                     +')
        print('+          roll required: 16          +')
        print('+                                     +')
        print('+++++++++++++++++++++++++++++++++++++++')
        return 16
    if r > 16:
        print(' /n  G A M E   O V E R ')

    if r == 10 or r == 11:
        print('+++++++ ' ' BLOATERS ' ' +++++++')
        print('+                                     +')
        print('+          roll required:  18          +')
        print('+                                     +')
        print('+++++++++++++++++++++++++++++++++++++++')
        return 18
    if r > 18:
        print(' /n   G A M E  O V E R')
    if location == mH and r == 12:
        eye = '\U0001F441'
        print('+++++++++ ' + eye + '  THE RAT KING ' + eye + '  +++++++++')
        print('+                                     +')
        print('+          roll required:  20         +')
        print('+                                     +')
        print('+++++++++++++++++++++++++++++++++++++++')
        return 20
    if r > 20:
        print(' /n ')
    #return -1
    