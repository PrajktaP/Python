import os
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <directory_path>")
    sys.exit(1)

dirname = sys.argv[1]
all_file_names = []

# Walk and collect all file names
for root_folder, sub_folders, file_names in os.walk(dirname):
    for name in file_names:
        if name != '.DS_Store':
            base_name = os.path.splitext(name)[0]
            all_file_names.append(base_name)

# Sort all collected base names and print
for name in sorted(all_file_names):
    print(name)


# python get_file_names.py database/factories