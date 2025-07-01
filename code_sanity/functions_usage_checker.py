import os
import re
from collections import defaultdict
import sys

def extract_php_functions(filepath):
    function_names = []
    pattern = re.compile(r'function\s+([a-zA-Z0-9_]+)\s*\(')

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                function_names.append(match.group(1))
    
    return function_names

def count_php_function_usages(function_names, root_dir):
    usage_count = defaultdict(int)
    php_files = []

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.php'):
                php_files.append(os.path.join(subdir, file))

    for filepath in php_files:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                for func in function_names:
                    # Match only function *calls*, not definitions (we already extracted those)
                    matches = re.findall(r'\b{}\s*\('.format(re.escape(func)), content)
                    usage_count[func] += len(matches)
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    return dict(usage_count)

def analyze_php_file_usage(target_file, project_root):
    functions = extract_php_functions(target_file)
    print(f"\nFunctions in {target_file}: {functions}")
    usage_summary = count_php_function_usages(functions, project_root)
    return usage_summary

# === Example usage ===
if __name__ == '__main__':
    target_file = sys.argv[1]
    project_root = '/Users/prajktaphisarekar/work/laravel/lendisoft/lms-backend-test/module'

    usage = analyze_php_file_usage(target_file, project_root)
    print("\nFunction Usage Count:")
    for func, count in usage.items():
    	if count == 0:
	    	print(f"****** {func}: {count} ******")
    	else:
    		print(f"{func}: {count}")



# python functions_usage_checker.py 'module/LoanTransaction/Services/NonCashTransactionService.php' > python_output/services/NonCashTransactionService.txt



