
import csv


def process_csv(filename):
    employees = []
    invalid_count = 0

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    name = row["Name"].strip()
                    salary = float(row["Salary"])

                    if not name or salary < 0:
                        invalid_count += 1
                        continue

                    employees.append({
                        "Name": name,
                        "Salary": salary
                    })

                except (ValueError, KeyError, TypeError):
                    invalid_count += 1

        return employees, invalid_count

    except FileNotFoundError:
        print("Error: CSV file not found.")
        return None, 0


def generate_report(employees, invalid_count):
    if not employees:
        print("No valid employee records found.")
        print("Invalid records:", invalid_count)
        return

    salaries = [employee["Salary"] for employee in employees]

    total_salary = sum(salaries)
    average_salary = total_salary / len(salaries)
    highest_employee = max(employees, key=lambda emp: emp["Salary"])

    print("\n===== CSV DATA SUMMARY =====")
    print("Total employees:", len(employees))
    print("Total salary:", round(total_salary, 2))
    print("Average salary:", round(average_salary, 2))
    print("Highest-paid employee:", highest_employee["Name"])
    print("Highest salary:", round(highest_employee["Salary"], 2))
    print("Invalid records skipped:", invalid_count)


def main():
    filename = input("Enter CSV filename (default: employees.csv): ").strip()

    if not filename:
        filename = "employees.csv"

    employees, invalid_count = process_csv(filename)

    if employees is not None:
        generate_report(employees, invalid_count)


if __name__ == "__main__":
    main()

    
  
