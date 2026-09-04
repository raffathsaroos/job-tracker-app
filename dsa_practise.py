skills =["python","sql","react","docker","lanchain"]
print("the main skill is: ", skills[0])

# adding stack into array
skills.append("Next.js")
skills.append("FastAPI")
print("All skills: ", skills)

location_coordinates = (13.0827, 80.2707)  
print("Location:", location_coordinates)
"""
# 3. Dictionary (Key-Value சோடிகள்) - Job Details-க்கு மிக முக்கியமானது!
job_summary = {
    "company": "Google",
    "role": "Backend Engineer",
    "status": "Applied"
}
print("Company Name:", job_summary["company"])

# 4. Set (Unique மதிப்பினை மட்டும் சேமிக்கும்)
job_statuses = {"Applied", "Interviewing", "Offered", "Rejected"}
print("Statuses:", job_statuses)
"""

job_summary = {
                "company": "goo",
                "role": "full",
                "status": "preparing"
              }
print("Extracting only company name from job-summary: ",job_summary["company"])

job_status = {"not applied yet","just applied","screening","interviewing"}
print("here are all statuses: ", job_status)
