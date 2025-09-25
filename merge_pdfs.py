import os
import sys
from PyPDF2 import PdfMerger

def merge_pdfs(folder_path, output_filename="merged.pdf"):
    merger = PdfMerger()
    
    # Get all PDF files in the folder (sorted for consistent order)
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
    pdf_files.sort()
    
    if not pdf_files:
        print("No PDF files found in the given folder.")
        return
    
    for pdf in pdf_files:
        merger.append(os.path.join(folder_path, pdf))
    
    output_path = os.path.join(folder_path, output_filename)
    merger.write(output_path)
    merger.close()
    
    print(f"Merged PDF saved at: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python merge_pdfs.py <folder_path> [output_filename]")
    else:
        folder = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "merged.pdf"
        merge_pdfs(folder, output_file)


"""
python merge_pdfs.py Marvellous_PDFs study_material.pdf
"""