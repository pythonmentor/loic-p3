"""Maze generate's file for MacGiver maze game."""

# -tc- Attention à respecter la PEP8 dans l'ordre des imports et la manière
# -tc- de les formater.
from random import sample, choice
import config
from lib import funct # -tc- modifier le nom de ce module et trouver un nom plus thématique


class Maze:
    """Generate the maze frame."""

    game_count = 0

    def __init__(self, nb_obj):
        """Create BadGuy status. Load maze file and create 'frame' list."""
        # Select one file randomly
        selected_level = choice(funct.list_files(config.LEVELS_REP))
        # Read .json and return a list
        self.frame = funct.string_json(selected_level)['level_']
        # Generate
        self.empty_spaces_list = []
        self.walls_spaces_list = []
        self.moves_spaces_list = []
        self.coord_lists()
        self.objects_positions(nb_obj)
        self.moves_spaces()
        # Game count
        type(self).game_count += 1

    def coord_lists(self):
        """Create lists for each sprite type."""
        # Empty spaces coordinates list:
        for x in range(len(self.frame)): # -tc- plus pythonique: for x, line in enumerate(self.frame)
            for y in range(len(self.frame)): # -tc- plus pythonique: for y, char in enumerate(line)
                if self.frame[y][x] == 'E': # -tc- si tu fais les modifications: if char == 'E'
                    self.empty_spaces_list.append((x, y)) # -tc- dans la logique de pygame, on utilise plutôt (y, x)
                elif self.frame[y][x] == 'M':
                    self.perso_start_coord = (x, y)
                elif self.frame[y][x] == 'G':
                    bad_guy_coord = ((x, y))
                    self.bad_guy_coord = bad_guy_coord
                elif self.frame[y][x] == 'O':
                    outdoor_coord = ((x, y))
                    self.outdoor_coord = outdoor_coord

                # -tc- construire une liste des murs peut également être pratique 
                # -tc- pour construire l'interface graphique



    def objects_positions(self, nb_obj):
        """Create a dictionnary of objects coord."""
        # Objects coordinates list:
        list_coord_obj = sample(self.empty_spaces_list, nb_obj)
        # Create dictionary of objects positions : 'obj'i+1:(x,y)
        self.dict_obj = {}
        for i in range(nb_obj):
            self.dict_obj['obj' + str(i + 1)] = list_coord_obj[i]

        # -tc- personnellement, je ferais le contraire, je mettrais la position
        # -tc- de l'objet en clé et le nom en valeur. Cela permet de très 
        # -tc- rapidement tester si macgyver est positionné sur la cas d'un
        # -tc- objet.

    def moves_spaces(self):
        """Create list of moves spaces."""
        self.moves_spaces_list = self.empty_spaces_list
        self.moves_spaces_list.append(self.perso_start_coord)
        self.moves_spaces_list.append(self.bad_guy_coord)
        self.moves_spaces_list.append(self.outdoor_coord)


    @classmethod
    def print_count(cls):
        if cls.game_count == 1:
            print(f"You played {cls.game_count} game.")
        else:
            print(f"You played {cls.game_count} games.")

        # -tc- dommage de mettre des prints dans une classe de modèle
