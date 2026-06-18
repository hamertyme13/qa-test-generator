import os
import re
from datetime import datetime

def export_to_selenium(test_cases):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output/test_cases_{timestamp}.py"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write("from selenium import webdriver\n")
        file.write("from selenium.webdriver.common.by import By\n")
        file.write("from selenium.webdriver.common.keys import Keys\n")
        file.write("import unittest\n\n")
        
        file.write("class TestCases(unittest.TestCase):\n")
        file.write("    def setUp(self):\n")
        file.write("        self.driver = webdriver.Chrome()\n\n")
        
        for test_case in test_cases:
            safe_name = re.sub(
                r'[^a-zA-Z0-9]+',
                '_',
                test_case.scenario.lower()
        )

            test_method_name = f"test_{safe_name}"
            file.write(f"    def {test_method_name}(self):\n")
            file.write(f"        # Scenario: {test_case.scenario}\n")
            file.write(f"        # Expected Result: {test_case.expected_result}\n")
            file.write(f"        # Priority: {test_case.priority}\n")
            file.write("        pass  # TODO: Implement test steps here\n\n")
        
        file.write("    def tearDown(self):\n")
        file.write("        self.driver.quit()\n\n")
        
        file.write("if __name__ == '__main__':\n")
        file.write("    unittest.main()\n")
    
    return filename