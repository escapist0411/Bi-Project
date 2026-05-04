import pandas as pd
import numpy as np

# Set random seed
np.random.seed(42)

# Generate 500 samples
n_samples = 500

# Realistic Job Titles
job_roles = [
    "Data Scientist", "Data Analyst", "BI Developer", "Machine Learning Engineer",
    "Data Engineer", "Software Engineer", "Cloud Architect", "Database Administrator",
    "Business Analyst", "Systems Analyst", "DevOps Engineer", "Frontend Developer",
    "Backend Developer", "Full Stack Developer", "Network Engineer", "Security Analyst",
    "IT Manager", "Technical Lead", "Scrum Master", "UI/UX Designer", "QA Engineer"
]

# Randomly assign job titles
job_titles = np.random.choice(job_roles, n_samples)

# Experience Level (0-100%)
experience = np.random.randint(0, 101, n_samples)

# Salary (mocking 0-100 range)
salary = np.random.randint(0, 101, n_samples)

# Location (Target Variable) - e.g., 0: New York, 1: San Francisco, 2: Remote, 3: Austin
location_names = ["New York", "San Francisco", "Remote", "Austin"]
location = []
for s in salary:
    if s > 80:
        location.append(np.random.choice(["New York", "San Francisco"], p=[0.4, 0.6]))
    elif s > 40:
        location.append(np.random.choice(["New York", "Remote", "Austin"], p=[0.3, 0.4, 0.3]))
    else:
        location.append(np.random.choice(["Remote", "Austin"], p=[0.7, 0.3]))

df = pd.DataFrame({
    'Job Title': job_titles,
    'Experience Level': experience,
    'Salary': salary,
    'Location': location
})

df.to_csv('data/dataset.csv', index=False)
print("Mock dataset created at data/dataset.csv")
