jobs = [
    {
        "company": "Google",
        "role": "Backend Developer",
        "status": "Applied",
        "salary": 120000
    },
    {
        "company": "Microsoft",
        "role": "Full Stack Engineer",
        "status": "Interviewing",
        "salary": 110000
    }
]

print("=== JOB APPLICATION TRACKER ===")


for index, job in enumerate(jobs, start=1):
    print(f"\nJob #{index}:")
    print(f"  Company : {job['company']}")
    print(f"  Role    : {job['role']}")
    print(f"  Status  : {job['status']}")
    print(f"  Salary  : ${job['salary']}")

print("\n===============================")