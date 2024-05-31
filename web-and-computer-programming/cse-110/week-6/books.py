# Instructions: For this assignment, you'll download the file books.txt that contains the names of the books in the Book of Mormon, and save it to your computer.

with open("c:/Users/rapha/my-codes/byu-codes/web-and-computer-programming/cse-110/week-6/books.txt") as books:
    for book in books:
        # Printing it line by line and strip off leading and trailing whitespace and display each book to the screen.
        print(book.strip())
