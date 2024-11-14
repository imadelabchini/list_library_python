
# step 1 :setup
library = []
wishlist = []

#step 2: Adding Individual Books
book_name = input("\nEnter the name of a book you own: ")
library.append(book_name)

book_name = input("\nEnter the name another book you own (or press 'Enter' or skip): ")
if book_name :
     library.append(book_name)

print("Your Library: ",library)

#step 3: Managing the Wishlist
book_name = input("\nEnter the name of a book you  wish to have in the future: ")
wishlist.append(book_name)

book_name = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ")
wishlist.append(book_name)
if book_name:
     wishlist.append(book_name)

print(f"\nYour Lwishlist: {wishlist}")

#step 4: Merging Wishlist into Library
acquired_book = input("\nEnter the name of another book from your wishlist that you've acquired (oor press 'Enter' or skip): ")
if acquired_book in wishlist :
     library.append(acquired_book)
     wishlist.remove(acquired_book)

print("\nupdated Library: ",library)
print(f"updated wilshlist: {wishlist}")

#step 5:Donating books
donated_book = input("\nEnter the name of a book from your Library  youwish to donate (oor press 'Enter' or skip): ")

if donated_book in library :
     library.remove(donated_book)

print(f"\nFinal Library after donations: {library}")
