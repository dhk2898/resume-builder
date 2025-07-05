# CLI Resume Builder

A command-line interface tool for building resumes with validation and PDF generation support.

The following resume builder was used as a guideline for this project:
https://github.com/king04aman/All-In-One-Python-Projects/tree/main/Resume%20Builder

---

## Features

### Input Validation
- **Date Validation**  
  Ensures correct formatting for start/end dates using `datetime.strptime`.  
  Supported formats: `YYYY-MM` or `YYYY-MM-DD`

- **Regex Validation**  
  Validates input fields like:
  - Email (via `validators` library)
  - Phone number (must be digits)
  - LinkedIn and GitHub URLs (validated via regular expressions)

- **Institution Validation**  
  Uses the **U.S. Department of Education's College Scorecard API** to:
  - Validate U.S. institutions
  - Provide suggestions and fallback manual input for unmatched entries

---

### PDF Generation (via `fpdf`)
- Formats user input into a structured resume
- Supports:
  - Header section (name, title, contact info)
  - Summary paragraph
  - Work experience 
  - Education history
  - Technical skills
  - Projects
  - Certifications
- Generates a downloadable `.pdf` file named after the user's full name

---

## Usage

1. The user is guided step-by-step through the CLI.
2. Each resume section is entered interactively.
3. Validation is applied at every step to ensure correctness.
4. Once data collection is complete, a PDF is generated using `fpdf`.

---

## Dependencies

validators: For validating emails
requests: Used for validating schools with the Scorecard API (currently just schools in the USA)
prompt_toolkit: A library for building beautiful command-line applications.
fpdf: A library for generating PDF documents from the entered resume data.

---

## Potential Future Features
Fuzzy matching and dropdown selection for schools with multiple matches

International institution support

GUI version using Tkinter or Textual
