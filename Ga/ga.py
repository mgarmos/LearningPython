from player import Player

def play():
    player = Player()

    print('Mensaje de bienvenida')

    

    action_input = get_user_command()

    if action_input in ['n', 'N']:
        print('Ir al norte')
    elif action_input in ['s', 'S']:
        print('Ir al sur')
    elif action_input in ['e', 'E']:
        print('Ir al este')
    elif action_input in ['o', 'O']:
        print('Ir al oeste')
    elif action_input in ['I', 'i']:        
        print(player.print_inventory())


    else:
        print('Acción inválida')

def get_user_command():
    return input('Accion: ')


play()




