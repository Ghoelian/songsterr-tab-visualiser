from tkinter import *
from tkinter import ttk
from API import *


class UI:
    def __init__(self, master):
        self.api = API()

        self.master = master

        self.master.title("Search Songsterr")

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        mainFrame = ttk.Frame(self.master)
        mainFrame.grid(column=0, row=0, sticky="nesw")

        mainFrame.columnconfigure(0, weight=1)
        mainFrame.rowconfigure(1, weight=1)

        mainFrame.option_add("*font", "Helvetica 10")

        searchFrame = ttk.Frame(mainFrame, padding="3 3 12 12")
        searchFrame.grid(column=0, row=0, sticky="ew")

        searchFrame.columnconfigure(1, weight=1)

        self.query = StringVar()

        ttk.Label(searchFrame, text="Search", font=("Helvetica", 10, "bold"),
                  padding="0 0 5 0").grid(column=0, row=0, sticky="ew")

        queryEntry = ttk.Entry(searchFrame, textvariable=self.query)
        queryEntry.grid(column=1, row=0, sticky="ew")

        resultFrame = ttk.Frame(mainFrame)
        resultFrame.grid(column=0, row=1, sticky="nesw")

        resultFrame.columnconfigure(0, weight=1)
        resultFrame.rowconfigure(0, weight=1)

        self.songList = StringVar()
        self.songList.set("")

        resultScrollbar = Scrollbar(resultFrame, orient="vertical")
        resultScrollbar.grid(column=1, row=0, sticky="ns")

        self.resultList = Listbox(
            resultFrame, yscrollcommand=resultScrollbar.set)
        self.resultList.grid(column=0, row=0, sticky="nesw")

        resultScrollbar.config(command=self.resultList.yview)

        self.master.bind("<Return>", self.search)
        self.resultList.bind("<Double-1>", self.playTab)

        queryEntry.focus()

    def search(self, *args):
        self.resultList.delete(0, END)

        self.songs = self.api.getSongs(self.query.get())
        index = 0

        for song in self.songs:
            self.resultList.insert(
                index, song["title"] + " by " + song["artist"]["name"])

            index += 1

    def playTab(self, *args):
        if(self.resultList.size() > 0):
            song = self.songs[self.resultList.curselection()[0]]

            print(self.api.getTab(song))
