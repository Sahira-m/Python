import os
import shutil

f = open("practice.txt", "w+")
f.write("test")
f.close()

print(os.getcwd())  # to get the current working directory
print(os.listdir("C:\\Sahira"))  # to list the folders contain the path
# shutil.move( "practice.txt", "C:\\Sahira\\YH\YH-PYTHON\python-October\\pythonModules")
# used to move a file to specified directory

# os.unlink(path) which deletes a file at the path your provide
# os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
# shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.

# TO print folder subfolde and files for the specified path
filePath = "C:\\Sahira\\YH\YH-PYTHON\python-October"
for folder, sub_folders, files in os.walk(filePath):
    print("Currently looking at folder: " + folder)
    print("\n")
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: " + sub_fold)

    print("\n")

    print("THE FILES ARE: ")
    for f in files:
        print("\t File: " + f)
    print("\n")

    # Now look at subfolders
