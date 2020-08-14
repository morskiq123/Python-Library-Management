MENU:

The menu provides you with access to all the functions the program has. Clicking “Exit” closes the whole program.


BOOK SEARCH:

The book searching function allows the user to check for books via ID, Author and Title. There is also a button which displays all of the available books. Underneath each book there it provides information if the book is available or not.

BOOK CHECKOUT:

Enables the user to check out a book, though first it has to ask for the user’s ID. The available ID’s range from 1000 to 9999. Anything else is invalid. The program runs through the database, changes availability of the book and logs the user currently using it. 

BOOK RETURN:

Virtually almost the same as the checking out service of this program, though instead when the user decides to return a book the program overwrites the user using the book to 0(see below) and makes the availability to 1(see below)


WEEDING:
This section of the program separates books into suggested for weeding and unfavourable. Books that have been taken less than ten(10) are suggested to be removed, whereas  books that have been taken more than ten(10) times are put into the favourable category.

NOTE!!!!!
Due to using double lists you can only delete 1 book during each session, meaning that when you delete a book you will need close the window either via the button saying “Go back” or manually, by pressing the X button on top of the window.


FORMATING FOR DATABASE.TXT

id | title | author | available (1 = True; 0 = False) | user using book (0 = no one)

FORMATING FOR LOG.TXT:

id | times taken