import validators
from prompt_toolkit import prompt
from datetime import datetime
import re
import os

class Resume_Data:
    def __init__(self, validator):
        self.validator = validator
        self._resume_data = {
            "contact_info":{},
            "summary":[],
            "experience":[],
            "education":[],
            "technical_skills":[],
            "projects":[],
            "certifications":[]
        }

    @property
    def resume_data(self):
        return self._resume_data

    def clear_screen(self):
        os.system("cls" if os == "nt" else "clear")

    def return_to_home(self):
        print("\nReturning to Home Menu")

    def add_contact_info(self):
        self.clear_screen()
        print("Enter Contact Information")
        for key, message in [
                ("name", "Name: "),
                ("job_title", "Job Title: "),
                ("email", "Email: "),
                ("phone", "Phone Number: "),
                ("linkedin", "LinkedIn: "),
                ("github", "Github: "),
                ("location", "Location: ")
            ]:
            while True:
                value  = prompt(message)
                match key:
                    case "email":
                        if not validators.email(value):
                            print(f"Invalid {key}")
                            continue
                    case "linkedin":
                        linkedin_pattern = r"^https:\/\/(www\.)?linkedin\.com\/.*$"
                        if not re.match(linkedin_pattern, value):
                            print(f"Invalid {key} URL")
                            continue
                    case "github":
                        github_pattern = r"^https:\/\/(www\.)?github\.com\/.*$"
                        if not re.match(github_pattern, value):
                            print(f"Invalid {key} URL")
                            continue
                    case "phone":
                        if not value.isdigit():
                            print(f"Invalid {key}")
                            continue
                    case _:
                        break

                self._resume_data["contact_info"][key] = value
                break
        self.return_to_home()

    def add_summary(self):
        self.clear_screen()
        print("Please add an introductory summary: ")
        summary = {
            "summary": prompt("Summary: ")
        }
        self._resume_data["summary"] = summary
        self.return_to_home()

    def add_experience(self):
        while True:
            self.clear_screen()
            print("Enter Experience")
            experience = {}
            for key, message in [
                ("title", "Job Title: "),
                ("company", "Company: "),
                ("start_date", "Start Date (YYYY-MM): "),
                ("end_date", "End Date (YYYY-MM or leave blank if current): "),
                ("description", "Describe your role and responsibilities: ")
            ]:
                while True:
                    value = prompt(message).strip()

                    match key:
                        case "start_date":
                            try:
                                datetime.strptime(value, "%Y-%m")
                                break
                            except ValueError:
                                print("Invalid start date format. Please use YYYY-MM")
                                continue

                        case "end_date":
                            if value == "":
                                value = "Present"
                                break
                            try:
                                datetime.strptime(value, "%Y-%m")
                                break
                            except ValueError:
                                print("Invalid end date format. Please use YYYY-MM")
                                continue

                        case _:  # Default case
                            break

                experience[key] = value

            self._resume_data["experience"].append(experience)
            more = prompt("Do you wish to add more experience? Yes/No ").strip().lower()
            if more == "no":
                break
        self.return_to_home()


    def add_education(self):
        while True:
            self.clear_screen()
            print("Enter Education Information")
            education = {}
            for key, message in [
                ("degree", "Degree: "),
                ("institution", "Institution: "),
                ("start_date", "Start Date (YYYY-MM): "),
                ("end_date", "End Date (YYYY-MM): ")
            ]:
                while True:
                    value = prompt(message).strip()
                    match key:
                        case "institution":
                            validated = self.validator.validate(value)
                            if validated:
                                value = validated["school.name"]
                                break
                            else:
                                print("Could not validate institution")
                                manual_choice = prompt("Would you like continue with the institution name you've entered? (yes/no): ").strip().lower()
                                if manual_choice in ("yes", "y"):
                                    value = value
                                    break
                                else:
                                    print("Enter the institution name again")
                                    continue
                        case "start_date":
                            try:
                                datetime.strptime(value, "%Y-%m")
                                break
                            except ValueError:
                                print("Invalid start date format. Please use YYYY-MM.")
                                continue

                        case "end_date":
                            try:
                                datetime.strptime(value, "%Y-%m")
                                break
                            except ValueError:
                                print("Invalid end date format. Please use YYYY-MM.")
                                continue
                        case _:
                            break

                education[key] = value

            self._resume_data["education"].append(education)
            more = prompt("Do you wish to add more experience? Yes/No ").strip().lower()
            if more == "no":
                break
        self.return_to_home()


    def add_technical_skills(self):
        self.clear_screen()
        print("Enter skills. Please separate with a comma: ")
        skills = [skill.strip() for skill in prompt("Skills (comma-separated): ").split(",")]
        self._resume_data["technical_skills"].extend(skills)
        self.return_to_home()


    def add_projects(self):
        while True:
            self.clear_screen()
            print("Enter Project Information")
            project = {
                "name": prompt("Project Name: "),
                "description": prompt("Description: "),
                "technologies": prompt("Technologies Used: ")
            }
            self._resume_data["projects"].append(project)
            more = prompt("Do you want to add more projects? (yes/no): ").strip().lower()
            if more == "no":
                break
        self.return_to_home()

    def add_certifications(self):
        while True:
            self.clear_screen()
            print("Enter Certifications")

            cert = {
                "name": prompt("Certification Name: "),
                "provider": prompt("Provider: ")
            }
            while True:
                year = prompt("Year (e.g., 2022): ").strip()
                if year.isdigit() and len(year) == 4 and 1900 <= int(year) <= datetime.now().year:
                    cert["year"] = year
                    break
                else:
                    print("Invalid Year")

            self._resume_data["certifications"].append(cert)

            more = prompt("Do you want to add more certifications? (yes/no): ").strip().lower()
            if more == "no":
                break
        self.return_to_home()
