import os


# Function to convert PPTX to PDF (Windows only)
def pptx_to_pdf_windows(input_pptx, output_pdf):
    import comtypes.client

    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = 1

    presentation = powerpoint.Presentations.Open(os.path.abspath(input_pptx))
    presentation.SaveAs(os.path.abspath(output_pdf), 32)  # 32 = PDF format
    presentation.Close()
    powerpoint.Quit()


def pptx_to_pdf_linux(input_pptx, output_folder):
    import subprocess

    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", input_pptx, "--outdir", output_folder])
