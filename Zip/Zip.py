import zipfile

# slashes may need to change for MacOS or Linux
f = open("new_file1.txt", "w+")
f.write("Here is some text")
f.close()
# slashes may need to change for MacOS or Linux
f = open("new_file2.txt", "w+")
f.write(
    "Here is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some textHere is some text"
)
f.close()
comp_file = zipfile.ZipFile("comp_file.zip", "w")
comp_file.write("new_file1.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("new_file2.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()
