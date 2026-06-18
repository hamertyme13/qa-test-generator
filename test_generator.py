class TestCase:
    def __init__(self, test_id, scenario, expected_result, priority):
        self.test_id = test_id
        self.scenario = scenario
        self.expected_result = expected_result
        self.priority = priority
    
    def to_list(self):
        return [self.test_id, self.scenario, self.expected_result, self.priority]

def generate_test_cases(feature, fields):
    test_cases = []

    counter = 1

    #Positive Test
    scenario = f"{feature} with valid inputs"
    expected = "Operation completes successfully"

    test_cases.append(
        TestCase(f"TC{counter:03}", scenario, expected, "High")
    )
    counter += 1

    for field in fields:
        field_name = field["name"]
        field_type = field["type"]

        #Invalid Input
        test_cases.append(
            TestCase(f"TC{counter:03}", f"{feature} with invalid {field_name}", "Required field error displayed", "High")
        )
        counter += 1

        #Empty Input
        test_cases.append(
            TestCase(f"TC{counter:03}", f"{feature} with empty {field_name}", "Required field error displayed", "High")
        )
        counter += 1

        # Minimum Length
        test_cases.append(
            TestCase(f"TC{counter:03}", f"{feature} with short {field_name}", "Minimum length error displayed", "High")
        )
        counter += 1

        # Maximum Length
        test_cases.append(
            TestCase(f"TC{counter:03}", f"{feature} with long {field_name}", "Maximum length error displayed", "High")
        )
        counter += 1

        # Special Characters
        test_cases.append(
            TestCase(f"TC{counter:03}", f"{feature} with special characters in {field_name}", "Special characters error displayed", "Medium")
        )
        counter += 1

        # Numeric Input
        if field_type == "text":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with numeric input in {field_name}", "Numeric input error displayed", "Medium")
            )
            counter += 1

        # Date Input
        elif field_type == "date":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with invalid date in {field_name}", "Invalid date error displayed", "Medium")
            )
            counter += 1

        # Email Input
        elif field_type == "email":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with invalid email in {field_name}", "Invalid email error displayed", "Medium")
            )
            counter += 1

        # Phone Input
        elif field_type == "phone":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with invalid phone in {field_name}", "Invalid phone error displayed", "Medium")
            )
            counter += 1

        # Password Input
        elif field_type == "password":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with invalid password in {field_name}", "Invalid password error displayed", "Medium")
            )
            counter += 1

            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with weak password in {field_name}", "Weak password error displayed", "Medium")
            )
            counter += 1

            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with short password in {field_name}", "Short password error displayed", "Medium")
            )
            counter += 1

            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with long password in {field_name}", "Long password error displayed", "Medium")
            )
            counter += 1

            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with password missing special character in {field_name}", "Password missing special character error displayed", "Medium")
            )
            counter += 1

            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with password missing number in {field_name}", "Password missing number error displayed", "Medium")
            )
            counter += 1

            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with password missing uppercase letter in {field_name}", "Password missing uppercase letter error displayed", "Medium")
            )
            counter += 1

            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with password missing lowercase letter in {field_name}", "Password missing lowercase letter error displayed", "Medium")
            )
            counter += 1

        # Confirm Password Input
        elif field_type == "confirm_password":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with invalid confirm password in {field_name}", "Invalid confirm password error displayed", "Medium")
            )
            counter += 1

        # Checkbox Input
        elif field_type == "checkbox":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with unchecked {field_name}", "Unchecked checkbox error displayed", "Medium")
            )
            counter += 1
        
        # Radio Button Input
        elif field_type == "radio":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with unselected {field_name}", "Unselected radio button error displayed", "Medium")
            )
            counter += 1

        # File Upload Input
        elif field_type == "file":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with invalid file type in {field_name}", "Invalid file type error displayed", "Medium")
            )
            counter += 1

        # Dropdown Input
        elif field_type == "dropdown":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with invalid selection in {field_name}", "Invalid selection error displayed", "Medium")
            )
            counter += 1

        # Multi-select Input
        elif field_type == "multi-select":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with invalid multi-selection in {field_name}", "Invalid multi-selection error displayed", "Medium")
            )
            counter += 1

        # Range Input
        elif field_type == "range":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with invalid range in {field_name}", "Invalid range error displayed", "Medium")
            )
            counter += 1

        # Textarea Input
        elif field_type == "textarea":
            test_cases.append(
                TestCase(f"TC{counter:03}", f"{feature} with invalid input in {field_name}", "Invalid input error displayed", "Medium")
            )
            counter += 1

        

    return test_cases
