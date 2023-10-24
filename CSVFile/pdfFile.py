import PyPDF2

# pip install PyPDF     package
f = open("Project_Report1.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(f)
print("Length of file is", len(pdf_reader.pages))
page_number = 0
page_one = pdf_reader.pages[0]

# Extract the text
page_one_text = page_one.extract_text()
print("Extracted text from page 1 is", page_one_text)
# Write some data to a file
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one)
pdf_output = open("Some_New_Doc.pdf", "wb")
pdf_writer.write(pdf_output)
f.close()

f = open("Project_report1.pdf", "rb")

# List of every page's text.
# The index will correspond to the page number.
pdf_text = []

pdf_reader = PyPDF2.PdfReader(f)

for p in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[0]

    pdf_text.append(page.extract_text())

print("ALL DATA", pdf_text[1])
