import requests
import sys
from tabulate import tabulate
import csv

# =========================================================================================================================================
# Book Tracker
# =========================================================================================================================================
# Implementation steps
# 1. show current user library - OK
# 2. user options: 1 - add book, 2 - update book, 3 - remove book, 4 - quit - OK
# 2.1 - ask for book isbn, prompts for confirmation about adding the book to the library (will be registered on a file) - OK
# 2.1_ if the book is added to the library, add a key to the current page and the percentage of reading - OK
# 2.1__ write the book into the file to make it available even when the program is closed - OK
# 2.2 - update current book page and percentage of reading - OK
# 2.2 - update csv file with the current book page and percentage - OK
# 2.3 - remove book from the library - OK
# 2.4 - quit the program - OK
# main


def main():
    # 9780261102736 - The Silmarillion
    # 9780007309368 - The Children of Hurin
    # 9780439023481 - The Hunger Games

    # construction of user library based on the file
    user_lib = []
    with open("user_library.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_lib.append({"Title": row["Title"], "Author": row["Author"], "Pages": int(row["Pages"]),
                             "Current Page": int(row["Current Page"]), "Percentage": row["Percentage"], "Publish Date": row["Publish Date"]})
    while True:
        # print user library
        if len(user_lib) > 0:
            # current view of the library
            book_library = tabulate(user_lib, headers = "keys", tablefmt = "grid")
            print(f"\nUser Library\n{book_library}\n")
        # give the user options
        options_str = "Options:\n1 - Add a new book\n2 - Update the progress of a book\n3 - Remove book\n4 - Quit"
        print(options_str)
        chosen_option = input("Which option do you want to select? ")
        if chosen_option == "1":
            book_isbn = input("Book ISBN: ")
            book_dict = get_book_info(book_isbn)
            # delete some dictionary keys to print the book
            aux_dict = book_dict.copy()
            del aux_dict["Current Page"]
            del aux_dict["Percentage"]
            book_dict_formatted = [aux_dict]
            book_dict_formatted = tabulate(book_dict_formatted, headers = "keys", tablefmt = "grid")
            print(f"\n{book_dict_formatted}\n")
            yes_no = input("Do you want to add this book to your library? (y/n) ")
            if yes_no == "y":
                user_lib.append(book_dict)
            elif yes_no == "q":
                break
            else:
                print("The book was not added to your library")
        elif chosen_option == "2":
            print("\nAvailable Books")
            for i in range(len(user_lib)):
                print(f"{i + 1} - {user_lib[i]['Title']}")
            chosen_book = int(input("Select an available book index: "))
            index = chosen_book - 1
            current_page = int(input("Type the page you are current reading: "))
            user_lib = update_current_page(index, user_lib, current_page)
        elif chosen_option == "3":
            print("\nAvailable Books")
            for i in range(len(user_lib)):
                print(f"{i + 1} - {user_lib[i]['Title']}")
            chosen_book = int(input("Select an available book index: "))
            index = chosen_book - 1
            user_lib = remove_book(index, user_lib)
        elif chosen_option == "4":
            quit_input = input("Are you sure you want to quit? (y/n) ")
            if quit_input == "y":
                update_library_file(user_lib)
                print("Exiting...")
                return False
        else:
            print("You need to enter a valid option")
            return False


def get_book_info(book_isbn):
    # handle empty input
    if book_isbn == "":
        sys.exit("Empty Input")
    # get book information from an API
    try:
        response = requests.get(f"https://openlibrary.org/api/books?bibkeys=ISBN:{book_isbn}&jscmd=data&format=json")
    except requests.RequestException:
        sys.exit("Error")
    except KeyError:
        sys.exit("Error")
    else:
        # create a dictionary to store the book information
        book_dict = {}
        try:
            book_title = response.json()[f"ISBN:{book_isbn}"]["title"]
        except KeyError:
            sys.exit("ISBN Input Error")
        book_author = response.json()[f"ISBN:{book_isbn}"]["authors"][0]["name"]
        try:
            book_pages = response.json()[f"ISBN:{book_isbn}"]["number_of_pages"]
        except KeyError:
            book_pages = int(input("Please enter the number of pages of your book: "))
        book_date = response.json()[f"ISBN:{book_isbn}"]["publish_date"]
        book_dict = {'Title': book_title, 'Author': book_author, 'Pages': book_pages, 'Current Page': 0, 'Percentage': '0%','Publish Date': book_date}

        return book_dict


def update_current_page(index, book_lib, current_page):
    if index < len(book_lib):
        if current_page > book_lib[index]["Pages"]:
            print("The entered page is invalid!")
        else:
            book_lib[index]["Current Page"] = current_page
            book_percentage = round(current_page * 100 / book_lib[index]["Pages"], 2)
            book_lib[index]["Percentage"] = f"{book_percentage}%"
    else:
        print("The entered option is invalid!")

    return book_lib


def remove_book(index, book_lib):
    if index < len(book_lib):
        book_lib.pop(index)
    else:
        print("The entered option is invalid!")

    return book_lib

def update_library_file(book_lib):
    header = ["Title", "Author", "Pages", "Current Page", "Percentage", "Publish Date"]
    with open("user_library.csv", "w") as file:
        writer = csv.writer(file)
        # only print the header if there is at least one entry in the user library
        if len(book_lib) != 0:
            writer.writerow(header)
        for i in range(len(book_lib)):
            writer.writerow(book_lib[i].values())

if __name__ == "__main__":
    main()