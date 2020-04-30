"""Generic functions for MacGiver maze game."""
from os import listdir
from os.path import isfile, join
import json
import pygame
from os import path


def list_files(path):
    """Make list of all path files in a directory."""
    files_list = [join(path, f) for f in listdir(path)
                  if isfile(join(path, f))]
    return files_list


def string_json(path):
    """Read a .json and return a dictionary."""
    with open(path) as json_data:
        data_dict = json.load(json_data)
        return data_dict


dict_ = {}


def name_inc(name, n, value):
    """Create dictionary with key name increment."""
    dict_[name+str(n)] = value
    return dict_


def py_img(path):
    """Convert images for pygame."""
    py_img = pygame.image.load(path).convert_alpha()
    return py_img


def file_name(adress):
    """Return the name of a file, without extension."""
    file_name = path.basename(path.splitext(adress)[0])
    return file_name