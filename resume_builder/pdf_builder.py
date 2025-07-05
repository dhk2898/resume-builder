from fpdf import FPDF

class PDF_Builder:
    # sanity check to make sure the resume data being passed in is valid. This should always be valid. 
    def __init__(self, resume_data):
        if not self.is_valid_resume_data(resume_data):
            raise ValueError("Invalid Resume Data")
        self.data = resume_data
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)


    def is_valid_resume_data(self, data):
        required_keys = {
            "contact_info": dict,
            "summary": str,
            "experience": list,
            "education": list,
            "technical_skills": list,
            "projects": list,
            "certifications": list
            }
        if not isinstance(data, dict):
            return False
        for key, expected_type in required_keys.items():
            if key not in data:
                return False
            if not isinstance(data[key], expected_type):
                return False
        return True


    def generate_pdf(self):
        self.pdf.add_page()
        self.add_header()
        self.add_summary()
        self.add_experience()
        self.add_education()
        self.add_skills()
        self.add_certifications()
        self.pdf.output(f"{self.data['contact_info'].get('name', 'Unnamed')}_resume.pdf")


    def add_header(self):
        contact = self.data.get("contact_info", {})
        name = contact.get("name", "YOUR NAME")
        job_title = contact.get("job_title", "YOUR JOB TITLE")
        email = contact.get("email", "YOUR EMAIL")
        linkedin = contact.get("linkedin", "YOUR LINKEDIN")
        github = contact.get("github", "YOUR GITHUB")
        location = contact.get("location", "YOUR LOCATION")

        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(0, 10, name.upper(), ln=True, align="C")

        self.pdf.set_font("Arial", "", 12)
        self.pdf.cell(0, 8, job_title, ln=True, align="C")

        # filter just in case one of the values is blank to avoid weird formatting
        contact_line = " || ".join(filter(None, [email, linkedin, github, location]))
        self.pdf.set_font("Arial", "", 10)
        self.pdf.cell(0, 8, contact_line, ln=True, align="C")
        self.pdf.ln(5)

    def add_summary(self):
        summary = self.data.get("summary", "")
        if summary:
            self.section_title("Summary")
            self.pdf.set_font("Arial", "", 10)
            self.pdf.multi_cell(0, 6, summary)
            self.pdf.ln(3)

    def add_experience(self):
        self.section_title("Experience")
        for exp in self.data.get("experience", []):
            self.pdf.set_font("Arial", "B", 11)
            self.pdf.cell(0, 6, exp.get("company", "Company"), ln=True)

            role_line = f"{exp.get('title', 'Role')}"
            location = exp.get("location", "")
            dates = f"{exp.get('start_date', '')} ~ {exp.get('end_date', '')}"
            self.inline_label(role_line, location, dates)

            self.pdf.set_font("Arial", "", 10)
            for bullet in exp.get("description", "").split("\n"):
                if bullet.strip():
                    self.pdf.cell(5)
                    self.pdf.multi_cell(0, 5, f"- {bullet.strip()}")
            self.pdf.ln(3)

    def add_education(self):
        self.section_title("Education")
        for edu in self.data.get("education", []):
            degree = edu.get("degree", "")
            school = edu.get("institution", "")
            location = edu.get("location", "")
            dates = f"{edu.get('start_date', '')} ~ {edu.get('end_date', '')}"
            self.pdf.set_font("Arial", "B", 11)
            self.pdf.cell(0, 6, school, ln=True)
            self.inline_label(degree, location, dates)

    def add_skills(self):
        skills = self.data.get("technical_skills", [])
        if skills:
            self.section_title("Skills")
            self.pdf.set_font("Arial", "", 10)
            self.pdf.multi_cell(0, 6, ", ".join(skills))
            self.pdf.ln(3)

    def add_certifications(self):
        certs = self.data.get("certifications", [])
        if certs:
            self.section_title("Certification")
            self.pdf.set_font("Arial", "", 10)
            for cert in certs:
                line = f"{cert.get('name')} - {cert.get('provider')} - {cert.get('year')}"
                self.pdf.multi_cell(0, 6, line)
            self.pdf.ln(3)

    def section_title(self, title):
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.set_text_color(40, 40, 40)
        self.pdf.cell(0, 8, title.upper(), ln=True)
        self.pdf.set_draw_color(200, 200, 200)
        self.pdf.line(self.pdf.get_x(), self.pdf.get_y(), 200, self.pdf.get_y())
        self.pdf.ln(3)
        self.pdf.set_text_color(0, 0, 0)

    def inline_label(self, left, right_top, right_bottom):
        self.pdf.set_font("Arial", "", 10)
        self.pdf.cell(0, 6, left, ln=True)
        if right_top or right_bottom:
            self.pdf.set_font("Arial", "I", 9)
            meta = ", ".join(filter(None, [right_top, right_bottom]))
            self.pdf.cell(0, 5, meta, ln=True)


