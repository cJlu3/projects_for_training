from core import create_tables, insert_data, create_book

def main():
    book1 = create_book(title='book_1',
                        author='author_of_book_1',
                        year=1111,
                        is_taken=True)
    book2 = create_book(title='book_2',
                        author='author_of_book_2',
                        year=2222)
    book_list = [book1, book2]
    
    create_tables()
    insert_data(book_list=book_list)



if __name__ == "__main__":
    main()
