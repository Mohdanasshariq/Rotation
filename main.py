import PyPDF2

def rotate_page(pdf_path, page_number, rotation_angle):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        for i, page in enumerate(reader.pages):
            if i + 1 == page_number:
                # Rotate the desired page
                page.rotate(rotation_angle)

            writer.add_page(page)

        with open('rotated.pdf', 'wb') as output_file:
            writer.write(output_file)

# Usage example
rotate_page('input.pdf', 1, 90)
