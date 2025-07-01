import os
import sys

def get_model_files_in_module(project_root, folder = 'Models'):
    model_files = []
    module_dir = os.path.join(project_root, 'module')

    for subdir, _, files in os.walk(module_dir):
        # Only include files in a 'Models' folder
        if os.path.basename(subdir) == folder:
            for file in files:
                if file.endswith('.php'):
                    full_path = os.path.join(subdir, file)
                    relative_path = os.path.relpath(full_path, project_root)
                    model_files.append(relative_path)
    
    return model_files

# === Example usage ===
if __name__ == '__main__':
    if not os.path.exists("python_output"):
        os.mkdir("python_output")

    project_root = '/Users/prajktaphisarekar/work/laravel/lendisoft/lms-backend-test'
    folder = sys.argv[1]

    model_files = get_model_files_in_module(project_root, folder)
    print(f"\nModel Files in 'module/*/{folder}':")
    for path in model_files:
        print(path)


# python list_files.py Services > python_output/files_list.txt