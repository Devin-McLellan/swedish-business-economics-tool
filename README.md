# Python_Project_Salary_Control
Program that scans all municipalities in Sweden and compiles local tax tables for easy comparison and analysis.

# Swedish Tax Table Lookup Program 🇸🇪

This project is a Python-based program that searches through **all municipalities in Sweden** and returns the corresponding **tax tables** based on provided data.

The program uses an external CSV file containing up-to-date tax information and is structured in a modular way for clarity, maintainability, and reuse.

---

## Project Structure

swedish-tax-table-lookup/
├── src/
│   ├── main.py                # Program entry point
│   └── functions.py           # Core logic and helper functions
│
├── data/
│   └── skattetabell_new.csv   # Tax table data for all Swedish municipalities
│
├── README.md
└── requirements.txt           # (Optional) External dependencies
---

## How it Works

- Loads tax data from `skattetabell_new.csv`
- Searches through all Swedish municipalities
- Returns the correct tax table based on user input
- Separates logic and execution for cleaner code structure

---

## Technologies Used

- **Python 3**
- **CSV data handling**
- Modular program design

---

## How to Run

1. Make sure you have Python 3 installed
2. Place all files in the same directory
3. Run the program:

```bash
python mitt_program_main.py

 Purpose

This project demonstrates:
	•	Data processing with CSV files
	•	Clean program structure in Python

	Input validation
	•	Command-line arguments
	•	GUI or web interface
	•	Automatic updates of tax data
	•	Practical problem-solving using real-world public data
