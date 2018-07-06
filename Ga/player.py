import items

class Player:

    def __init__(self):
        self.inventory = [items.Rock(), items.Dagger(),'Gold(5)','Crusty Bread']

              
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = '';
        for weapon in self.inventory:
            try:
                if weapon.damage > max_damage:
                    max_damage = weapon.damage
                    best_weapon = weapon
            except AttributeError:
                pass
        return best_weapon


    def print_inventory(self):
        print('Inventory: ')
        for item in self.inventory:
            print('* ' + str(item))
        best_weapon =   self.most_powerful_weapon()  
        print("Your best weapon is your {}".format(best_weapon))
        return ''


