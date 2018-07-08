from player import Player
import world

def play():
    

    print('Escape from Cave Terror!')
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)

        print(player.x)
        print(player.y)


        print(room.intro_text())
        room.modify_player(player)
        
        # Interactives rooms
        if room.x == 0 and room.y == 0:
            print("You have lost 50hp")
            player.hp = player.hp - 50

        if room.x == 2 and room.y == 3:
            print("You have lost 15hp")
            player.hp -= 15


        # Termina el juego
        if player.hp < 1:
            print('PLAYER DIED')
            return
        if room.x == 1 and room.y == 0:
            print('YOU WIN')
            print(str(player.hp) + ' (hp)')
            return

        action_input = get_player_command()


        if action_input in ['n', 'N']:
            player.move_north()
            
        elif action_input in ['s', 'S']:
            player.move_south()
        elif action_input in ['e', 'E']:
            player.move_east()
        elif action_input in ['w', 'W']:
            player.move_west()
        elif action_input in ['A', 'a']:
            player.attack()
        elif action_input in ['sw', 'SW']:
            player.move_south()
            player.move_west()
        elif action_input in ['se', 'SE']:
            player.move_south()
            player.move_east()
        elif action_input in ['ne', 'NE']:
            player.move_north()
            player.move_east()
        elif action_input in ['nw', 'NW']:
            player.move_north()
            player.move_west()

        elif action_input in ['I', 'i']:        
            print(player.print_inventory())
            print (player.hp)
                        
        else:
            print('Acción inválida')


def get_player_command():
    return input('Accion: ')


play()




