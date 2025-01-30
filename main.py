import os
import platform
import pandas as pd

from pptx import Presentation

from config import get_config

config = get_config()

# File paths
excel_file = config.sources.data.path  # Input Excel file
pptx_template = config.sources.template  # PowerPoint template
output_folder = config.output_dir  # Folder to store results

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Load Excel file
df = pd.read_excel(excel_file, sheet_name=config.sources.data.sheet)


# Function to replace text in PowerPoint
def replace_text_in_pptx(template, nome, output_pptx):
    prs = Presentation(template)

    # Replace {nome} in all slides
    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        if "{nome}" in run.text:
                            run.text = run.text.replace("{nome}", nome)

    # Save modified presentation
    prs.save(output_pptx)


# Function to convert PPTX to PDF (Windows only)
def pptx_to_pdf_windows(input_pptx, output_pdf):
    import comtypes.client

    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = 1

    presentation = powerpoint.Presentations.Open(os.path.abspath(input_pptx))
    presentation.SaveAs(os.path.abspath(output_pdf), 32)  # 32 = PDF format
    presentation.Close()
    powerpoint.Quit()


def pptx_to_pdf_linux(input_pptx):
    import subprocess

    subprocess.run(["soffice", "--headless", "--outdir", output_folder, "--convert-to", "pdf", input_pptx])


# Process each row in the Excel file
for index, row in df.iterrows():
    nome = row["nome"]
    pptx_filename = os.path.join(output_folder, f"{nome}.pptx")
    pdf_filename = os.path.join(output_folder, f"{nome}.pdf")

    print(f"Generating PPTX for {nome}...")
    replace_text_in_pptx(pptx_template, nome, pptx_filename)

    print(f"Converting {pptx_filename} to PDF...")
    if platform.system() == "Windows":
        pptx_to_pdf_windows(pptx_filename, pdf_filename)
    else:
        pptx_to_pdf_linux(pptx_filename)

print("✅ Process completed!")
