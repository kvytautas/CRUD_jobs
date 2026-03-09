import json

import pymysql

DB_CONFIG = {
    'host':'localhost', #127.0.0.1  ;)
    'port': 3306,
    'user':'root',
    'password':"Birute88",
    'database':'jobs_db'
}

headers = ['id', 'position', 'salary', 'location', 'required_skills']

def get_conn():
    return pymysql.connect(**DB_CONFIG)

def load_jobs():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from jobs") # query
    rows = cur.fetchall()
    cur.close()
    conn.close()
    jobs = []
    for row in rows:    # vertical flow
        single_job = {} # horizontal
        for col_num in range(len(headers)):
            single_job[headers[col_num]] = row[col_num]
        jobs.append(single_job)
    return jobs

def print_menu():
    print("-------------------------")
    print("Press 1 to print jobs list")
    print("Press 2 to add a job add")
    print("Press 3 to edit a job add")
    print("Press 4 to delete a job add")
    print("Press 5 to close program.")
    print("-------------------------")

def print_jobs(jobs):
    jobs = load_jobs()
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
            print("No required skills to enter")
        else:
            print(f"Enter required skill #{i+1}")
            required_skill = input()
            required_skills.append(required_skill)
            json_skills = json.dumps(required_skills)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO `jobs_db`.`jobs`(`position`,`salary`,`location`,`required_skills`) VALUES (%s,%s,%s,%s);",
                (position,salary,location,json_skills))
    conn.commit()
    cur.close()
    conn.close()


def edit_job(jobs):
    print("Edit job add")
    print('Enter job id to edit')
    edit_id = input()

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
            print("No required skills to enter")
        else:
            print(f"Enter required skill #{i + 1}")
            required_skill = input()
            required_skills.append(required_skill)
            json_skills = json.dumps(required_skills)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE `jobs_db`.`jobs` SET `position` =%s, `salary` = %s, `location` = %s, `required_skills` =%s WHERE `id` =%s;",
                (position, salary, location, json_skills, edit_id))
    conn.commit()
    cur.close()
    conn.close()






    # for job in jobs:
    #     if job['id'] == edit_id:
    #         print("Enter new position:")
    #         job['position'] = input()
    #         print("Enter new salary:")
    #         job['salary'] = int(input())
    #         print("Enter new location:")
    #         job['location'] = input()
    #         print("Enter 1 if editing all required_skills:")
    #         print("Enter 2 if editing single required_skill:")
    #         edit_choice = int(input())
    #         if edit_choice == 1:
    #             for i in range(len(job["required_skills"])):
    #                 print(f"Enter new skill #{i + 1}")
    #                 job["required_skills"][i] = input()
    #
    #                 # print(f"Enter new skill #{i + 1}")
    #                 # job["required_skills"][i] = input()
    #         elif edit_choice == 2:
    #             print(f"Enter number of the skill to edit:")
    #             for i in range(len(job["required_skills"])):
    #                 print(f"{job["required_skills"][i]} to edit press {i + 1}")
    #             edit_choice2 = int(input())
    #             for i in range(len(job["required_skills"])):
    #                 if edit_choice2 == i + 1:
    #                     job["required_skills"][i] = input()


def delete_job(jobs):
    print("Delete job from the list")
    print('Select job id to delete')
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from jobs where id = %s", (del_id,))
    row = cur.fetchone()
    if row:
        print(f"{row[0]}. Position: {row[1]}  Salary: {float(row[2]):.2f}  €"
              f"Location"
              f"{row[3]} Required_skills:"
              f" {row[4]}")
        cur.execute("delete from jobs where id = %s",(del_id,))
        conn.commit()
    else:
        print('Job id not found')
    cur.close()
    conn.close()

