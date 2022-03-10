#!/usr/bin/env python3

from UI import *
from tkinter import *

"""
Module Docstring
"""

__author__ = "Julian Vos"
__version__ = "0.1.0"
__license__ = "MIT"


def SongsterrTabVisualiser():
    """ Main entry point of the app """

    root = Tk()

    UI(root)

    root.mainloop()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    SongsterrTabVisualiser()
