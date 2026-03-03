from data import load_job_data


def print_menu():
    print("-------------------------")
    print("Press 1 to print jobs list")
    print("Press 2 to add a job add")
    print("Press 3 to edit a job add")
    print("Press 4 to delete a job add")
    print("Press 5 to close program.")
    print("-------------------------")

def load_jobs():
    return load_job_data()

def print_jobs(jobs):
    print("Jobs list:")
    for job in jobs:
        print(
            f"{job['id']}. Position: {job['position']}  Salary: €{job['salary']:.1f} Location(s): {job['location']}  Required skills: {job['required_skills']}"
        )
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

    id_counter += 1
    new_job = {
        'id': id_counter,
        "position": position,
        "salary": salary,
        "location": location,
        "required_skills": required_skills
    }
    jobs.append(new_job)
    return id_counter

def edit_job(jobs):
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
            elif edit_choice == 2:
                print(f"Enter number of the skill to edit:")
                for i in range(len(job["required_skills"])):
                    print(f"{job["required_skills"][i]} to edit press {i + 1}")
                edit_choice2 = int(input())
                for i in range(len(job["required_skills"])):
                    if edit_choice2 == i + 1:
                        job["required_skills"][i] = input()

def delete_job(jobs):
    print("Delete job from the list")
    print('Select job id to delete')
    del_id = int(input())
    for job in jobs:
        if job['id'] == del_id:
            jobs.remove(job)
            print("Job add deleted")
            break