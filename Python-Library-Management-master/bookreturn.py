list#Library system
#By Angel Yotov
#Began 01.12.2018
#Finished 12.12.2018

## This module is used for returning books via the ID of the books

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def idCheck(x):
    ## Checks if the user's ID is valid
    try:
        ID = int(x) ## Converts the input into an int
        if((ID < 1000) or (ID > 9999)): ## Check if the ID is of a proper value
            messagebox.showerror(title = "ERROR", message = "You have entered an invalid ID")
            loginEntry.delete(0,END)
        else:
            messagebox.showinfo(title = "Welcome", message = "Welcome student "+userID+"! Enter the ID of the book you wish to return.")
            login()
    except ValueError: ## This part is so the code doesn't stop. The only error that can be produced is a ValueError
            messagebox.showerror(title = "ERROR", message = "You have entered an invalid ID. Please enter an integer")
            loginEntry.delete(0,END)

def getEntry(arg = None):
    ## Get text from entry box and display it to the label underneath
    global userID
    userID = loginEntry.get()
    idCheck(userID)
    loginEntry.delete(0,END)

def login():
    entryLabel.grid_remove()
    loginEntry.grid_remove()
    enterButton.grid_remove()

    ## Removes the original label and entry, replaces them with book searching ones
    bookLabel = ttk.Label(frame, text = "Enter the ID of the book you wish to return")
    bookLabel.grid(row = 1, column = 1,pady = 10)

    global bookEntry
    bookEntry = ttk.Entry(frame, width = 5)
    bookEntry.bind('<Return>',returnBook)
    bookEntry.grid(row = 2, column = 1)

    getBookButton = ttk.Button(frame,text = "Return book", command = returnBook)
    getBookButton.grid(row = 3, column = 1)

def returnBook(arg = None):
    ## Function reads through book list, logs in the return and changes the availability

    l1=[] ## Double list used in order to rewrite the database
    userInput = int(bookEntry.get())
    data = open("database.txt","r")
    for line in data:
        line = line.strip("\n")
        line = line.split("/")
        l1.append(line)
    data.close()
    if l1[userInput-1][3] == '0' and l1[userInput-1][4] != userID:
        messagebox.showerror(title = "ERROR", message = "This book is assigned to a diffrent user")
    elif l1[userInput-1][3] == '0' and l1[userInput-1][4] == userID: ## If book is unavailable and user ID matches the user using the book
        l1[userInput-1][3] = '1' ## Makes the book available after returning it
        l1[userInput-1][4] = '0' ## Resets the User ID using the book
        messagebox.showinfo(title = "Success", message = "Success. This book has now been returned")
    else:
        messagebox.showinfo(title = "Book in storage", message = "The book you are trying to return is already in storage")

    ## This part rewrites the database with the changes
    database = open("database.txt","w")
    for x in l1:
        database.write ("/".join(x))
        database.write("\n")
    database.close()
    bookEntry.delete(0,END)

def main():
    ## Creates the main window
    rootCheckout = Tk()
    rootCheckout.title("Book returning")

    ## Creates a frame to organise the widgets
    global frame
    frame = ttk.Frame(rootCheckout)
    frame.pack(fill = BOTH, expand = True)

    ## Labels
    global entryLabel
    entryLabel = ttk.Label(frame, text = "Enter your student ID")
    entryLabel.grid(row = 1, column = 1)

    ## Entries
    global loginEntry
    loginEntry = ttk.Entry(frame,width = 5)
    loginEntry.grid(row = 2, column = 1)
    loginEntry.bind("<Return>",getEntry)

    ## Buttons
    goBackButton = ttk.Button(frame, text = "Go back", command = rootCheckout.destroy)
    goBackButton.grid(row = 0, column = 0, padx = 2, pady = 5)

    global enterButton
    enterButton = ttk.Button(frame, text = "Enter", command = getEntry)
    enterButton.grid(row = 3,column = 1)

    rootCheckout.geometry("430x250")
    rootCheckout.geometry("+400+250")
    rootCheckout.mainloop()

## For testing purpouses
if __name__ == '__main__':
    main()
