#Library system
#By Angel Yotov
#Began 01.12.2018
#Finished 12.12.2018

## This is the module to see which books are doing good and which aren't. Enables user to remove books from database aswell.
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

i=10 ## Constant INT used to compare books

def favourableBooks(arg = None):
    listbox.delete(0,END)
    listbox.insert(END,"FAVOURABLE BOOKS")
    listbox.insert(END,"\n")
    logs = open("logfile.txt","r")
    for line in logs:
        line = line.strip("\n")
        line = line.split("/")
        line[1] = int(line[1])
        if line[1] >= 10:
            line[0] = str(line[0])
            line[1] = str(line[1])
            listbox.insert(END,"Book ID: " +line[0])
            listbox.insert(END,"Times taken: "+line[1])
            listbox.insert(END,"\n")
    logs.close()

def booksForWeeding(arg = None):
    listbox.delete(0,END)
    logs = open("logfile.txt","r")
    listbox.insert(END,"BOOKS FOR WEEDING")
    listbox.insert(END,"\n")
    for line in logs:
        ine = line.strip("\n")
        line = line.split("/")
        line[1] = int(line[1])
        if line[1] < 10:
            line[0] = str(line[0])
            line[1] = str(line[1])
            listbox.insert(END,"Book ID: " +line[0])
            listbox.insert(END,"Times taken: "+line[1])
            listbox.insert(END,"\n")
    logs.close()
    label.grid(row = 5, column = 1,pady=5)
    weedEntry.grid(row = 6, column = 1)
    enterButton.grid(row = 7, column = 1,pady = 5)

def weedingBooks(arg = None):
    ## Function used for removing a book
    global l1
    l1 = []
    userInput = int(weedEntry.get())
    database = open("database.txt","r")
    for line in database:
        line = line.strip("\n")
        line = line.split("/")
        l1.append(line)
    ## The funciton where the book is removed
    if userInput == int(l1[userInput-1][0]):
        for x in range(0,len(l1)-1):
            item = l1[x]
            item_0 = int(item[0])
            if userInput == item_0:
                l1.remove(item)
                messagebox.showinfo(title = "Success", message = "The book has been removed from the database and the log")
    database = open("database.txt","w")
    for line in l1:
        database.write ("/".join(line))
        database.write("\n")
    database.close()


def main():
    ## Main window
    rootWeed = Tk()
    rootWeed.title("Weed books")
    rootWeed.resizable(False, False)

    ## Frame
    frame = ttk.Frame(rootWeed, relief = SUNKEN)
    frame.pack(fill=BOTH, expand = True)

    ## Label
    global label
    label = ttk.Label(frame, text = "Enter the ID of the book that you would wish to remove")

    ## Entry
    global weedEntry
    weedEntry = ttk.Entry(frame, width = 5)
    weedEntry.bind('<Return>',weedingBooks)

    ## Buttons
    goBackButton = ttk.Button(frame, text = "Go back", command = rootWeed.destroy)
    goBackButton.grid(row = 0, column = 0, padx = 5, pady = 5)

    prefferedBooks = ttk.Button(frame, text = "Show favourable books", command = favourableBooks)
    prefferedBooks.grid(row = 1, column = 1)

    booksForWeed = ttk.Button(frame, text = "Show books that are suggested for weeding", command = booksForWeeding)
    booksForWeed.grid(row = 4, column = 1)

    global enterButton
    enterButton = ttk.Button(frame, text = "Enter", command = weedingBooks)

    ## Listbox
    global listbox
    listbox = Listbox(frame)
    listbox.grid(row = 2, column = 1, pady = 10)

    ## Positioning of the main window when program starts
    rootWeed.geometry("+400+250")
    rootWeed.geometry("500x400")
    rootWeed.mainloop()

## For testing purpouses
if __name__ == '__main__':
    main()
