from test_generator import generate_test_cases
from exporter import export_to_csv
from excel_exporter import export_to_excel
from selenium_exporter import export_to_selenium
from project_manager import (save_project, load_project)

print("Welcome to the QA Test Case Generator")
print("Please enter the details for your application and feature to generate test cases.")
print("You will be prompted to enter the number of fields and their details.")
print("After generating test cases, you can choose to export them in various formats (CSV, Excel, Selenium Test Script).")
print("You can also save and load your project for future use.\n")
print("Let's get started!\n")
print("--------------------------------------------------\n")
print("1. Create New Project: Start a new project by entering the application name, feature name, and field details.")
print("2. Load Existing Project: Load a previously saved project to continue working on it.")

main_choice = input("Select an option (1-2): ")

if main_choice == "1":

    application = input("Application Name: ")
    feature = input("Feature Name: ")

    field_count = int(
        input("Number of fields: ")
    )

    fields = []

    for _ in range(field_count):

        field_name = input(
            "Field Name: "
        )

        field_type = input(
            "Field Type: "
        ).lower()

        fields.append(
            {
                "name": field_name,
                "type": field_type
            }
        )

    save_project(
        "projects/latest_project.json",
        application,
        feature,
        fields
    )

elif main_choice == "2":

    project = load_project(
        "projects/latest_project.json"
    )

    application = project["application"]
    feature = project["feature"]
    fields = project["fields"]

    print(
        f"\nLoaded project: "
        f"{application}"
    )

else:

    print("Invalid option.")
    exit()

test_cases = generate_test_cases(
    feature,
    fields
)




# Save Project
save_project("projects/latest_project.json", application, feature, fields)



# Menu for export options
print("\nQA Test Case Generator")
print("1. Export to CSV")
print("2. Export to Excel")
print("3. Export to Both CSV and Excel")
print("4. Export to Selenium Test Script")
print("5. Export Everything (CSV, Excel, Selenium Test Script)")

choice = input("Select an option (1-5): ")

if choice == "1":
    csv_file = export_to_csv(test_cases)
    print(f"CSV file generated: {csv_file}")
elif choice == "2":
    excel_file = export_to_excel(test_cases)
    print(f"Excel file generated: {excel_file}")
elif choice == "3":
    csv_file = export_to_csv(test_cases)
    excel_file = export_to_excel(test_cases)
    print(f"CSV and Excel files generated: {csv_file}, {excel_file}")
elif choice == "4":
    selenium_file = export_to_selenium(test_cases)
    print(f"Selenium test script generated: {selenium_file}")
elif choice == "5":
    csv_file = export_to_csv(test_cases)
    excel_file = export_to_excel(test_cases)
    selenium_file = export_to_selenium(test_cases)
    print(f"CSV, Excel, and Selenium files generated: {csv_file}, {excel_file}, {selenium_file}")
else:
    print("Invalid choice. No files generated.")

# Informational summary
print("Export completed.")
print(f"{len(test_cases)} test cases generated.")

# Display summary of generated test cases
print(f"\nGenerated {len(test_cases)} test cases.\n")

high_count = sum(1 for tc in test_cases if tc.priority == "High")
medium_count = sum(1 for tc in test_cases if tc.priority == "Medium")
low_count = sum(1 for tc in test_cases if tc.priority == "Low")

print("Summary")
print("-------")
print(f"High Priority: {high_count}")
print(f"Medium Priority: {medium_count}")
print(f"Low Priority: {low_count}")

for test_case in test_cases:
    print(f" - {test_case.test_id}: {test_case.scenario} (Expected: {test_case.expected_result})")