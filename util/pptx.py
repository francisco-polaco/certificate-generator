# Function to replace text in shapes
def replace_text_in_shapes(shapes, tag, text):
    for shape in shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    if tag in run.text:
                        run.text = run.text.replace(tag, text)

        elif shape.shape_type == 6:  # GroupShape -> need to recursively call this function on child shapes.
            replace_text_in_shapes(shape.shapes, tag, text)  # Recursively process child shapes


def replace_text_in_pptx(presentation, tag, text):
    # Replace tag in all slides
    for slide in presentation.slides:
        replace_text_in_shapes(slide.shapes, tag, text)
