from random import randint
from sys import exit

class Bg3DamageCalculator:
    armor_class = 18
    weapon_damage = "2d10+4"
    damage_reduction = 0
    flat_damage_negation = 1
    advantage = 0
    attacks_simulated = 10000
    savage_attacker = 0
    weapon_master = 0

    def dice_roll(self, sides: int) -> int:
        return randint(1,sides)
        
    def advantage_roll(self, sides: int) -> int:
        return max(self.dice_roll(sides),self.dice_roll(sides))

    def disadvantage_roll(self, sides: int) -> int:
        return min(self.dice_roll(sides),self.dice_roll(sides))
        
    def attack_roll(self, target_armor_class: int, ability_modifier: int, advantage: int) -> bool:
        if advantage == 0:
            return self.dice_roll(20) + ability_modifier >= target_armor_class
        if advantage == -1:
            return self.disadvantage_roll(20) + ability_modifier >= target_armor_class
        if advantage == 1:
            return self.advantage_roll(20) + ability_modifier >= target_armor_class
        
    def damage_roll(self, weapon_damage: str, target_damage_reduction: int, target_damage_negation: int, advantage: int) -> int:
        multiplier, rest = weapon_damage.split('d')
        die, modifier = rest.split('+')
        multiplier = int(multiplier)
        die = int(die)
        modifier = int(modifier)
        if advantage == 0:
            damage = multiplier*self.dice_roll(die)+modifier
        elif advantage == -1:
            damage = multiplier*self.disadvantage_roll_roll(die)+modifier
        elif advantage == 1:
            damage = multiplier*self.advantage_roll_roll(die)+modifier
        damage -= int(damage * (target_damage_reduction / 100)) + target_damage_negation
        return damage if damage >= 0 else 0

    def show_state(self) -> None:
        print('Current parameters:')
        print(f'<1> Weapon: {self.weapon_damage}')
        print(f'<2> Target armor class: {self.armor_class}')
        print(f'<3> Target damage reduction: {self.damage_reduction}%')
        print(f'<4> Target damage negation: {self.flat_damage_negation}')
        print(f'<5> Advantage: {('Disadvantage', 'None', 'Advantage')[self.advantage + 1]}')
        print(f'<6> Savage attacker: {'Yes' if self.savage_attacker else 'No'}')
        print(f'<7> Great weapon master/sharpshooter all in: {'Yes' if self.weapon_master else 'No'}\n')

    def change_parameters(self) -> None:
        self.show_state()
        while True:
            parameter = input('Choose a parameter to change (1..7),\nor\'done\' to go back to menu:')
            if parameter == '1':
                try:
                    weapon_damage = input(f'Input a new value for parameter <{parameter}>: ')
                    multiplier, rest = weapon_damage.split('d')
                    die, modifier = rest.split('+')
                    multiplier = int(multiplier)
                    die = int(die)
                    modifier = int(modifier)
                except TypeError:
                    print('Try again.')
                    continue
            elif parameter == '2':
                pass
            elif parameter == '3':
                pass
            elif parameter == '4':
                pass
            elif parameter == '5':
                break
            elif parameter == '6':
                break
            elif parameter == '7':
                break
            else:
                print('Incorrect option, try inputting again.')
                continue

    def menu(self) -> None:
        self.show_state()
        while True:
            print('-1- Show current parameters')
            print('-2- Change parameters')
            print(f'-3- Calculate damage per {self.attacks_simulated} attacks with current parameters')
            print('-4- Show log and compare damage')
            print('-5- Exit\n')
            option = input('Choose a menu option (1..5):')
            if option == '1':
                self.show_state()
            elif option == '2':
                pass
            elif option == '3':
                pass
            elif option == '4':
                pass
            elif option == '5':
                break
            else:
                print('Incorrect option, try inputting again.')
                continue
        print('Exiting..')

def main():
    calculator = Bg3DamageCalculator()
    calculator.menu()
if __name__ == '__main__':
    main()