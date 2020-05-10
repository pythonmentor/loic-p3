"""Main file for MacGiver maze game."""

# -tc- Attention à respecter la PEP8 dans l'ordre des imports et la manière
# -tc- de les formater. Utiliser des parenthèses plutôt que des \ poour les
# -tc- import sur plusieurs lignes
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE,\
                          K_UP, K_DOWN, K_LEFT, K_RIGHT,\
                          K_F1, K_F2
import config
from maze import Maze
from player import Player
from display import Display_mess, Display_maze

# -tc- définir la logique du jeu dans une classe me semblerait une bonne idée.
# -tc- Cela permettrait d'instancier les objets du jeu dans la méthode
# -tc- d'initialisation puis d'utiliser une méthode pour chaque phase du jeu,
# -tc- plutôt que d'avoir une logique complexe composée de boucles imbriquée.

# -tc- Une fonction qui dépasse un demi-écran (voir max un écran) est une 
# -tc- mauvaise idée. Ma politique est de factoriser si dépasse 20 lignes.
def main():
    """Launch functions."""
    # Launch pygame
    pygame.init()

    # Pygame parameters
    pygame.key.set_repeat(config.KEY_SET_REPEAT_DELAY,
                          config.KEY_SET_REPEAT_INTERVAL)
    pygame.time.Clock().tick(config.TIME_CLOCK_TICK)

    # -tc- si big_loop, game_loop et menu_loop sont des booléan, utiliser
    # -tc- True/False. Plus proche de l'intension et donc plus lisible.
    big_loop = 1 
    while big_loop:
        game_loop = 1
        menu_loop = 1
        if Maze.game_count != 0:
            Maze.print_count() # -tc- faire les prints directement ici et pas
            # -tc- dans Maze. Par ailleurs, quel intérêt de faire des prints
            # -tc- dans le programme pygame

        # MENU LOOP ##########################################
        while menu_loop:
            nb_obj = 0
            message = Display_mess()
            message.display_message(config.MENU_MESS)
            for event in pygame.event.get():
                # Close window
                 # -tc- utiliser des parenthèses plutôt qu'un \
                if event.type == QUIT \
                 or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    menu_loop = 0 # -tc- False
                    big_loop = 0 # -tc- False
                # Choose number of objects
                elif event.type == KEYDOWN:
                    if event.key == K_F1: # créer un dictionnaire de config pour les niveau est simplement obtenir la valeur de nb_obj de ce dictionnaire
                        nb_obj = 3
                        menu_loop = 0
                    elif event.key == K_F2:
                        nb_obj = 4
                        menu_loop = 0
        # END MENU LOOP ######################################

        # Loads
        if nb_obj != 0:
            # Load & generate the maze from the file
            level = Maze(nb_obj)
            # Manage player movements and generate inventory
            player = Player(level)
            # Display the maze
            display_maze = Display_maze(level, player)

            # GAME LOOP ##########################################
            while game_loop:
                for event in pygame.event.get():
                    # Back to menu
                    if event.type == QUIT \
                     or (event.type == KEYDOWN
                       and event.key == K_ESCAPE):
                        game_loop = 0
                    # Movements reactions
                    keys_events = {
                     'UP': K_UP,
                     'DOWN': K_DOWN,
                     'LEFT': K_LEFT,
                     'RIGHT': K_RIGHT,
                    }
                    if event.type == KEYDOWN:
                        for move, value in keys_events.items():
                            if event.key == value:
                                player.movement(move, level)

                # Add loot in Inventory
                player.loot(level)
                # Re-paste images
                # -tc- Pourquoi redessine tu l'ensemble du labyrinthe à chaque
                # -tc- tour de boucle. Il suffit de dessiner un background
                # -tc- avec le labyrinthe au début du programme avec les 
                # -tc- éléments qui ne bougent pas. Après, tu utilises des
                # -tc- classes qui héritent de pygame.sprite.Sprite et tu 
                # -tc- les stocke dans un pygame.sprite.Group. Tu pourras
                # -tc- manipuler leur affichage de manière beaucoup plus propre
                # -tc- et idiomatique.
                display_maze.repaste_display(level, player)

                # Meeting BadGuy
                # -tc- avoir un player.position sous forme de tuple semble plus
                # -tc- logique au vu de ce que tu as fais dans maze.py
                if (player.x, player.y) == level.coord_badguy:
                    # Check inventory
                    if len(player.inventory_list) != nb_obj:
                        message.display_message(config.LOOSE_MESS)
                        # -tc- utiliser des parenthèses plutôt qu'un \
                        for event in pygame.event.get():
                            # Close window
                            # -tc- utiliser des parenthèses plutôt qu'un \
                            if event.type == QUIT \
                             or (event.type == KEYDOWN
                               and event.key == K_ESCAPE):
                                game_loop = 0 # -tc- False
                                big_loop = 0# -tc- False
                            # Choose replay or quit
                            elif event.type == KEYDOWN:
                                if event.key == K_F1: # -tc- ton code est très très répétitif. Code déjà vu plus haut. Tu peux factoriser très facilement
                                    game_loop = 0# -tc- False
                                elif event.key == K_F2:
                                    game_loop = 0# -tc- False
                                    big_loop = 0# -tc- False
                    else:
                        display_maze.badguy_sleeping = True

                # Check Exit
                if (player.x, player.y) == level.outdoor_coord:
                    # Check if badguy is sleeping
                    for event in pygame.event.get():
                        # Close window
                       # -tc- une 3e fois pratiquement le même code!!! 
                        if event.type == QUIT \
                         or (event.type == KEYDOWN
                           and event.key == K_ESCAPE):
                            game_loop = 0
                            big_loop = 0
                        # Choose replay or quit
                        elif event.type == KEYDOWN:
                            if event.key == K_F1:
                                game_loop = 0
                            if event.key == K_F2:
                                game_loop = 0
                                big_loop = 0
                    if display_maze.badguy_sleeping is True:
                        message.display_message(config.WIN_MESS)
                    else:
                        message.display_message(config.CHEAT_MESS)
            # END GAME LOOP ######################################


if __name__ == "__main__":

    main()
