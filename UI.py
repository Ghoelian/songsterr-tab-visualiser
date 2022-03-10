from tkinter import *
from tkinter import ttk
from API import *


class UI:
    def __init__(self, master):
        self.api = API()

        self.master = master

        master.title("Search Songsterr")

        mainframe = ttk.Frame(master, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        self.query = StringVar()

        ttk.Label(mainframe, text="Search",
                  padding="0 0 5 0").grid(column=1, row=1)

        queryEntry = ttk.Entry(mainframe, width=14, textvariable=self.query)
        queryEntry.grid(column=2, row=1)

        songList = ttk.Label(mainframe).grid(column=1, row=2)

        master.bind("<Return>", self.search)

        queryEntry.focus()

    def search(self, *args):
        songs = self.api.getSongs(self.query.get())

        for song in songs:
            print(song)
