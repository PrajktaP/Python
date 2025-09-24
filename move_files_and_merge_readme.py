import os
import shutil
import sys

def move_files_and_merge_readme(main_folder):
    readme_contents = []

    # Loop through all subfolders
    for root, dirs, files in os.walk(main_folder, topdown=False):
        if root == main_folder:
            continue  # skip the main folder itself

        for file in files:
            file_path = os.path.join(root, file)

            if file.lower() == "readme.txt":
                # Collect contents of readme.txt
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    readme_contents.append(f"\n--- From {root} ---\n")
                    readme_contents.append(f.read())
            else:
                # Move other files to the main folder
                new_path = os.path.join(main_folder, file)
                # Handle name collisions by renaming
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(new_path):
                    new_path = os.path.join(main_folder, f"{base}_{counter}{ext}")
                    counter += 1
                shutil.move(file_path, new_path)
                print(f"Moved: {file_path} -> {new_path}")

    # Write combined readme.txt
    if readme_contents:
        readme_path = os.path.join(main_folder, "readme.txt")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write("\n".join(readme_contents))
        print(f"Combined readme.txt created at {readme_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <main_folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid folder.")
        sys.exit(1)

    move_files_and_merge_readme(folder_path)



"""
python script.py /path/to/your/main/folder
"""