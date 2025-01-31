# Function to replace text in PowerPoint
def replace_text_in_pptx(presentation, tag, text):
    # Replace tag in all slides
    for slide in presentation.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        if tag in run.text:
                            run.text = run.text.replace(tag, text)
