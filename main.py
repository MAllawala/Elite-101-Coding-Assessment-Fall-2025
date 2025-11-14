from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def available_books():
    #Initialize the list for holding the available books
    available_list = []

    # A for loop for iterating through eack book
    for book in library_books:
        #An if statement to check if avaiable or not
        if book["available"] == True:
            available_list.append(book)
    # Print the details of the books
    for book in available_list:
        print(f"{book['id']} {book['title']} {book['author']}")
    
available_books()

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search_book():
    #Ask user for genre or author
    user_input = input("Enter book author or genre. ").lower()
    # For loop to iterate through the books
    for book in library_books:
        #If statement to check if genre or author 
        
        #Made the value of genre and author for all books lower case
        genre = book["genre"].lower()
        author = book["author"].lower()

        if user_input == genre or user_input == author:
            print(f"{book['id']} {book['title']} {book['author']}")

search_book()

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
