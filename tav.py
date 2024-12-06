import random
from draw import draw_d20
class Tav:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        #self.level = 1

        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.intelligence = 0
        self.wisdom = 0
        self.assign_stats()

    
        character_sheet:self
        self.strength = assign_stats[0]
        self.dexterity = assign_stats[1]
        self.constitution = assign_stats[2]
        self.charisma = assign_stats[3]
        self.intelligence = assign_stats[4]
        self.wisdom = assign_stats[5]
        
        print('====== ' + ' THE LAST OF US 2 ' + ' ======')
        print('What is your name? :  ' + self.name)
        print('Choose your role :  ' + self.role)
        #print('Level: ' + str(self.level))
        print('--------- ' +' YOUR STATS ' + ' ---------')
        print('Strength         ' + str(self.strength))
        print('Dexterity        ' + str(self.dexterity))
        print('Constitution     ' + str(self.constitution))
        print('Charisma         ' + str(self.charisma))
        print('Intelligence     ' + str(self.intelligence))
        print('Wisdom           ' + str(self.wisdom))
        print('---------------------------------------')

def assign_stats(self) -> None:
        standard = [15, 14, 13, 12, 10, 8]
        random.shuffle(standard)