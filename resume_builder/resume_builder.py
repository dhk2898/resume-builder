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
                 (2, "Summary"),
                 (3, "Experience"),
                 (4, "Education"),
                 (5, "Technical Skills"),
                 (6, "Projects"),
                 (7, "Generate Resume (PDF)"),
                 (8, "Exit"),

            ]
        ).run()

        if choice is None:
            continue

        match choice:
            case 1:
                r.add_contact_info()
            case 2:
                r.add_summary()
            case 3:
                r.add_experience()
            case 4:
                r.add_education()
            case 5:
                r.add_technical_skills()
            case 6:
                r.add_projects()
            case 7:
                pdf.generate_pdf()
            case 8:
                print("Exiting....")
                break


if __name__ == "__main__":
    main()
