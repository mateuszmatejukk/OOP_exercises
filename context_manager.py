class Library():
    def __init__(self):
        print('Init')
        self.authorised = False
        self.books = ['book1', 'book2', 'book3']

    def __str__(self):
        if self.authorised:
            return str(self.books)
        return "Not Authorised"

    def __enter__(self):
        self.authorised = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.authorised = False


# library = Library()
# library = library.__enter__()
# print("Inside")
# print(library)
# library.__exit__(None, None, None)
# print("Outside")
# print(library) # should return Not Authorised


with Library() as library:  # library.__enter__()
    print("Inside")
    print(library)  # library.__exit__(..., ...., ...., ...)
print("Outside")
print(library)  # should return Not Authorised
