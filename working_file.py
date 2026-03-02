def load_job_data():
    return [
    {"id":0,
    "position":"Data analyst",
    "salary":1850,
    "location":"Vln",
    "required_skills":["sql", "python", "powerbi", "windows", "excel"]},
    {"id":1,
    "position":"Expert in Test Scenario Preparation",
    "salary":3850,
    "location":"Vln, Kns, Hybrid",
    "required_skills":["Basel4", "CRR3", "ICAAP", "ILAAP"]},
    {"id":2,
    "position":"Quantitative analyst",
    "salary":4200,
    "location":"Remote",
    "required_skills":["Statistics","SAS", "AI"]},
    {"id":3,
    "position":"Credit Risk Officer",
    "salary":4750,
    "location":"Vln, Riga, Tallinn",
    "required_skills":["PowerBI", "R", "Github"]}
    ]

# jobs = load_job_data()

# for job in jobs:
#     skills = ", ".join(jobs["required_skills"])

# print(*jobs[1]["required_skills"])
# print(jobs[1]["required_skills"])
# print(jobs[1]["required_skills"][2])
# print(len(jobs[1]["required_skills"]))
#
# from list_CRUD import print_jobs
#
# print("Edit jobs")
# print_jobs(jobs)
# print('Enter job id to edit')
#
# edit_id = int(input())
# for job in jobs:
#     if job["id"] == edit_id:
#         print("Enter 1 new if editing all required_skills:")
#         print("Enter 2 new if editing single required_skill:")
#         edit_choice = int(input())
#         if edit_choice == 1:
#             for i in range(len(job["required_skills"])):
#                 print(f"Enter new skill #{i + 1}")
#                 job["required_skills"][i] = input()
#
# print_jobs(jobs)


#         job['required_skills'] = input()



# print("Add a job:")
# print("Type in position name:")
# position = input()
# print("Type in salary:")
# salary = int(input())
# print("Type in location:")
# location = input()
# print("Type in number of skills required:")
# new_skills_num = int(input())
# required_skills = []
# for i in range(new_skills_num):
#
#     if new_skills_num == 0:
#         print("No required skills")
#     else:
#         print(f"Enter required skill #{i + 1}")
#         required_skill = input()
#         required_skills.append(required_skill)
#         print(required_skills)
#
# new_job = {
#     'id': 4,
#     "position": position,
#     "salary": salary,
#     "location": location,
#     "required_skills": required_skills
# }
# jobs.append(new_job)
#
# print(jobs[4]["required_skills"])