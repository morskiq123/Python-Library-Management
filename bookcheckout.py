#Library system
#By Angel Yotov
#Began 01.12.2018
#Finished 12.12.2018

## This is the module that is used for getting the desired books
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def idCheck(x):
    ## Checks if the user's ID is valid
    try:
        ID = int(x) ## Converts the input into an int
        if((ID < 1000) or (ID > 9999)): ## Check if the ID is of a proper value
            messagebox.showerror(title = "ERROR", message = "You have entered an invalid ID.")
            loginEntry.delete(0,END)
        else:
            messagebox.showinfo(title = "Welcome", message = "Welcome student "+userID+"! Enter the ID of the book you wish to take.")
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
    ## What happens after a successful ID has been entered
    entryLabel.grid_remove()
    loginEntry.grid_remove()
    enterButton.grid_remove()

    ## Removes the original label and entry, replaces them with book searching ones
    bookLabel = ttk.Label(frame, text = "Enter the ID of the book you wish to borrow")
    bookLabel.grid(row = 1, column = 1,pady = 10)

    global bookEntry
    bookEntry = ttk.Entry(frame, width = 5)
    bookEntry.grid(row = 2, column = 1)
    bookEntry.bind("<Return>",getBook)

    getBookButton = ttk.Button(frame,text = "Get book")
    getBookButton.grid(row = 3, column = 1)
    getBookButton.config(command = getBook)


def getBook(arg = None):
    ## Function reads through book list, then writes the ID, changes availability and logs it
    userInput = int(bookEntry.get())

    l1=[]
    data = open("database.txt","r")
    for line in data:
        line = line.strip("\n")
        line = line.split("/")
        l1.append(line)
    data.close()
    if l1[userInput-1][3] == '0':
        messagebox.showinfo(title = "Book in use", message = "The book is already in use. Sorry for the inconveninece")
    else:
        l1[userInput-1][3] = '0' ## Makes the book unavailable
        l1[userInput-1][4] = str(userID) ## Puts in the user's ID
        messagebox.showinfo(title = "Success", message = "Success. This book is now signed to your student ID")
    ## This part rewrites the database with the changes
    database = open("database.txt","w")
    for x in l1:
        database.write ("/".join(x))
        database.write("\n")
    database.close()
    bookEntry.delete(0,END)

    ## Clear list so we populate from logfile.txt
    l1.clear()
    logs = open("logfile.txt","r")
    for log in logs:
        log = log.strip("\n")
        log = log.split("/")
        l1.append(log)
    logs.close()

    ## Add one to the times taken and re-write the txt file
    timesTaken = int((l1[userInput-1][1])) + 1
    l1[userInput-1][1] = str(timesTaken)

    logfile = open("logfile.txt","w")
    for y in l1:
        logfile.write ("/".join(y))
        logfile.write("\n")
    logfile.close()


def main():
    ## Creates the main window
    rootCheckout = Tk()
    rootCheckout.title("Book lending")

    ## Frame to organise widgets
    global frame
    frame = ttk.Frame(rootCheckout, relief = SUNKEN)
    frame.pack(fill = BOTH, expand = True)

    ## Login entry
    global loginEntry
    loginEntry = ttk.Entry(frame, width = 15)
    loginEntry.bind('<Return>',getEntry)

    ## Labels
    global entryLabel
    entryLabel = ttk.Label(frame, text = "Enter your student ID")
    entryLabel.grid(row = 1, column = 1)

    ## Entries
    loginEntry = ttk.Entry(frame,width = 5)
    loginEntry.grid(row = 2, column = 1)
    loginEntry.bind("<Return>",getEntry)

    ## Buttons
    goBackButton = ttk.Button(frame, text = "Go back", command = rootCheckout.destroy)
    goBackButton.grid(row = 0, column = 0, pady = 5,padx = 5, stick = 'w')

    global enterButton
    enterButton = ttk.Button(frame, text = "Enter",command = getEntry)
    enterButton.grid(row=3, column = 1)

    ## Main window configurations
    rootCheckout.geometry("450x200")
    rootCheckout.geometry("+400+250")
    rootCheckout.mainloop()

## For testing purpouses
if __name__ == '__main__':
    main()
