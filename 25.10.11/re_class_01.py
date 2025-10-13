class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available
    def borrow(self):
        if self.is_available:
            print("대출 되었습니다")
            self.is_available = False            
            return self.is_available
        else:
            print("이미 대출중인 책입니다.")
    def return_book(self):
        print("반납 되었습니다.")
        self.is_available = True
        return self.is_available
    def info(self):
        if self.is_available == True:
            available = "가능"
        else :
            available = "불가능"
        print(f"(제목 : {self.title} | 저자 : {self.author} | 대출여부 : {available}")

class Library:
    def __init__(self):
        self.book_list=[]
        self.book_dict={}

    def add_book(self,book):
        self.book_list.appned(book)
        self.book_dict[book.title] = book

library = Library()

book1 = Book("햄릿","윌리엄 셰익스피어",True)
book2 = Book("오셀로","윌리엄 셰익스피어",False)
book3 = Book("맥베스","윌리엄 셰익스피어",True)
book4 = Book("리어왕","윌리엄 셰익스피어",True)


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
