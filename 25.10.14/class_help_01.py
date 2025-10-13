# ==============================
# Book 클래스
# ==============================
class Book:
    def __init__(self, title, author):
        # 책은 "정보"만 가진다 (수량은 Library가 관리)
        self.title = title
        self.author = author

    def info(self):
        # Book 자체는 수량을 모른다 → Library가 출력 시 수량 포함해서 보여줄 것
        print(f"[{self.title} - {self.author}]")


# ==============================
# Library 클래스
# ==============================
class Library:
    def __init__(self):
        self.book_list = []  # Book 객체를 순서대로 저장 (출력/정렬용)
        self.book_dict = {}  # (title, author) → {"book": Book, "count": n}

    # ------------------------------
    # 1) 책 추가 (중복 시 count 증가)
    # ------------------------------
    def add_book(self, book):
        key = (book.title, book.author)

        # 이미 있는 책이면 수량만 +1
        if key in self.book_dict:
            self.book_dict[key]["count"] += 1
            print(f"'{book.title}' 수량이 1 증가했습니다. (총 {self.book_dict[key]['count']}권)")
        else:
            # 새 책이면 list와 dict 모두에 추가
            self.book_list.append(book)
            self.book_dict[key] = {"book": book, "count": 1}
            print(f"'{book.title}' 책이 도서관에 추가되었습니다.")

    # ------------------------------
    # 2) 전체 책 목록 표시 (수량 포함)
    # ------------------------------
    def show_all_books(self):
        if not self.book_list:
            print("도서관에 책이 없습니다.")
            return

        print("=== 도서관 보유 도서 목록 ===")
        for book in self.book_list:
            key = (book.title, book.author)
            count = self.book_dict[key]["count"]
            print(f"[{book.title} - {book.author}] | 수량: {count}권")
        print("============================")

    # ------------------------------
    # 3) 제목으로 책 검색 (여러 권 가능)
    # ------------------------------
    def search_by_title(self, title):
        result = []
        for key, info in self.book_dict.items():
            if key[0] == title:  # key[0] = title
                result.append(info["book"])

        if result:
            print(f"'{title}' 제목으로 {len(result)}권을 찾았습니다.")
            for book in result:
                key = (book.title, book.author)
                count = self.book_dict[key]["count"]
                print(f"[{book.title} - {book.author}] | 수량: {count}권")
            return result
        else:
            print("책이 존재하지 않습니다.")
            return None

    # ------------------------------
    # 4) 저자로 책 검색 (여러 권 가능)
    # ------------------------------
    def search_by_author(self, author):
        result = []
        for key, info in self.book_dict.items():
            if key[1] == author:  # key[1] = author
                result.append(info["book"])

        if result:
            print(f"'{author}' 저자의 책 {len(result)}권을 찾았습니다.")
            for book in result:
                key = (book.title, book.author)
                count = self.book_dict[key]["count"]
                print(f"[{book.title} - {book.author}] | 수량: {count}권")
            return result
        else:
            print("책이 존재하지 않습니다.")
            return None

    # ------------------------------
    # 5) 책 대출 (count > 0이면 -1)
    # ------------------------------
    def borrow(self, title):
        for key, info in self.book_dict.items():
            if key[0] == title:
                if info["count"] > 0:
                    info["count"] -= 1
                    print(f"'{title}' 책을 1권 대출했습니다. (남은 수량: {info['count']}권)")

                    # 수량이 0이 되면 리스트에서도 삭제 (보여줄 필요 없음)
                    if info["count"] == 0:
                        self.book_list.remove(info["book"])
                        print(f"'{title}' 책의 모든 수량이 대출되어 목록에서 제거됩니다.")
                        del self.book_dict[key]
                    return
                else:
                    print("책 수량이 0이라 대출할 수 없습니다.")
                    return
        print("존재하지 않는 책입니다.")

    # ------------------------------
    # 6) 책 반납 (count + 1, 새로 추가되면 리스트에도 다시 추가)
    # ------------------------------
    def return_book(self, title, author):
        key = (title, author)
        if key in self.book_dict:
            self.book_dict[key]["count"] += 1
            print(f"'{title}' 책이 1권 반납되었습니다. (수량: {self.book_dict[key]['count']}권)")
        else:
            # 책이 아예 없던 경우, 새로 추가
            new_book = Book(title, author)
            self.book_list.append(new_book)
            self.book_dict[key] = {"book": new_book, "count": 1}
            print(f"'{title}' 책이 반납되어 새로 등록되었습니다. (수량: 1권)")

    # ------------------------------
    # 7) 책 삭제 (count - 1, 0이면 완전 삭제)
    # ------------------------------
    def remove_book(self, title):
        for key, info in self.book_dict.items():
            if key[0] == title:
                info["count"] -= 1
                print(f"'{title}' 책을 1권 삭제했습니다. (남은 수량: {info['count']}권)")

                if info["count"] == 0:
                    self.book_list.remove(info["book"])
                    del self.book_dict[key]
                    print(f"'{title}' 책의 모든 수량이 사라져 도서관에서 제거되었습니다.")
                return
        print("존재하지 않는 책입니다.")

    # ------------------------------
    # 8) 제목순 정렬
    # ------------------------------
    def sort_by_title(self):
        self.book_list.sort(key=lambda book: book.title)
        print("제목순으로 정렬되었습니다.")

    # ------------------------------
    # 9) 저자순 정렬
    # ------------------------------
    def sort_by_author(self):
        self.book_list.sort(key=lambda book: book.author)
        print("저자순으로 정렬되었습니다.")


# ==============================
# 사용 예시
# ==============================
lib = Library()

book1 = Book("햄릿", "셰익스피어")
book2 = Book("햄릿", "셰익스피어")
book3 = Book("어린왕자", "생텍쥐페리")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

lib.show_all_books()

lib.borrow("햄릿")
lib.show_all_books()

lib.return_book("햄릿", "셰익스피어")
lib.show_all_books()

lib.remove_book("어린왕자")
lib.show_all_books()
