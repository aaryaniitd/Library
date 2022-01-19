from helper import filereader, fileadder, fileremover
class Library:
    def __init__(self, listofbooks, name):
        self.name = name
        self.listofbooks = listofbooks
        self.lendDict = {} 

    def displaybooks(self):
        print("We have the following books in our library: \n")
        for book in filereader('Books.txt'):
            print(book)
        print("\n")
    def searchbook(self):
        bookname = input("Please type the name of the book you want to search. ")
        i = 0
        while i < len(filereader('Books.txt')):
            if bookname.casefold() == filereader('Books.txt')[i].casefold():
                print("This book is available.\n")
                break
            else:
                if i == len(filereader('Books.txt'))-1:
                    print("Sorry, this book is unavailable.\n")
                    break
                else:
                    i+= 1
            
    def lendbook(self, user, book):
        if book in self.listofbooks:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                fileremover('Books.txt', book)
                print("Lender-Book database has been updated. You can take your book.\n") 
        elif book not in self.listofbooks:
            if book in self.lendDict.keys():
                print(f"Sorry, this book is already lended to {self.lendDict[book]}.\n")
            else:
                print(f"Sorry '{book}' is not available in the library right now.")

    def addbook(self,bookname):
        fileadder('Books.txt', bookname)
        print("Thanks for donating this book to the library. \nAs per our offer, you can issue a book of your choice for an extended period of 3 weeks.\n")

    def returnbook(self,bookname):
        if bookname in self.lendDict.keys():
            self.listofbooks.append(bookname)
            del self.lendDict[bookname]
            fileadder('Books.txt',bookname)
            print("Thank You for returning this book. Please come back to read more.\n")
        else:
            print("Sorry, this book was not borrowed.\n")
        
if __name__ == '__main__':
    aaryan = Library(filereader('Books.txt'), "Aaryan's Library")

    print(f"Welcome to {aaryan.name}. Enter your choice to continue\n")
    print("1. Search a Book")
    print("2. Display All Books")
    print("3. Lend a Book")
    print("4. Return a Book")
    print("5. Donate a Book\n")
    choice = int(input())
    if choice == 1:
        print("\n")
        aaryan.searchbook()
    elif choice == 2:
        print("\n")
        aaryan.displaybooks()

    elif choice == 3:
        print("\n")
        bookname = input("Enter the name of the book you want to lend. ")
        user = input("Enter your name. ")
        aaryan.lendbook(user, bookname)

    elif choice == 4:
        print("\n")
        bookname = input("Enter the name of the book you want to return. ")
        aaryan.returnbook(bookname)

    elif choice == 5:
        print("\n")
        bookname = input("Enter the name of the book you want to donate. ")
        aaryan.addbook(bookname)

    else:
        print("\n")
        print("Sorry, but this is not a valid option.")
      
    def options():
        print("1. Search a Book")
        print("2. Display Books")
        print("3. Lend a Book")
        print("4. Return a Book")
        print("5. Donate a Book \n")
        choice = int(input())

        if choice == 1:
            print("\n")
            aaryan.searchbook()
            
        elif choice == 2:
            print("\n")
            aaryan.displaybooks()

        elif choice == 3:
            print("\n")
            bookname = input("Enter the name of the book you want to lend. ") #9927066667
            user = input("Enter your name. ")
            aaryan.lendbook(user, bookname)

        elif choice == 4:
            print("\n")
            bookname = input("Enter the name of the book you want to return. ")
            aaryan.returnbook(bookname)

        elif choice == 5:
            print("\n")
            bookname = input("Enter the name of the book you want to donate. ")
            aaryan.addbook(bookname)

        else:
            print("\n")
            print("Sorry, but this is not a valid option.")
while True:            
    temp = input("Do you want to see the available options again? ")
    if temp == "yes":
        print("\n")
        options()
    elif temp == "no":
        print("\n")
        print("Thank you for visiting our library.")
        break
    else:
        print("Sorry, this is not a valid option. ")
        
input("press enter to close")  
        
                      
