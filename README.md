 CSV Data Processor

Description

The CSV Data Processor is a Python project that reads employee data from a CSV file and calculates useful statistics such as total salary, average salary, highest salary, and total number of employees. It uses Python's built-in CSV module to process data easily and efficiently.

Objectives

- Learn CSV file handling in Python.
- Read employee records from a CSV file.
- Calculate total and average salaries.
- Find the highest-paid employee.
- Count valid employee records.
- Handle missing and invalid values.

Technologies Used

- Python 3
- CSV module

Project Files

- "csv_processor.py" – Python program for processing CSV data.
- "employees.csv" – Input dataset containing employee details.
- "README.md" – Project documentation.

How to Run

1. Install Python 3 on your computer.

2. Save the Python program as "csv_processor.py".

3. Create the "employees.csv" file with employee names and salaries.

4. Keep both files in the same folder.

5. Open the terminal in that folder.

6. Run the following command:
   
   "python csv_processor.py"

7. Enter the CSV filename when prompted.

Features

- Reads CSV data using Python's "csv" module.
- Calculates total salary and average salary.
- Identifies the highest-paid employee.
- Counts valid employee records.
- Handles missing or invalid salary values.
- Displays a summary report in the terminal.

Sample Output

===== CSV DATA SUMMARY =====
Total employees: 5
Total salary: 230000.0
Average salary: 46000.0
Highest-paid employee: Priya
Highest salary: 60000.0
Invalid records skipped: 0

Interview Questions

1. What is CSV?

CSV stands for Comma-Separated Values. It is a file format used to store data in rows and columns.

2. How can Python read CSV files?

Python uses the built-in "csv" module. The "csv.DictReader()" function reads rows as dictionaries.

3. What is the purpose of the "sum()" function?

The "sum()" function calculates the total of numerical values.

4. How is the average salary calculated?

The average salary is calculated by dividing the total salary by the number of valid employees.

5. Why is error handling important?

Error handling helps the program manage missing files and invalid data without crashing.

Conclusion

This project helped me understand CSV file handling, data processing, statistical calculations, and error handling in Python. It demonstrates how Python can be used to analyze structured data and generate a useful summary report.
