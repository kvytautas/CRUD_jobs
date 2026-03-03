import csv

# headers = ['id','position','salary','location','required_skills']
# def load_jobs():
#     with open("./jobs.csv", mode="r", encoding="utf-8") as file:
#         return list(csv.DictReader(file))

headers = ['id', 'position', 'salary', 'location', 'required_skills']

def load_jobs():
    jobs = []
    with open("./jobs.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert types
            # row["id"] = int(row["id"])
            row["salary"] = int(row["salary"])

            # Convert required_skills string → list
            # Assumes CSV stores: "sql, python, excel"
            row["required_skills"] = row["required_skills"].split(", ")

            jobs.append(row)
    return jobs

def save_jobs(jobs):
    with open('./jobs.csv',mode='w',newline='',encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(jobs)

def print_menu():
    print("-------------------------")
    print("Press 1 to print jobs list")
    print("Press 2 to add a job add")
    print("Press 3 to edit a job add")
    print("Press 4 to delete a job add")
    print("Press 5 to close program.")
    print("-------------------------")

def print_jobs(jobs):
    for job in jobs:
        print(f"{job['id']}. Position: {job['position']}  Salary: €{float(job['salary']):.2f} Location(s): {job['location']}  Required skills: {job['required_skills']}")

def add_job(jobs,id_counter):
    print("Add a job")
    print("Type in position name:")
    position = input()
    print("Type in salary:")
    salary = int(input())
    print("Type in location:")
    location = input()
    print("Type in number of skills required:")
    new_skills_num = int(input())
    required_skills = []
    for i in range(new_skills_num):
        if new_skills_num == 0:
            print("No required skills")
        else:
            print(f"Enter required skill #{i+1}")
            required_skill = input()
            required_skills.append(required_skill)

    id_counter = int(jobs[-1]['id']) + 1 if len(jobs) > 0 else 1
    job = {
        'id': id_counter,
        "position": position,
        "salary": salary,
        "location": location,
        "required_skills": required_skills
    }
    jobs.append(job)
    save_jobs(jobs)
    return id_counter

def edit_job(jobs):
    print("Edit job add")
    print('Enter job id to edit')
    edit_id = input()
    for job in jobs:
        if job['id'] == edit_id:
            print("Enter new position:")
            job['position'] = input()
            print("Enter new salary:")
            job['salary'] = int(input())
            print("Enter new location:")
            job['location'] = input()
            # print("Enter new required_skills:")
            # job['required_skills'] = input()
            #########################################
            print("Enter 1 if editing all required_skills:")
            print("Enter 2 if editing single required_skill:")
            edit_choice = int(input())
            if edit_choice == 1:
                for i in range(len(job["required_skills"])):
                    print(f"Enter new skill #{i + 1}")
                    job["required_skills"][i] = input()

                    # print(f"Enter new skill #{i + 1}")
                    # job["required_skills"][i] = input()
            elif edit_choice == 2:
                print(f"Enter number of the skill to edit:")
                for i in range(len(job["required_skills"])):
                    print(f"{job["required_skills"][i]} to edit press {i + 1}")
                edit_choice2 = int(input())
                for i in range(len(job["required_skills"])):
                    if edit_choice2 == i + 1:
                        job["required_skills"][i] = input()
    save_jobs(jobs)

def delete_job(jobs):
    print("Delete job from the list")
    print('Select job id to delete')
    del_id = input()
    for job in jobs:
        if job['id'] == del_id:
            jobs.remove(job)
            print("Job add deleted")
            break
    save_jobs(jobs)