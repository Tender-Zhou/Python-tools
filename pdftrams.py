import os
import fitz

def convert_pdf_folder_to_images(pdf_folder, output_folder, zoom_x=2.0, zoom_y=2.0):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf" or ".PDF"):
            pdf_path = os.path.join(pdf_folder, filename)
            try:
                with fitz.open(pdf_path) as document:
                    base_name = os.path.splitext(filename)[0]
                    pdf_output_folder = os.path.join(output_folder, base_name)
                    if not os.path.exists(pdf_output_folder):
                        os.makedirs(pdf_output_folder)

                    for page_num in range(len(document)):
                        page = document.load_page(page_num)
                        mat = fitz.Matrix(zoom_x, zoom_y)
                        pix = page.get_pixmap(matrix=mat)

                        image_filename = f'{base_name}_page_{page_num + 1}.png'
                        image_filepath = os.path.join(pdf_output_folder, image_filename)
                        pix.save(image_filepath)
                        print(f'saved: {image_filepath}')
            except Exception as e:
                print(f"Failed to process {pdf_path}: {e}")
                
if __name__ == "__main__":
    pdf_folder = input("Enter the path of the folder containing PDF files: ")
    output_folder = input("Enter the path of the output folder: ")
    convert_pdf_folder_to_images(pdf_folder, output_folder)