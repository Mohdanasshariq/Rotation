def rotate_page(input_path, output_path, page_number, rotation_angle):
    with open(input_path, 'rb') as file:
        pdf_data = file.read()

    # Identify the start and end positions of the page content
    start_page_tag = b"/Type /Page\n"
    end_page_tag = b"\nendobj\n"
    page_start = pdf_data.find(start_page_tag, 0)
    page_end = pdf_data.find(end_page_tag, page_start)

    if page_start == -1 or page_end == -1:
        raise ValueError("Invalid PDF file or page number.")

    # Extract the page content
    page_content = pdf_data[page_start:page_end]

    # Find the rotation angle property and update it
    rotation_tag = b"/Rotate"
    rotation_start = page_content.find(rotation_tag)

    if rotation_start == -1:
        # If the rotation property doesn't exist, add it to the page content
        rotation_prop = b" /Rotate " + str(rotation_angle).encode() + b"\n"
        page_content = page_content[:-1] + rotation_prop + page_content[-1:]
    else:
        # If the rotation property exists, update its value
        rotation_end = page_content.find(b"\n", rotation_start)
        rotation_value = str(rotation_angle).encode()
        page_content = (
            page_content[:rotation_start] +
            rotation_tag + b" " + rotation_value + page_content[rotation_end:]
        )

    # Update the modified page content in the PDF data
    modified_pdf_data = (
        pdf_data[:page_start] +
        page_content +
        pdf_data[page_end:]
    )

    with open(output_path, 'wb') as output_file:
        output_file.write(modified_pdf_data)

# Usage example
input_file = 'input.pdf'
output_file = 'output.pdf'
page_number = 1  # The page number you want to rotate
rotation_angle = 90  # The rotation angle in degrees (e.g., 90 for clockwise)

rotate_page(input_file, output_file, page_number, rotation_angle)