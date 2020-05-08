# P3-MacGyver
## Help MacGyver escape!
### Presentation
It is a personal learning project.  
This is project 3 of the Application Developer - Python, by Openclassrooms.  
The goal was to make a python coded labyrinth.

[Openclassrooms - Help MacGyver escape!](https://openclassrooms.com/en/projects/156/assignment)

### Principle of the game:
To exit the labyrinth the player must collect all the objects before meeting the guard, put him to sleep and thus have access to the exit.

---
### Prerequisite:
```
-tc- un prérequis est tout d'abord de créer et d'activer un environnement virtuel avec pipenv shell ou python3 -m venv venv (sous macos ou linux) / py -m venv venv (sous windows) puis source venv/bin/activate (macos et linux) / venv\Scripts\activate (sous windows). L'approche recommandée par la doc python est d'utiliser pipenv pour gérer les dépendances.
```
You can install the required files with "pip install -r requirements.txt".  
Required module :  
- pygame ```-tc- pas besoin de le mentionner si dans le requirements.txt```

### Launch:
Launch the game with "python3 macgyver.py" ```-tc- python3 n'existe pas sous windows ```

### Project structure:
The organization of the program is made up of several modules, each with very specific functionalities.

- macgyver.py: has the main function which calls the other modules and contains the game loop.
- config.py: contains the program constants, indicates the path of the folders containing the images.
- maze.py: generates the labyrinth and what is there.
- player.py: contains the rules for moving and manages the pickup of objects.
- display.py: takes care of the loading of the images and the display by the pygame module.
---
### Version features:
__Choose number of objects__  
Before playing, a menu invite the player to choose the number of objects.  
The player must then collect them all before confronting the Guardian.

__Replay__  
When the game end, the player is invite to choose if he want to play again.

__New labyrinths__  
It is possible to add new labyrinths, in the 'levels' folder, respecting the structure and putting it in .json format.  
The program then automatically loads a random labyrinth among the files present in the folder.  

Structure of the labyrinth: a square of 15 sprites out of 15 sprites, where:
- W: is a wall,
- E: is an empty box,
- M: is the starting position of MacGyver,
- B: is the Guardian,
- O: is the exit, it must be next to the Guardian (so that an object cannot be in between).
