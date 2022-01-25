import tabula

# read pfd tables into a list of dataframes 

pdf_path = "resources/pdfs/Geotech.pdf"
dfs = tabula.read_pdf(pdf_path, stream=True)
