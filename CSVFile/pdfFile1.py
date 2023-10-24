import csv

data = open("file1.csv", encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

link_str = ""
for row_num, data in enumerate(data_lines):
    link_str += data[row_num]
print(link_str)

"".join(link_str)
# To check a phone number exist a pdf file or not
import PyPDF2

f = open("Find_the_Phone_Number.pdf", "rb")
pdf = PyPDF2.PdfReader(f)
len(pdf.pages)
import re

pattern = r"\d{3}"
all_text = ""

for n in range(len(pdf.pages)):
    page = pdf.pages[n]
    page_text = page.extract_text()

    all_text = all_text + " " + page_text
for match in re.finditer(pattern, all_text):
    print(match)
