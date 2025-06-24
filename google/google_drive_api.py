import os
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload
import fitz  # PyMuPDF

def extract_body_text(pdf_path):
    with fitz.open(pdf_path) as doc:
        content = []
        for page in doc:
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                # Only consider text blocks
                if block['type'] != 0:
                    continue

                for line in block['lines']:
                    for span in line['spans']:
                        y = span['bbox'][1]  # y-coordinate of text
                        text = span['text'].strip()

                        # Skip headers (e.g., y < 100) and footers (e.g., y > 700)
                        if 100 < y < 700 and text:
                            content.append(text)
        return "\n".join(content)

def pull_file_from_google_drive(assignment_no, folder_id, json_file_path, base_folder, destination_file):
    # Replace with your folder ID and path to the service account key file
    FOLDER_ID = folder_id
    SERVICE_ACCOUNT_FILE = json_file_path

    # Authenticate
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('drive', 'v3', credentials=creds)

    # Query files in the specific folder
    query = f"'{FOLDER_ID}' in parents and trashed = false"
    results = service.files().list(q=query, fields="files(id, name, mimeType)").execute()
    items = results.get('files', [])

    # Destination folder path
    assignment_folder = f"Assignment_{assignment_no}"
    destination_folder = os.path.join(base_folder, assignment_folder)
    # Create folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    if not items:
        print("No files found.")
    else:
        for item in items:
            if f"python assignment {assignment_no}" in item['name'].lower():
                print(f"*****{item['name']} ({item['id']})")
                request = service.files().get_media(fileId=item['id'])

                # new_filename = destination_file
                # Full file path inside the assignment folder
                pdf_filename = f"assignment_{assignment_no}.pdf"
                pdf_path = os.path.join(destination_folder, pdf_filename)

                # Save to the specified location
                fobj = open(pdf_path, 'wb')
                downloader = MediaIoBaseDownload(fobj, request)
                done = False
                while not done:
                    status, done = downloader.next_chunk()
                    print(f"  Download progress: {int(status.progress() * 100)}%")

                print(f"√ Downloaded: {pdf_path}")

                # 2. Read PDF and extract text
                try:
                    doc = fitz.open(pdf_path)
                    all_text = ""
                    for page in doc:
                        all_text += page.get_text()

                    # 3. Write extracted text into readme.txt
                    extracted_text = extract_body_text(pdf_path)

                    readme_path = os.path.join(destination_folder, destination_file)
                    f = open(readme_path, 'w', encoding='utf-8')
                    f.write(extracted_text)

                    print(f"√ Extracted text saved to: {readme_path}")

                    # Delete the downloaded PDF
                    os.remove(pdf_path)
                    print(f"√ Deleted PDF file: {pdf_path}")
                except Exception as e:
                    print(f"X Error reading PDF: {e}")

def main():
    # if len(sys.argv) < 2:
    #     print("Invalid arguments, please enter assignment number after program name")
    #     exit()

    # # arguments from command line
    # assignment_no = int(sys.argv[1])
    # folder_id = sys.argv[2]
    # json_file_path = sys.argv[3]
    # base_folder = sys.argv[4]

    # arguments from input file
    assignment_no = int(input())
    gdrive_folder_id = input()
    json_file_path = input()
    base_folder = input()
    destination_file = input()

    pull_file_from_google_drive(assignment_no, gdrive_folder_id, json_file_path, base_folder, destination_file)

if __name__ == "__main__":
    main()




"""
call using following command

> python google_drive_api.py < input.txt
"""