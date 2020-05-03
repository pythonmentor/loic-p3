"""Generic functions for MacGiver maze game."""
from os import listdir
from os.path import basename, isfile, join, splitext
from json import load
from pygame import image


def list_files(path):
    """Make list of all path files in a directory."""
    files_list = [join(path, f) for f in listdir(path)
                  if isfile(join(path, f))]
    return files_list


def string_json(path):
    """Read a .json and return a dictionary."""
    with open(path) as json_data:
        data_dict = load(json_data)
        return data_dict


def py_img(path):
    """Convert images for pygame."""
    py_img = image.load(path).convert_alpha()
    return py_img


def file_name(path):
    """Return the name of a file, without extension."""
    file_name = basename(splitext(path)[0])
    return file_name
