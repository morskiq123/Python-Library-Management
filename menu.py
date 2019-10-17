#Library systemB
#By Angel Yotov
#Began 01.12.2018
#Finished 12.12.2018

## The main menu, where the application is supposed to start
from tkinter import *
from tkinter import ttk
import bookcheckout
import booksearch
import bookreturn
import bookweed

def main():
    ## Main window
    root = Tk()
    root.title("Library menu")
    root.resizable(False, False)

    ## Frame to organise the widgets
    frame = ttk.Frame(root, relief = SUNKEN)
    frame.pack(fill = BOTH , expand = True, anchor = N)

    ## Exit button; closes the application
    exitButton = ttk.Button(frame, text = 'Exit', command = quit)
    exitButton.grid(row = 0, column = 0, stick = 'w',padx = 5, pady = 5)

    ## Greetings label
    greetingsLabel = ttk.Label(frame,text = "Welcome to the Library menu")
    greetingsLabel.grid(row = 1, column = 1,padx = 10)

    ## Button for checking book availability, opens booksearch.py
    booksAvailable = ttk.Button(frame, text = "See available books", command = booksearch.main)
    booksAvailable.grid(row = 2, column = 0, padx = 10, pady = 10)

    ## Button for getting books, opens getbook.py
    getBook = ttk.Button(frame, text = "Get a book", command = bookcheckout.main)
    getBook.grid(row = 2, column = 1, pady = 10)

    ## Button for returnig books, opens bookreturn.py
    returnBook = ttk.Button(frame, text = "Return your book", command = bookreturn.main)
    returnBook.grid(row = 2, column = 2, pady = 10)


    # Button to access weedbooks.py
    weedButton = ttk.Button(frame, text = 'Weed books', command = bookweed.main)
    weedButton.grid(row = 3, column = 1)

    ## Positioning of the main window when program starts
    root.geometry("+400+250")
    root.geometry("550x150")
    root.mainloop()

## For testing purpouses
if __name__ == '__main__':
    main()
