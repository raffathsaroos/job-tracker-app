import json

skills =["python","sql","react","docker","lanchain"]
print("the main skill is: ", skills[0])

# adding stack into array
skills.append("Next.js")
skills.append("FastAPI")
print("All skills: ", skills)

location_coordinates = (13.0827, 80.2707)  
print("Location:", location_coordinates)


job_summary = {
                "company": "goo",
                "role": "full",
                "status": "preparing"
              }
print("Extracting only company name from job-summary: ",job_summary["company"])

job_status = {"not_yet","just_applied","screening","interviewing"}
print("here are all statuses: ", job_status)


user_status = input("Enter ur job status: ")

if user_status == "not_yet":
    print("please apply soon")
elif user_status == "just_applied":
    print("please wait")
elif user_status == "screening":
    print("under review")
else:
    print("be ready")

print("--- Required Skills ---")
for x in skills:
    print(f"- {x}")

count = 1
while count <= 3:
    print(f"X {count}")
    count += 1
    
    

job_dict = {"company": "Goo", "title": "fullstack Developer", "status": "just_applied"}
json_data = json.dumps(job_dict)

print("JSON Format String:", json_data)
print("Data Type:", type(json_data))  
    

