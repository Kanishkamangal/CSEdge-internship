import PyPDF2
import fitz
import os

def pdf_to_text(pdf_file, output_folder):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)

        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Extract text from each page
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()

            # Write extracted text to a text file
            text_file_path = os.path.join(output_folder, f"page_{page_num + 1}.txt")
            with open(text_file_path, 'w') as text_file:
                text_file.write(text)

    print("Text extraction completed. Text files saved in:", output_folder)

def pdf_to_images(pdf_file, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each page and save as image
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        image_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        pix = page.get_pixmap()
        pix.writePNG(image_path)

    print("Image conversion completed. Images saved in:", output_folder)

def main():
    pdf_file = 'sample.pdf'  # Change this to the path of your PDF file
    output_folder = 'output'  # Output folder where converted files will be saved

    # Convert PDF to text
    pdf_to_text(pdf_file, output_folder)

    # Convert PDF to images
    pdf_to_images(pdf_file, output_folder)

if __name__ == "_main_":
    main()