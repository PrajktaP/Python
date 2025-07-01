import os
import re
from collections import defaultdict

def get_php_files_in_folder(project_root, folder_name):
    php_files = []
    module_dir = os.path.join(project_root, 'module')

    for subdir, _, files in os.walk(module_dir):
        if os.path.basename(subdir) == folder_name:
            for file in files:
                if file.endswith('.php'):
                    full_path = os.path.join(subdir, file)
                    php_files.append(full_path)
    return php_files

def extract_full_class_name(file_path, project_root):
    """Try to extract the fully qualified class name (namespace + class)"""
    namespace = None
    class_name = None

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if not namespace and line.strip().startswith("namespace"):
                    match = re.match(r'namespace\s+([^;]+);', line)
                    if match:
                        namespace = match.group(1).strip()

                if not class_name and line.strip().startswith("class "):
                    match = re.match(r'class\s+(\w+)', line)
                    if match:
                        class_name = match.group(1).strip()

                if namespace and class_name:
                    break

        if namespace and class_name:
            return f"{namespace}\\{class_name}"
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def count_use_statements(class_names, project_root):
    usage_count = defaultdict(int)

    for subdir, _, files in os.walk(project_root):
        for file in files:
            if file.endswith('.php'):
                file_path = os.path.join(subdir, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        for class_name in class_names:
                            if re.search(rf'\buse\s+{re.escape(class_name)}\s*;', content):
                                usage_count[class_name] += 1
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    return dict(usage_count)

# === Main flow ===
if __name__ == '__main__':
    import sys

    project_root = '/Users/prajktaphisarekar/work/laravel/lendisoft/lms-backend-test'
    folder_name = sys.argv[1] if len(sys.argv) > 1 else 'Models'

    print(f"Scanning for PHP files inside module/**/{folder_name}")

    php_files = get_php_files_in_folder(project_root, folder_name)
    class_names = [extract_full_class_name(f, project_root) for f in php_files]
    class_names = [c for c in class_names if c]  # remove Nones

    usage_summary = count_use_statements(class_names, project_root)

    print("\n Class Import Usage Summary:")
    for class_name in class_names:
        count = usage_summary.get(class_name, 0)
        print(f"{class_name}: {count} use statements")



# python files_usage_checker.py Services > python_output/files_usage_checker_output.txt
