import os
import platform

import pandas as pd
from pptx import Presentation

from config import get_config
from util.pdf import pptx_to_pdf_windows, pptx_to_pdf_linux
from util.pptx import replace_text_in_pptx

config = get_config()


def generate_pptx(replace_dict, template_path, output_path):
    prs = Presentation(template_path)

    for column, value in replace_dict.items():
        replace_text_in_pptx(prs, f"#{column}", value)

    prs.save(output_path)


def pptx_to_pdf(pptx_filename, output_folder, output_pdf_filename):
    if platform.system() == "Windows":
        pptx_to_pdf_windows(pptx_filename, output_pdf_filename)
    else:
        pptx_to_pdf_linux(pptx_filename, output_folder)


def main():
    # File paths
    excel_file = config.sources.data.path  # Input Excel file
    pptx_template = config.sources.template  # PowerPoint template
    output_folder = config.output.path  # directory to store results

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Load Excel file
    print(f"Reading {excel_file}...")
    df = pd.read_excel(excel_file, sheet_name=config.sources.data.sheet)

    # Process each row in the Excel file
    for index, row in df.iterrows():
        replace_dict = {f"{column}": row[column] for column in df.columns.tolist()}

        suffix_filename = "_".join(str(row[column]) for column in config.output.columns_to_filename)
        output_pptx_filename = os.path.join(output_folder, f"{suffix_filename}.pptx")

        # PPTX
        print(f"Generating {output_pptx_filename}...")
        generate_pptx(replace_dict, pptx_template, output_pptx_filename)

        # PDF
        print(f"Converting {output_pptx_filename} to PDF...")
        output_pdf_filename = os.path.join(output_folder, f"{suffix_filename}.pdf")
        pptx_to_pdf(output_pptx_filename, output_folder, output_pdf_filename)

    print("✅ Process completed!")


if __name__ == "__main__":
    main()
