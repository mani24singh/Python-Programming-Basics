class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def diplayAvailableBooks(self):
        print("The Books available in the Library are : \n")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"The Book-({bookName}) has been issued under your name. Please keep it safe and return it within 30 days period. Thank You.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry!!.. The requested book is not available at library currently, or has been issued to someone else. Kindly wait for the book availability in future.")
            return False
        
    def returnBook(self, bookName):
        print("Thank-you for returning/donating this book!!.. We hope you have enjoyed reading it. And wish you a great day ahead. ")
        self.books.append(bookName)


class Student:
    def requestBook(self):
        self.book = input("Please Enter the name of the book you want to borrow : ")
        return self.book

    def returnBook(self):
        self.book = input("Please Enter the name of the book you want to return : ")
        return self.book

if __name__ == "__main__":

    GeniusLibrary = Library(["To kill a Mockingbird", "The Great Gatsby", "Pride and Prejudice",
     "War and Peace", "The Lord of the Rings", "A passage to india", "Jane Eyre", "Alice in Wonderland",
     "Brave New World", "Beloved", "Invisible Man", "The Grapes of wrath", "Animal Farm", "David Copperfield"])

    student = Student()
    
    while (True):
        welcomeMessage = '''\n ======== Welcome To Genius-Library ========
        Please choose an option desired :
        1. List all the Books.
        2. Request a Book.
        3. Add/Return a Book.
        4. Exit the Library.
        '''
        print(welcomeMessage)

        a = int(input("Enter a choice : "))

        if a == 1:
            GeniusLibrary.diplayAvailableBooks()

        elif a == 2:
            GeniusLibrary.borrowBook(student.requestBook())

        elif a == 3:
            GeniusLibrary.returnBook(student.returnBook())

        elif a == 4:
            print("Thanks for choosing Genius-Library. We hope you liked our service. Have a nice day!!")
            exit()

        else:
            print("Invalid Choice. Please select a valid input.")









