import csv

# open a csv file
data = open("example.csv", encoding="utf-8")
# Read csv file
csv_data = csv.reader(data)
# reformat it into a python object list of lists
data_lines = list(csv_data)
print("datas are\n", "\n", data_lines[0], "\n", data_lines[1])
# TO PRINT EMAIL OF FIRST 10 PERSON
email_data = []
first_letter = "b"
for item in data_lines[1:]:
    if first_letter in item[3][0]:
        email_data.append(item[3])
print("Email id starting with a", email_data)
print("full name of first five persons are ")
full_name = []
for items in data_lines[1:6]:
    full_name.append(items[1] + " " + items[2])
print(full_name)
# HOW TO WRITE DATA TO CSV FILE
file_to_output = open("newFileCreated.csv", mode="w", newline="")
csv_writer = csv.writer(file_to_output, delimiter=",")
csv_writer.writerow(["age", "name"])

csv_writer.writerows([["20", "sony"], ["1", "AAA"], ["2", "BBB"]])

file_to_output = open("newFileCreated.csv", mode="a", newline="")
csv_writer.writerows([["2", "CCC"], ["12", "KKK"], ["32", "kkkl"]])
