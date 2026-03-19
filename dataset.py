import pandas as pd
import random

num_samples = 2000   # Increased for better training

indian_cities = [
    "Delhi", "Mumbai", "Bangalore",
    "Hyderabad", "Pune",
    "Chennai", "Kolkata", "Ahmedabad"
]

real_titles = [
    "Software Engineer", "Data Analyst",
    "Backend Developer", "Frontend Developer",
    "HR Executive", "Marketing Manager",
    "Python Developer", "Machine Learning Engineer"
]

fake_titles = [
    "Data Entry Work From Home",
    "Earn Money Online",
    "Urgent Hiring No Interview",
    "Part Time Home Based Job"
]

real_keywords = [
    "Python", "SQL", "Team collaboration",
    "Project management", "Software development"
]

fake_keywords = [
    "No interview", "Registration fee",
    "Guaranteed income", "Limited seats"
]

data = []

for i in range(num_samples):

    if i < num_samples // 2:
        fraudulent = 0
        title = random.choice(real_titles)
        description = f"We are hiring for {random.choice(real_keywords)} role."
        requirements = "Bachelor's degree required with 2+ years experience."
        benefits = "Health insurance and performance bonus."
    else:
        fraudulent = 1
        title = random.choice(fake_titles)
        description = f"Earn money using {random.choice(fake_keywords)}."
        requirements = "No qualification needed."
        benefits = "Instant payment and unlimited earning."

    row = {
        "title": title,
        "location": random.choice(indian_cities),
        "company_profile": "Reputed Indian Company",
        "description": description,
        "requirements": requirements,
        "benefits": benefits,
        "fraudulent": fraudulent
    }

    data.append(row)

df = pd.DataFrame(data)
df.to_csv("india_fake_job_dataset.csv", index=False)

print("Dataset Created Successfully!")
