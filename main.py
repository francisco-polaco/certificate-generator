import os
import platform

import pandas as pd
from more_itertools import first
from pptx import Presentation

from config import get_config
from util.pdf import pptx_to_pdf_windows, pptx_to_pdf_linux
from util.pptx import replace_text_in_pptx

config = get_config()

# File paths
excel_file = config.sources.data.path  # Input Excel file
pptx_template = config.sources.template  # PowerPoint template
output_folder = config.output_dir  # Folder to store results

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Load Excel file
df = pd.read_excel(excel_file, sheet_name=config.sources.data.sheet)

df.columns.tolist()

# Process each row in the Excel file
for index, row in df.iterrows():
    replace_dict = {f"{column}": row[column] for column in df.columns.tolist()}

    prs = Presentation(pptx_template)

    for column, value in replace_dict.items():
        print(f"{{{column}}}")
        replace_text_in_pptx(prs, f"{{{column}}}", value)

    suffix_filename = first(replace_dict.values())

    output_pptx_filename = os.path.join(output_folder, f"{suffix_filename}.pptx")

    prs.save(output_pptx_filename)

    # PDF
    output_pdf_filename = os.path.join(output_folder, f"{suffix_filename}.pdf")
    print(f"Converting {output_pptx_filename} to PDF...")
    if platform.system() == "Windows":
        pptx_to_pdf_windows(output_pptx_filename, output_pdf_filename)
    else:
        pptx_to_pdf_linux(output_pptx_filename, output_folder)

print("✅ Process completed!")
