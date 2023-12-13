# TODO Найдите количество книг, которое можно разместить на дискете

bites_for_one_symbol = 4
count_of_symbols_in_line = 25
count_of_lines_in_page = 50
count_of_pages_in_book = 100
floppy_disk_capacity = 1.44

bites_in_book = bites_for_one_symbol * count_of_symbols_in_line *count_of_lines_in_page * count_of_pages_in_book
book_capacity = bites_in_book / 1024 / 1024
number_of_books = round(floppy_disk_capacity / book_capacity)

print("Количество книг, помещающихся на дискету:", number_of_books)
