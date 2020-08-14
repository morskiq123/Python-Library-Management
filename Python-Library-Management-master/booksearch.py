#Library system
#By Angel Yotov
#Began 01.12.2018
#Finished 12.12.2018

## This is the module that is used for looking up the desired books
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def titleBookSearch(arg = None):
    ## Function used to search for the books via Title, accesses database.txt
    listbox.delete(0,END)
    l1 = [] ## Needed to store list of database
    userInput = (titleEntry.get())
    data = open("database.txt","r")
    for line in data:
        line = line.strip("\n")
        line = line.split("/")
        l1.append(line)
    data.close()
    for line in l1:
        if userInput == line[1]:
            listbox.insert(END,"ID: " + line[0])
            listbox.insert(END,"Book: "+ userInput)
            listbox.insert(END,"Author: "+ line[2])
            if line[3] == '1':
                listbox.insert(END,"Book available for loan")
            else:
                listbox.insert(END,"Book not available for loan")
    titleEntry.delete(0,END)




def authorBookSearch(arg = None):
    ## Function used to search for the books via Author, accesses database.txt
    listbox.delete(0,END)
    l1 = [] ## Needed to store list of database
    userInput = (authorEntry.get())
    data = open("database.txt","r")
    for line in data:
        line = line.strip("\n")
        line = line.split("/")
        l1.append(line)
    data.close()
    for line in l1:
        if userInput == line[2]:
            listbox.insert(END,"ID: " + line[0])
            listbox.insert(END,"Book: "+ line[1])
            listbox.insert(END,"Author: "+ userInput)
            if line[3] == '1':
                listbox.insert(END,"Book available for loan")
            else:
                listbox.insert(END,"Book not available for loan")
    authorEntry.delete(0,END)

def idBookSearch(arg = None):
    ## Function used to search for the books via ID, accesses database.txt
    listbox.delete(0,END)
    l1 = [] ## Needed to store list of database
    userInput = (idEntry.get())
    data = open("database.txt","r")
    for line in data:
        line = line.strip("\n")
        line = line.split("/")
        l1.append(line)
    data.close()
    for line in l1:
        if userInput == line[0]:
            listbox.insert(END,"ID: " + userInput)
            listbox.insert(END,"Book: "+ line[1])
            listbox.insert(END,"Author: "+ line[2])
            if line[3] == '1':
                listbox.insert(END,"Book available for loan")
            else:
                listbox.insert(END,"Book not available for loan")
    idEntry.delete(0,END)

def showAll(arg = None):
    ## Function used to display all the books in the database.txt file
    listbox.delete(0,END)
    l1 = []
    data = open("database.txt","r")
    for line in data:
        line = line.strip("\n")
        line = line.split("/")
        l1.append(line)
    data.close()
    for line in l1:
        listbox.insert(END,"ID: " + line[0])
        listbox.insert(END,"Book: " + line[1])
        listbox.insert(END,"Author: "+ line[2])

        if line[3] == '1':
            listbox.insert(END,"Book available for loan")
            listbox.insert(END, "\n")
        else:
            listbox.insert(END,"Book not available for loan")
            listbox.insert(END, "\n")
def main():
    ## Creates the window
    global rootSearch
    rootSearch = Tk()
    rootSearch.title("Book search")

    ## Frame to put the widgets
    frame = ttk.Frame(rootSearch, relief = SUNKEN)
    frame.pack(fill=BOTH, expand = True)

    ## Buttons
    backButton = ttk.Button(frame,text = "Go back", command = rootSearch.destroy)
    backButton.grid(row = 0,column = 0, pady = 5,padx = 5, stick = 'w')

    idButton = ttk.Button(frame, text = "Enter")
    idButton.grid(row = 1, column = 2,stick = 'w')
    idButton.config(command = idBookSearch)

    authorButton = ttk.Button(frame, text = "Enter")
    authorButton.grid(row = 2, column = 2,stick = 'w')
    authorButton.config(command = authorBookSearch)

    titleButton = ttk.Button(frame,text = "Enter")
    titleButton.grid(row = 3, column = 2, stick = 'w')
    titleButton.config(command = titleBookSearch)

    allButton = ttk.Button(frame, text = "Display all books", command = showAll)
    allButton.grid(row = 5, column = 0, columnspan = 3, pady = 5 )

    ## Labels
    idSearch = ttk.Label(frame, text = "Search by ID")
    idSearch.grid(row = 1,column = 0,stick = 'e')

    authorSearch = ttk.Label(frame,text = "Search by author's name")
    authorSearch.grid(row = 2, column = 0, padx= 5,stick = 'e')

    titleSearch = ttk.Label(frame, text = "Search by book title")
    titleSearch.grid(row = 3, column = 0, stick = 'e')

    ## Entrys
    global idEntry
    idEntry = ttk.Entry(frame, width = 15)
    idEntry.grid(row = 1, column = 1, pady = 5)
    idEntry.bind('<Return>',idBookSearch)

    global authorEntry
    authorEntry = ttk.Entry(frame, width = 15)
    authorEntry.grid(row = 2, column = 1)
    authorEntry.bind('<Return>',authorBookSearch)

    global titleEntry
    titleEntry = ttk.Entry(frame, width = 15)
    titleEntry.grid(row = 3, column = 1,  pady = 5)
    titleEntry.bind('<Return>',titleBookSearch)

    ## Listbox
    global listbox
    listbox = Listbox(frame)
    listbox.grid(row = 4, column = 0, columnspan = 4)

    ## Adjusting size for the window
    rootSearch.geometry("+400+250")
    rootSearch.geometry("410x350")
    rootSearch.mainloop()

## For testing purpouses
if __name__ == '__main__':
    main()
