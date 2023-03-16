#  finds files in folders & subfolders of specified file types and
#  adds them to a zip archive at specified file output path

#  inputs: file extensions, directory path
#  outputs:  output file path (including name)

from zipfile import ZipFile
import os
directory = input("Enter relative path to directory in ./ format, with no trailing slash\n\r")
extensions = []
filepaths = []

while 1:
    response = input(
        "Enter file extension followed by enter and leave blank when all are entered\n\r"
    )

    if response != "":
        extensions.append(response)
    else:
        break

for root, directories, files in os.walk(directory):

    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                filepath = os.path.join(root, filename)
                filepaths.append(filepath)

with ZipFile("newZip.zip", 'w') as myzip:
    for filepath in filepaths:
        myzip.write(filepath)

print(filepaths)
