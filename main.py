from data import load_job_data
from list_CRUD import *

jobs = load_job_data()
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
            edit_job(jobs)
        case '4':
            delete_job(jobs)
        case '5':
            print("Closing the program")
            break
        case _:
            print("Unavailable option. Try again")