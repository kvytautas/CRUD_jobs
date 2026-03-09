# from list_CRUD import *
from file_CRUD import *
# from db_CRUD import *

jobs = load_jobs()
id_counter = 3

while True:
    print_menu()
    choice = input() # string input
    match choice:
        case '1':
            print_jobs(jobs)
        case '2':
            id_counter = add_job(jobs,id_counter)
        case '3':
            print_jobs(jobs)
            edit_job(jobs)
        case '4':
            delete_job(jobs)
        case '5':
            print("Closing the program")
            break
        case _:
            print("Unavailable option. Try again")
