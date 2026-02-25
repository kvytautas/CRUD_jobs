jobs = [
    {"id":0,
    "position":"Data analyst",
    "salary":1850,
    "location":"Vln, Kns",
    "required_skills":"sql, python, powerbi, windows, excel"},
    {"id":1,
    "position":"Expert in Test Scenario Preparation",
    "salary":3850,
    "location":"Vln, Kns, Hybrid",
    "required_skills":"Basel4, CRR3, ICAAP, ILAAP"},
    {"id":2,
    "position":"Quantitative analyst",
    "salary":4200,
    "location":"Remote",
    "required_skills":"Statistics,SAS, AI"},
    {"id":3,
    "position":"Credit Risk Officer",
    "salary":4750,
    "location":"Vln, Riga, Tallinn",
    "required_skills":"BI, R, Github"},
]
id_counter = 3

# print(jobs[1]["position"])
while True:
    print("-------------------------")
    print("Press 1 to print Jobs list")
    print("Press 2 to add a job add")
    print("Press 3 to edit a job add")
    print("Press 4 to delete a job add")
    print("Press 5 to close program.")
    print("-------------------------")
    choice = input() # string
    
    match choice:
        case '1':
            print("Jobs list:")
            for job in jobs:
                print(
                    f"{job['id']}. Position: {job['position']}  Salary: €{job['salary']:.1f} Location(s): {job['location']}  Required skills: {job['required_skills']}"
                )
        case '2':
            print("Add a job:")
            print("Type in position name:")
            position = input()
            print("Type in salary:")
            salary = int(input())
            print("Type in location:")
            location = input()
            print("Type in required skills:")
            required_skills = input()
            id_counter += 1
            new_job = {
                'id': id_counter,
                "position": position,
                "salary": salary,
                "location": location,
                "required_skills": required_skills
            }
            jobs.append(new_job)
        case '3':
            print("Edit job add")
            print('Enter job id to edit')
            edit_id = int(input())
            for job in jobs:
                if job['id'] == edit_id:
                    print("Enter new position:")
                    job['position'] = input()
                    print("Enter new salary:")
                    job['salary'] = int(input())
                    print("Enter new location:")
                    job['location'] = input()
                    print("Enter new required_skills:")
                    job['required_skills'] = input()
        case '4':
            print("Delete job position:")
            print('Select job id to delete')
            del_id = int(input())
            for job in jobs:
                if job['id'] == del_id:
                    jobs.remove(job)
                    print("Job add deleted")
                    break
        case '5':
            print("Closing the program")
            break
        case _:
            print("Unavailable option. Try again")