import pytest
from project import get_book_info, update_current_page, update_library_file

def test_get_book_info():
    # test of a book information
    assert get_book_info(9780261102736) == {'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '1999'}
    # test of another book information
    assert get_book_info(9780439023481) == {'Title': 'The Hunger Games', 'Author': 'Suzanne Collins', 'Pages': 374, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '2008-10'}
    # invalid isbn entry - empty entry
    with pytest.raises(SystemExit):
        get_book_info('')
    # invalid isbn entry - entry with letters
    with pytest.raises(SystemExit):
        get_book_info('123abc')

def test_update_current_page():
    # example of user library
    book_lib = [{'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '1999'}]
    assert update_current_page(0, book_lib, 44) == [{'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 44, 'Percentage': '9.93%', 'Publish Date': '1999'}]
    book_lib = [{'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '1999'}]
    assert update_current_page(0, book_lib, 443) == [{'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 443, 'Percentage': '100.0%', 'Publish Date': '1999'}]
    # invalid index - no changes to the book library list
    book_lib = [{'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '1999'}]
    assert update_current_page(1, book_lib, 44) == [{'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '1999'}]
    # invalid page - no changes to the book library list
    book_lib = [{'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '1999'}]
    assert update_current_page(0, book_lib, 500) == [{'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '1999'}]

def test_update_library_file():
    # test with one book
    book_lib = [{'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '1999'}]
    update_library_file(book_lib)
    with open("user_library.csv", "r") as file:
        contents = file.read()
        assert contents == "Title,Author,Pages,Current Page,Percentage,Publish Date\nThe Silmarillion,J.R.R. Tolkien,443,0,0%,1999\n"
    # test with two books
    book_lib = [{'Title': 'The Silmarillion', 'Author': 'J.R.R. Tolkien', 'Pages': 443, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '1999'},
    {'Title': 'The Hunger Games', 'Author': 'Suzanne Collins', 'Pages': 374, 'Current Page': 0, 'Percentage': '0%', 'Publish Date': '2008-10'}]
    update_library_file(book_lib)
    with open("user_library.csv", "r") as file:
        contents = file.read()
        assert contents == "Title,Author,Pages,Current Page,Percentage,Publish Date\nThe Silmarillion,J.R.R. Tolkien,443,0,0%,1999\nThe Hunger Games,Suzanne Collins,374,0,0%,2008-10\n"
    # test with no books - empty file expected
    book_lib = []
    update_library_file(book_lib)
    with open("user_library.csv", "r") as file:
        contents = file.read()
        assert contents == ""