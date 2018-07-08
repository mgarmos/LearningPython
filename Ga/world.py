import enemies
import random

class MapTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead")

    def modify_player(self, player):
        pass        

class StartTile(MapTile):
    def intro_text(self):
        return """ 
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

class BoringTile(MapTile):
    def intro_text(self):
        return """
        This is a very boring part of the cave.
        """  
class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        Victory is yours!
        """

class VictorTile(MapTile):
    def intro_text(self):
        return """
        You're in Víctor's room.
        Ajj!  It smells like feet
        Go out quickly or you will died
        """
class MomTile(MapTile):
    def intro_text(self):
        return """
        You've enter in mom's room without knocking the door. Mom shouts you.
        """

class AdrianTile(MapTile):
    def intro_text(self):
        return """
        You are in Adrian's room.
        and whose fault is it????
        jajaja
        """ 

class DadTile(MapTile):
    def intro_text(self):
        return """
        If you jump in dad's bed, he will nag you
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.KillerTeddy()        
        elif r < 0.75:
            self.enemy = enemies.Ogre()
        elif r < 0.90:
            self.enemy = enemies.BatColony()
        elif r < 0.97:
                self.enemy = enemies.GiantSpider()        
        else:
            self.enemy = enemies.RockMonster()
        
        # print("Has Been created: " + self.enemy.name + " in [" + str(x) + "," + str(y) +"]")
        # print("r: " + str(r))
        #print("Has Been created: " + self.enemy.name )

        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            return "A {} awaits!".format(self.enemy.name)
        else:
            return "You've defeated the {}.".format(self.enemy.name)

    def modify_player(self, player):
            if self.enemy.is_alive():
                player.hp = player.hp - self.enemy.damage
                print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))            

                   

world_map = [
    [MomTile(0,0),VictoryTile(1,0),DadTile(2,0)],
    [EnemyTile(0,1),EnemyTile(1,1),EnemyTile(2,1)],
    [BoringTile(0,2),StartTile(1,2),BoringTile(2,2)],
    [AdrianTile(0,3),EnemyTile(1,3),VictorTile(2,3)]

]

def tile_at(x, y):
    if x < 0 or y < 0 :
        return None
    
    try:
        return world_map[y][x]
    except IndexError:
        return BoringTile(0,0)
