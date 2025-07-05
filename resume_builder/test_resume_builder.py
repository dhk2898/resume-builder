from resume_data import Resume_Data
from pdf_builder import PDF_Builder
from institution_validator import Institution_Validator

# Dummy Data file to check formatting

def fill_dummy_data(r):
    # Contact Info
    r._resume_data["contact_info"] = {
        "name": "Jane Doe",
        "job_title": "Senior Data Analyst",
        "email": "jane.doe@example.com",
        "phone": "1234567890",
        "linkedin": "https://www.linkedin.com/in/janedoe",
        "github": "https://github.com/janedoe",
        "location": "San Francisco, CA"
    }

    r._resume_data["summary"] = (
        "Experienced data analyst with a passion for turning data into strategic insights. "
        "Skilled in dashboard creation, SQL, and stakeholder communication."
    )

    # Experience
    r._resume_data["experience"] = [
        {
            "company": "TechCorp",
            "title": "Data Analyst",
            "location": "San Francisco, CA",
            "start_date": "01/2020",
            "end_date": "Present",
            "description": (
                "Built and maintained dashboards\n"
                "Conducted data audits\n"
                "Collaborated with business teams to define KPIs"
            )
        }
    ]


    r._resume_data["education"] = [
        {
            "degree": "B.S. in Computer Science",
            "institution": "University of California, Berkeley",
            "location": "Berkeley, CA",
            "start_date": "2015",
            "end_date": "2019"
        }
    ]


    r._resume_data["technical_skills"] = [
        "Python", "SQL", "Tableau", "Excel", "Data Visualization"
    ]

    r._resume_data["certifications"] = [
        {
            "name": "Certified Data Analyst",
            "provider": "DataCamp",
            "year": "2022"
        }
    ]


def main():
    validator = Institution_Validator()
    r = Resume_Data(validator)
    fill_dummy_data(r)

    pdf_builder = PDF_Builder(r.resume_data)
    pdf_builder.generate_pdf()

if __name__ == "__main__":
    main()
