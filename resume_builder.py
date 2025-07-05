from resume_data import Resume_Data
from pdf_builder import PDF_Builder
from institution_validator import Institution_Validator
from prompt_toolkit.shortcuts import radiolist_dialog

validator = Institution_Validator()
r = Resume_Data(validator)
pdf = PDF_Builder(r.resume_data)


def main():
    while True:
        r.clear_screen()
        choice = radiolist_dialog(
            title = "CLI resume builder",
            text = "Please select which part of your resume you'd like to work on",
            values =[
                 (1, "Contact Info"),
                 (2, "Experience"),
                 (3, "Education"),
                 (4, "Technical Skills"),
                 (5, "Projects"),
                 (6, "Generate Resume (PDF)"),
                 (7, "Exit"),

            ]
        ).run()

        if choice is None:
            continue

        match choice:
            case 1:
                r.add_contact_info()
            case 2:
                r.add_experience()
            case 3:
                r.add_education()
            case 4:
                r.add_technical_skills()
            case 5:
                r.add_projects()
            case 6:
                pdf.generate_pdf()
            case 7:
                print("Exiting....")
                break


if __name__ == "__main__":
    main()
