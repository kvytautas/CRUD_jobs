import csv

data = [
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

# Write CSV
with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "position", "salary", "location", "required_skills"])

    for job in data:
        skills = ", ".join(job["required_skills"])  # convert list → string
        writer.writerow([job["id"], job["position"], job["salary"], job["location"], skills])