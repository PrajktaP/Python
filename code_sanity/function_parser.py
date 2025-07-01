import re
import sys

def extract_php_methods(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Match public, protected, or private methods
    method_pattern = r'(public|protected|private)\s+function\s+(\w+)\s*\('
    matches = re.findall(method_pattern, content)

    # Return only the method names
    return [match[1] for match in matches]

def main():
    # Example usage
    php_file = sys.argv[1]
    methods = sorted(list(set(extract_php_methods(php_file))))

    print("Found methods:")
    for method in methods:
        print(method)

if __name__ == "__main__":
    main()



"""
python function_parser.py module/Loan/Models/Loan.php > loan_methods.php
"""
