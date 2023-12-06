
import random

Organizations = [
    "Accounting and Finance",
    "Information Technology",
    "Sales",
    "Human Resources",
    "Management",
    "Marketing",
    "Production and Operations"
]

OrganizationsJobs = {
    "Accounting and Finance": [
        "Accountant",
        "Financial Analyst",
        "Auditor",
        "Bookkeeper",
        "Tax Specialist"
    ],
    "Information Technology": [
        "Software Developer",
        "Network Administrator",
        "Systems Analyst",
        "Database Administrator",
        "IT Support Specialist"
    ],
    "Sales": [
        "Sales Representative",
        "Sales Manager",
        "Account Executive",
        "Business Development Specialist",
        "Retail Sales Associate"
    ],
    "Human Resources": [
        "HR Manager",
        "Recruiter",
        "Human Resources Generalist",
        "Compensation Analyst",
        "Employee Relations Specialist"
    ],
    "Management": [
        "General Manager",
        "Operations Manager",
        "Project Manager",
        "Team Leader",
        "Business Development Manager"
    ],
    "Marketing": [
        "Marketing Coordinator",
        "Digital Marketing Specialist",
        "Brand Manager",
        "Marketing Analyst",
        "Content Writer"
    ],
    "Production and Operations": [
        "Production Manager",
        "Operations Analyst",
        "Manufacturing Engineer",
        "Quality Control Specialist",
        "Supply Chain Manager"
    ]
}

def get_random_job(organization_unit_name):
    if organization_unit_name in OrganizationsJobs:
        return random.choice(OrganizationsJobs[organization_unit_name])
    else:
        return "Unknown Organization"