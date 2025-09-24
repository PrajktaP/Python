import os
import sys

def merge_file_contents(folder_path, output_file="readme.txt"):
    merged_content = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories and the output file itself
        if os.path.isdir(file_path) or filename.lower() == output_file.lower():
            continue

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                merged_content.append(f"\n--- {filename} ---\n")
                merged_content.append(f.read())
        except Exception as e:
            print(f"Skipping {filename}: {e}")

    if merged_content:
        output_path = os.path.join(folder_path, output_file)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(merged_content))
        print(f"Merged contents written to {output_path}")
    else:
        print("No files to merge.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid folder.")
        sys.exit(1)

    merge_file_contents(folder_path)
